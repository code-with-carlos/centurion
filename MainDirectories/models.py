from django.db import models
from django.conf import settings

# generates database tables and also to access the data from python code 
class DataFile(models.Model): 
    data_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    file = models.FileField(upload_to = "data_files/")
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f"{self.file}"
    

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    USER_TYPE_DATA_OWNER = 1
    USER_TYPE_AUTH_USER = 2
    USER_TYPE_CHOICES = (
        (USER_TYPE_DATA_OWNER, 'Data Owner'),
        (USER_TYPE_AUTH_USER, 'Auth User'),
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.get_user_type_display()})'


    