from django.db import models
from django.utils import timezone
import uuid

class NewMemberData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.name
    


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


class GymImages(models.Model):
    image = models.ImageField(upload_to='gymmedia/')
class GymImage(models.Model):
    
    gymname = models.CharField(max_length=100)
    gymemail = models.EmailField()
    mobile = models.CharField(max_length=15)
    mgymtime = models.CharField(max_length=100)
    egymtime = models.CharField(max_length=100)
    maplink = models.CharField(max_length=1000)
    addressline1  = models.CharField(max_length=255)
    addressline2  = models.CharField(max_length=255)
    addressline3  = models.CharField(max_length=255)
    addressline4  = models.CharField(max_length=255)
    addressline5  = models.CharField(max_length=255)
    addressline6  = models.CharField(max_length=255)
    
    instalink = models.URLField(blank=True)
    fblink = models.URLField(blank=True)
    ytlink = models.URLField(blank=True)
    ownername = models.CharField(max_length=100)
    picname = models.FileField()
    picurl = models.FileField(default="-")
    experience = models.CharField(max_length=50)
    opend =models.CharField(max_length=20)
     
class Onsite(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()    
    created_at = models.DateTimeField(auto_now_add=True)



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


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    count = models.IntegerField(default=0)  # Example field, you can adjust as needed
    image = models.ImageField(upload_to='product_images')

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')   


class supliment(models.Model):
    sname = models.CharField(max_length=100)
    sprice = models.DecimalField(max_digits=10, decimal_places=2)
    sdetails = models.TextField()
    scount = models.IntegerField(default=0)  # Example field, you can adjust as needed
    simage = models.ImageField(upload_to='product_images')

class suplimentImage(models.Model):
    sproduct = models.ForeignKey(supliment, related_name='images', on_delete=models.CASCADE)
    simage = models.ImageField(upload_to='product_images')  

class equipment(models.Model):
    ename = models.CharField(max_length=100)
    eprice = models.DecimalField(max_digits=10, decimal_places=2)
    edetails = models.TextField()
    ecount = models.IntegerField(default=0)  # Example field, you can adjust as needed
    eimage = models.ImageField(upload_to='product_images')

class equipmentImage(models.Model):
    eproduct = models.ForeignKey(equipment, related_name='images', on_delete=models.CASCADE)
    eimage = models.ImageField(upload_to='product_images')  


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    date = models.DateField(null=True)
    categories = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/') 
    extra  =  models.CharField(max_length=200)        

def __str__(self):
    return self.tname 
