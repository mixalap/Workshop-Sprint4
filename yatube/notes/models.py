from django.db import models

class Note(models.Model):
    name = models.CharField(unique=True, max_length=50)
    text = models.TextField(max_length=300)
    publish = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
