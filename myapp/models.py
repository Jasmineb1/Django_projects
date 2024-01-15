from django.db import models

class ClassRoom(models.Model):
    name= models.CharField(max_length=10)

# Create your models here.
class Student(models.Model):  #class name becomes the table name later on: appname_classname
    name = models.CharField(max_length=20)
    age= models.IntegerField()
    address= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    classroom= models.ForeignKey(ClassRoom, on_delete= models.CASCADE, related_name="classroom_students")
    


