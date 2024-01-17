from django.db import models

class ClassRoom(models.Model):
    name= models.CharField(max_length=10)
    def __str__(self):
        return self.name

# Create your models here.
class Student(models.Model):  #class name becomes the table name later on: appname_classname
    name = models.CharField(max_length=20)
    age= models.IntegerField()
    address= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    classroom= models.ForeignKey(ClassRoom, on_delete= models.CASCADE, related_name="classroom_students", null= True, blank= True)
    def __str__(self):
        return self.name
    
    
class StudentProfile(models.Model):
    student= models.OneToOneField(Student, on_delete=models.CASCADE)
    phone= models.CharField(max_length=14)
    roll_no= models.IntegerField()
    bio= models.TextField(max_length=500)
    profile_picture=models.FileField(null=True, blank=True, upload_to="profile_pictures")
    def __str__(self):
        return self.student

#many to many
class Publication(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    def __str__(self):
        return self.headline


