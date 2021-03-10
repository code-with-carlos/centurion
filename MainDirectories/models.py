from django.db import models
from django.conf import settings

# generates database tables and also to access the data from python code 
class DataFile(models.Model): 
    data_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    file = models.FileField(upload_to = "data_files/")
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.file}"
    


