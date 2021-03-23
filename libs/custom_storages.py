from django.conf import settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage


class MediaS3BotoStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, name, content):
        name = super().save(name, content)
        self.local_storage._save(name, content)
        return name
