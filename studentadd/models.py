from django.db import models


# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=20,verbose_name = 'Student Name')
    Email = models.EmailField(max_length=30,verbose_name = 'Student Email')
    
    def __str__(self):
        return self.Name
    
    