from django.db import models
from django.contrib.auth.models import User





class Student_tab(models.Model):
    s_name = models.CharField(max_length=200)
    s_class = models.IntegerField()
    s_address = models.CharField(max_length=200)
    s_phone = models.CharField(max_length=200)
      


    def __unicode__(self):
        return self.name

# class auth_user_extended(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_role = models.CharField(max_length=100)
#     is_designation = models.CharField(max_length=100)
#     profile_image = models.ImageField(upload_to='profile_pics', blank=True)
#     mobile_no = models.CharField(max_length=100)



class auth_ext(models.Model):
      designation = models.CharField(max_length = 50)
      user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, to_field='username',db_column='user_id',related_name='addittive')


class employee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    # file = models.ImageField(blank=True, null=True, upload_to='cs_files')  
      


    def __unicode__(self):
        return self.name


class csv_files(models.Model):
   
    file = models.FileField(blank=True, null=True, upload_to='cs_files')  
      


    def __unicode__(self):
        return self.name