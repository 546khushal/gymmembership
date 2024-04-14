from django.db import models
from django.utils import timezone

class NewMemberData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()

'''
class MemberData(models.Model):
    imageurl = models.ImageField(default='-')
    imagename = models.ImageField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    dob = models.DateField()
    weight = models.FloatField()
    height_feet = models.IntegerField(default=0)
    height_inches = models.IntegerField(default=0)
    membership_plan_choices = [
        ('1month', '1month'),
        ('3months', '3months'),
        ('6months', '6months'),
        ('9months', '9months'),
        ('12months', '12months'),
    ]
    membership_plan = models.CharField(max_length=20, choices=membership_plan_choices)
    trainer = models.CharField(max_length=100)
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('online', 'Online'),
    ]
    pay_here_trainer = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    '''


class registerm(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.TextField()
    email = models.EmailField()
    passw = models.CharField(max_length=100)
    picname = models.FileField()
    picurl = models.FileField(default="-")
    dob = models.DateField(null=True)
    start = models.DateField(null=True)
    weight = models.CharField(max_length=10)
    heightf = models.CharField(max_length=10)  # Height in feet
    heighti = models.CharField(max_length=10)  # Height in inches
    membership_plan_choices = [
        ('1month', '1month'),
        ('3months', '3months'),
        ('6months', '6months'),
        ('9months', '9months'),
        ('12months', '12months'),
    ]
    membershipplan = models.CharField(max_length=100,choices=membership_plan_choices)
    
    trainer = models.CharField(max_length=100,)
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    feeamount = models.CharField(max_length=10)
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Online', 'Online'),
    ]
    pay = models.CharField(max_length=10,choices=PAYMENT_CHOICES)  # Payment method



class GymImage(models.Model):
    image = models.ImageField(upload_to='gymmedia/')

class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=100)
    mobile = models.TextField()
    email = models.EmailField()
    passw = models.CharField(max_length=100)
    picname = models.FileField()
    picurl = models.FileField(default="-")
    dob = models.DateField(null=True)  
    start = models.DateField(null=True)
    weight = models.CharField(max_length=10)
    heightf = models.CharField(max_length=10)  # Height in feet
    heighti = models.CharField(max_length=10)  # Height in inches
    

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    amount = models.TextField()
    membernumber =models.TextField()

def __str__(self):
    return self.tname 
