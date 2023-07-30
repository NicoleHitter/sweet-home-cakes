from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    """
    Users can send message
    """
    # Set topic options for message
    ORDER = 'OR'
    PRODUCT = 'PR'
    OTHER = 'OT'
   
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Set ordering and plural name
        """
        ordering = ['-date_created']
        verbose_name_plural = 'Leave Feedback'

    def __str__(self):
        return f'Message from {self.name}'

