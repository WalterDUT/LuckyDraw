from django.db import models

# Create your models here.
class Customer(models.Model):
    pass

def handle_uploaded_file(requestFile):
    pass

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)