from django.db import models
import hashlib

class Url(models.Model):
    original_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=50) 
    created_on = models.DateTimeField(auto_now_add=True)

    def create_short_url(original):
        return hashlib.shake_256(original.encode()).hexdigest(5)