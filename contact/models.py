from django.db import models

# Create your models here.


# Model for enquiry form
class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    heading = models.CharField(max_length=250)
    message_body = models.TextField()
    acknowledged = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_submitted", "acknowledged"]
        indexes = [
            models.Index(fields=["-date_submitted"]),
        ]

    def __str__(self):
        return f"Comment {self.heading} by '\
                         {self.name} on {self.date_submitted}"