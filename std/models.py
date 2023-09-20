from django.db import models

# Create your models here.
class Student(models.Model):
     m_roll=models.CharField(max_length=150,null=False)
     m_name=models.CharField(max_length=150)
     m_email=models.CharField(max_length=150)
     m_adress=models.CharField(max_length=150)
     m_phone=models.CharField(max_length=150)
     def __str__(self):

        return self.m_name
   
