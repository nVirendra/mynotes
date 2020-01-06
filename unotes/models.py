from django.db import models


# Create your models here.
class Unote(models.Model):
    file_id = models.AutoField
    file_name = models.CharField(max_length=50)
    file_desc = models.CharField(max_length=200, default="")
    file = models.FileField(upload_to='file')

    def __str__(self):
        return self.file_name
