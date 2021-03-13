from django.db import models

# Create your models here.
class Teacher(models.Model):
    name= models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name= models.CharField(max_length=64)
    std= models.IntegerField()
    board= models.CharField(max_length=5)
    num_absent= models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.std} {self.board})"

