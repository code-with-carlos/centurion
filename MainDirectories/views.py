from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from MainDirectories import models as main_models
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class DataOwnerHomeView (LoginRequiredMixin, TemplateView):
    template_name = "main/data_owner_home_view.html"

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
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())