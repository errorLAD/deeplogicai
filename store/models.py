from django.db import models

from django.contrib.auth.models import User

import datetime
import os
# Create your models here.

class file_upload(models.Model):
    ids = models.AutoField(primary_key=True)
    pdf_file = models.FileField(upload_to='')
    
    def __str__(self):
        return self.file_name
