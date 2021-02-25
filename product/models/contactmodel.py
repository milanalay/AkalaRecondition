from django.db import models




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name



class Newsletter(models.Model):
    email = models.EmailField(max_length=100)


    def __str__(self):
        return self.email