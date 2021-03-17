from django.contrib import admin
from MainDirectories import models as main_models

admin.site.register(main_models.DataFile)
admin.site.register(main_models.UserProfile)
admin.site.register(main_models.SendFile)
