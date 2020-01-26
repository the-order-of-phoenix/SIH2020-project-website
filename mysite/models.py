from django.db import models
from django.contrib.auth.models import User


User_CHOICES = (
    ('shop','Vendor'),
    ('buyer', 'Customer')
)




class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete='CASCADE',related_name='type')
    c_name=models.CharField(max_length=25,blank=False)
    f_name=models.CharField(max_length=25,blank=False)
    m_name=models.CharField(max_length=25,blank=False)
    date = models.DateField(auto_now_add=True)
    #nationality_user=models.CharField(max_length=10, choices=User_nationality,blank=False)
    #category_user=models.CharField(max_length=10, choices=User_category,blank=False)
    #pwd_user=models.CharField(max_length=10, choices=User_pwd,blank=False)
    #employment_user=models.CharField(max_length=10, choices=User_CHOICES,blank=False)
    def __str__(self):
        return self.c_name
