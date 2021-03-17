from django.db import models
from django.conf import settings

# generates database tables and also to access the data from python code 
class DataFile(models.Model): 
    data_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    key = models.BinaryField(max_length= 16)
    file = models.FileField(upload_to = "data_files/")
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.file}"
    

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publickeygen = models.BinaryField()
    privatekeygen = models.BinaryField()


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class SendFile(models.Model):
    data_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files_sent")
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files_received")
    file = models.ForeignKey(DataFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    