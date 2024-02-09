from django.db import models

# Create your models here.
class Profile(models.Model):
    rollnumber = models.IntegerField(primary_key=True)
    registration_no = models.IntegerField()
    student_name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    year = models.IntegerField()
    semester = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=100)

    def __str__(self):
        return self.student_name