from django.db import models


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


class Address(models.Model):
    """
    Admin can add or update company address for the page
    """
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=58)
    phone2 = models.CharField(max_length=58, blank=True, null=True)
    email = models.EmailField(max_length=100)
    email2 = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.address