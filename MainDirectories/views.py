from django.views.generic import TemplateView, ListView, CreateView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from MainDirectories import models as main_models
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from django.core.mail import EmailMessage
from django_downloadview import ObjectDownloadView



class DataOwnerHomeView (LoginRequiredMixin, TemplateView):
    template_name = "main/data_owner_home_view.html"
    def get_context_data(self,*args, **kwargs): 
        #aes_encryption()
        return super().get_context_data(*args, **kwargs)

class DataFileListView (LoginRequiredMixin, ListView):
    template_name = "main/data_file_list_view.html"
    model = main_models.DataFile

class DataFileUploadView(LoginRequiredMixin, CreateView):
    template_name = "main/data_file_upload_view.html"
    model = main_models.DataFile 
    fields = ['file']
    success_url = reverse_lazy('data_file_list')
    
    #overriding django library to set data owner to login user 
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.data_owner = self.request.user
        print('saving', self.object.file.name)
        file_data = self.object.file.read()
        key, encrypted_data = aes_encryption(file_data)
        print('key', key)
        new_file_name_for_encryption = f'{self.object.file.name}.Encrypted'
        self.object.key = key
        self.object.file.save(new_file_name_for_encryption, ContentFile(encrypted_data))
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
    

def get_aes_cipher(key):
    aesObj = AES.new(key, AES.MODE_CBC, b'This is an IV456')
    return aesObj

    
def aes_encryption(data): 
    print ("Test")
    #create a cipher object using the random secret
    #’ AB 3D 12 EE 44’ is our key file K 
    key = get_random_bytes(16)
    aesObj = get_aes_cipher(key) 
    # replace below 
    # the reading the data from my file to upload. Open file and read the data from the file     
    #data = b"My bank password: passwd@#126548My bank password: passwd@#126548My bank password: passwd@#126548My bank password: passwd@#126548"
    print(len(data))
    length = 16 - (len(data) % 16)
    data += bytes([length]) * length
    
    #Encrypt Data, its just one line 
    encrypted_data = aesObj.encrypt(data)
    print('encrypted_data', encrypted_data)
    return key, encrypted_data

def aes_decryption(encrypted_data, key):    
    #Decrypt data
    #aesObj1 = AES.new('AB 3D 12 EE 44  ', AES.MODE_CBC, 'This is an IV456')
    aesObj = get_aes_cipher(key) 
    decrypted_data = aesObj.decrypt(encrypted_data)
    print(decrypted_data)
    
class SendFileView(LoginRequiredMixin, CreateView):
    template_name = "main/send_file_view.html"
    model = main_models.SendFile 
    fields = ['file', 'auth_user']
    success_url = reverse_lazy('data_file_list')
    
    #overriding django library to set data owner to login user 
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.data_owner = self.request.user
        self.object.save()
        # this is where we send an email 
        send_user_email(self.object.auth_user, self.object.data_owner)
        return HttpResponseRedirect(self.get_success_url())
    
# function for sending email 
def send_user_email(auth_user, data_owner):
    sender_email = data_owner.email 
    receiver_email = auth_user.email 
    email = EmailMessage(
        'You got a file',
        'we are about to workout #todo',
        settings.ADMIN_EMAIL,
        [receiver_email],
        reply_to=[sender_email], 
    )
    email.send()
    
class DownloadView(ObjectDownloadView): 
    model = main_models.DataFile
    
    
    
