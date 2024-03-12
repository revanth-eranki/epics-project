from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



# Create your models here.
# class Profile(models.Model):
#     rollnumber = models.IntegerField(primary_key=True)
#     registration_no = models.IntegerField()
#     student_name = models.CharField(max_length=50)
#     branch = models.CharField(max_length=50)
#     year = models.IntegerField()
#     semester = models.IntegerField()
#     mobile_number = models.CharField(max_length=15)
#     email_id = models.EmailField(max_length=100)

#     def __str__(self):
#         return self.student_name
    

class Course(models.Model):
    course_id = models.CharField(primary_key=True)
    course_name = models.CharField(blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'

class Enrollment(models.Model):
    course = models.OneToOneField(Course, models.DO_NOTHING, primary_key=True)  # The composite primary key (course_id, user_name) found, that is not supported. The first column is selected.
    user_name = models.ForeignKey('Student1', models.DO_NOTHING, db_column='user_name')
    semester = models.CharField(blank=True, null=True)
    grades = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollment'
        unique_together = (('course', 'user_name'),)


class Student1(models.Model):
    user_name = models.CharField(primary_key=True)
    roll_number = models.CharField(blank=True, null=True)
    reg_num = models.CharField(blank=True, null=True)
    email_id = models.CharField(blank=True, null=True)
    mobille_num = models.CharField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)
    branch = models.CharField(blank=True, null=True)
    semester = models.CharField(blank=True, null=True)
    category = models.CharField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_1'
