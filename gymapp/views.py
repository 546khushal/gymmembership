from django.shortcuts import render,redirect
from .models import registerm
from .models import Trainer
from .models import Onsite
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.urls import reverse

from .models import GymImage
from .models import GymImages
from .models import Product, ProductImage
from .models import supliment, suplimentImage
from .models import equipment, equipmentImage
from .models import Blog

from django.http import HttpResponse
from .models import Product  # Import your Product model
from django.db import connection
from django.utils import timezone
from datetime import datetime
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage   #similar file dalte hai to url conflict ko solve krega

def index(request):
    images = GymImages.objects.all()
    gyms =GymImage.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        
        if name and mobile and gender and address:
            # Check if the record already exists in the database
            if not NewMemberData.objects.filter(name=name, mobile=mobile).exists():
                # Record doesn't exist, create a new one
                NewMemberData.objects.create(name=name, mobile=mobile, address=address, gender=gender)
                return render("Data inserted successfully.")
            else:
                return render("Record already exists.")
        else:
            return render("Please fill in all required fields.")
    
    return render(request, 'front/index.html',{'images': images ,'gyms':gyms})

def terms_and_conditions_view(request):
    return render(request, 'front/terms_and_conditions.html')

def calculate_bmi(request):
    if request.method == 'GET':
        feet = float(request.GET.get('feet', 0))
        inches = float(request.GET.get('inches', 0))
        weight = float(request.GET.get('weight', 0))
        age = float(request.GET.get('age', 0))

        if feet > 0 and inches >= 0 and weight > 0 and age > 0:
            height_in_meters = (feet * 0.3048) + (inches * 0.0254)
            bmi = weight / (height_in_meters * height_in_meters)
            classification = classify_bmi(bmi)

            return render(request, 'front/index.html', {'bmi': bmi, 'classification': classification})
        else:
            error = "All fields are required."
            return render(request, 'front/index.html', {'error': error})
    else:
        error = "Invalid request method."
        return render(request, 'front/index.html', {'error': error})

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal Weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def about(request):
    images = GymImages.objects.all()
    gyms =GymImage.objects.all()
    return render(request,'front/about.html',{'gyms':gyms,'images':images})

def login(request):
    return render(request,'front/login.html')

def ActivateMember(request):
    return render(request,'front/ActivateMember.html')

def ActivatedMember(request):
    return render(request,'front/ActivatedMember.html')

def owner(request):
    return render(request,'front/owner.html')
########################################ownerwork start
def ownerwork(request):
    search = request.GET.get('search', '')
    search_condition = ''

    if search:
        search_condition = f"WHERE memberid LIKE '%%{search}%%' OR name LIKE '%%{search}%%'"

    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM memberdata {search_condition}")
        rows = cursor.fetchall()

    members = []
    for row in rows:
        membership_status = "Active" if row[4] > timezone.now() else "Expired"
        status_color = "green" if membership_status == "Active" else "red"
        validity_color = "white" if row[4] > timezone.now() else "#FF6666"

        member = {
            'memberid': row[0],
            'image': row[1],
            'name': row[2],
            'mobile': row[3],
            'validitydate': row[4],
            'membership_status': membership_status,
            'status_color': status_color,
            'validity_color': validity_color
        }
        members.append(member)

    return render(request, 'ownerwork.html', {'members': members})

##############################ownerwork end 

def signup(request):
    return render(request,'front/signup.html')

def AddMember(request):
    return render(request,'front/AddMember.html')

def data(request):
    return render(request,'front/data.html')

def footer(request):
    gyms = GymImage.objects.all()
    return render(request,'front/footer.html',{'gyms':gyms})

#def navbar(request):
  #  return render(request,'navbar.html')



def location(request):
    gyms =GymImage.objects.all()
    return render(request,'front/location.html',{'gyms':gyms})

def NewMemberData(request):
    return render(request,'front/NewMemberData.html')
def memberdata(request):
    return render(request,'front/memberdata.html')
def Memberlist(request):
    return render(request,'front/Memberlist.html')
def Membership(request):
    gyms =GymImage.objects.all()
    return render(request,'front/membership.html',{'gyms':gyms})

def detail_login(request):
    if request.method == 'POST':
        member_id = request.POST.get('memberid')
        password = request.POST.get('password')

        # Check if the credentials exist in the database
        try:
            member = registerm.objects.get(member_id=member_id, passw=password)
        except registerm.DoesNotExist:
            # If the member_id or password is incorrect, display an error message or redirect to login page
            return render(request, 'back/error.html', {'error': 'Invalid credentials'})
        
        # If the credentials are correct, redirect to the member_mdetail page with the member_id
        return redirect('admin_mdetail', member_id=member.member_id)

    return render(request, 'membership.html')


def product(request):
     gyms =GymImage.objects.all() 
     products = Product.objects.all()
     
     return render(request, 'front/product.html', {'products': products,'gyms':gyms})
def productdata(request):
    return render(request,'front/productdata.html')
def trainer(request):
    return render(request,'front/trainer.html')






def pro_about(request):
    return render(request, 'front/pro_about.html')

def pro_home2(request):
    return render(request, 'front/pro_home2.html')

def pro_home3(request):
    return render(request, 'front/pro_home3.html')

def pro_blog_detail(request, blog_id):
    # Retrieve the desired Blog object using its ID
    blog_entry = Blog.objects.get(id=blog_id)
    return render(request, 'front/pro_blog_detail.html', {'blogd': [blog_entry]})

def pro_blog(request):
    blog = Blog.objects.all()
    return render(request, 'front/pro_blog.html',{'blog':blog})

def pro_contact(request):
    gyms =GymImage.objects.all() 
    return render(request, 'front/pro_contact.html',{'data':gyms})

def pro_index(request):
    products = Product.objects.all()
    gyms =GymImage.objects.all() 
    supliments =supliment.objects.all()
    equipments =equipment.objects.all()

    return render(request, 'front/pro_index.html', {'products': products,'gyms':gyms,'supliments':supliments,'equipments':equipments})


def pro_product_detail(request):
    return render(request, 'front/pro_product_detail.html')

def pro_product(request):
    products = Product.objects.all()
    gyms =GymImage.objects.all() 
    supliments =supliment.objects.all()
    equipments =equipment.objects.all()
    return render(request, 'front/pro_product.html',{'products': products,'gyms':gyms,'supliments':supliments,'equipments':equipments})

def pro_shoping_cart(request):
    return render(request, 'front/pro_shoping_cart.html')








#adimn back k liye 
def panel(request):
    return render(request,'back/admin_home.html')
def admin_404(request):
    return render(request,'back/admin_404.html')

def admin_blank(request):
    return render(request,'back/admin_blank.html')

def admin_charts(request):
    return render(request,'back/admin_charts.html')

def admin_forgot_password(request):
    return render(request,'back/admin_forgot_password.html')

def admin_home(request):
    return render(request,'back/admin_home.html')

def admin_index(request):
    return render(request,'back/admin_index.html')

def admin_login(request):
    return render(request,'back/admin_login.html')

def admin_register(request):
    trainer = Trainer.objects.all()
    return render(request,'back/admin_register.html',{'trainer':trainer})


def calculateEndDate(startdate, membershipplan):
    if startdate and membershipplan:  
        startDate = datetime.strptime(startdate, '%Y-%m-%d')
        endDate = startDate

        if membershipplan == "1":
            endDate += timedelta(days=30)  # Add 30 days for 1-month plan
        elif membershipplan == "3":
            endDate += timedelta(days=90)  # Add 90 days for 3-month plan
        elif membershipplan == "6":
            endDate += timedelta(days=180)  # Add 180 days for 6-month plan
        elif membershipplan == "9":
            endDate += timedelta(days=270)  # Add 270 days for 9-month plan
        elif membershipplan == "12":
            endDate += timedelta(days=365)  # Add 365 days for 12-month plan
        else:
            return None

        formattedEndDate = endDate.strftime('%Y-%m-%d')
        return formattedEndDate
    else:
        return None

def calculateDueDays(enddate):
    if enddate:
        endDate = datetime.strptime(enddate, '%Y-%m-%d')
        currentDate = datetime.now()
        timeDifference = endDate - currentDate
        dueDays = timeDifference.days
        return dueDays
    else:
        return None
    
def admin_tables(request):
    if request.method == "POST":
        # Handle form submission
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        weight = request.POST.get("weight")
        heightf = request.POST.get("heightf")
        heighti = request.POST.get("heighti")
        startdate = request.POST.get("start")
        membershipplan = request.POST.get("membershipplan")
        trainer = request.POST.get("trainer")
        gender = request.POST.get("gender")
        feeamount = request.POST.get("feeamount")
        pay = request.POST.get("pay")
        

        try:
            img = request.FILES['memberimg']
            
            # Check image size and format
            if str(img.content_type).startswith('image'):
                if img.size < 5000000:
                    # Save the image
                    fs = FileSystemStorage()
                    filename = fs.save(img.name, img)
                    url = fs.url(filename)
                    
                    # Create a new registerm object and save it
                    d = registerm.objects.create(name=name, email=email, mobile=mobile, passw=password, picname=filename, picurl=url, dob=dob, weight=weight, heightf=heightf, heighti=heighti, membershipplan=membershipplan, trainer=trainer, gender=gender, feeamount=feeamount, pay=pay, start=startdate)
                    # Redirect with success message
                    return redirect(reverse('admin_tables2') + f'?member_id={d.member_id}&member_name={d.name}')
                else:
                    error = "Please upload an image with size less than 5MB."
            else:
                error = "Please upload a valid image format."
        except KeyError:
            error = "Please upload an image."
        
        return render(request, 'back/error.html', {'error': error}) 
         
    else:
        error = "Please upload a valid image format."
        return render(request, 'back/error.html', {'error': error}) 

    
def admin_trainer(request):
    if request.method == "POST":
        # Handle form submission
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        dob = request.POST.get("dob")
        weight = request.POST.get("weight")
        heightf = request.POST.get("heightf")
        heighti = request.POST.get("heighti")
        gender = request.POST.get("gender")
        amount = request.POST.get("amount")
        membernumber = request.POST.get("membernumber")
        paydate =request.POST.get("paydate")

        try:
            img = request.FILES['trainerimg']
            
            # Check image size and format
            if img.content_type.startswith('image'):
                if img.size < 5000000:
                    fs = FileSystemStorage()
                    filename = fs.save(img.name, img)
                    url = fs.url(filename)
                    # Create a new Trainer object and save it
                    trainer = Trainer.objects.create(tname=name, email=email, mobile=mobile, passw=password, picname=filename, picurl=url, dob=dob, weight=weight, heightf=heightf, heighti=heighti, gender=gender, amount=amount, membernumber=membernumber,start=paydate)
                    return redirect('admin_trainer')  # Redirect to avoid resubmission
                else:
                    error = "Please upload an image with size less than 5MB."
            else:
                error = "Please upload a valid image format."
        except Exception:
            error = "Please upload an image."

        return render(request, 'back/error.html', {'error': error}) 
        
    else:
        # Handle GET request (rendering the form)
        trainers = Trainer.objects.all()  # Query all Trainer objects
        return render(request, 'back/admin_trainer.html', {'trainers': trainers})




def admin_tables2(request):
    data = registerm.objects.all()
    for item in data:
        if item.start:
            item.enddate = calculateEndDate(item.start.strftime('%Y-%m-%d'), item.membershipplan)
            item.duedays = calculateDueDays(item.enddate)
            # Determine status based on duedays
            if item.duedays is not None:
                if item.duedays <= 0:
                    item.status = "Expired"
                    item.bg_color = "red"
                    item.color = "white"
                else:
                    item.status = "Active"
                    item.bg_color = "white"
            else:
                item.status = "Unknown"
                item.bg_color = "white"  # Default background color
        else:
            item.enddate = None
            item.duedays = None
            item.status = "Unknown"
            item.bg_color = "white"  # Default background color

    return render(request, 'back/admin_tables2.html', {'data': data})



def admin_mdelete(request, member_id):
    try:
        member = registerm.objects.get(pk=member_id)
        member_name = member.name
        member.delete()
        # Redirect with delete_success parameter and member information
        return redirect(reverse('admin_tables2') + f'?delete_success=true&member_id={member_id}&member_name={member_name}')
    except registerm.DoesNotExist:
        # Handle if the object does not exist
        # Redirect back to the admin tables page
        return redirect('admin_tables2')
    

def admin_medit(request, member_id):
    edit = registerm.objects.get(pk=member_id)

    if request.method == "POST":
        # Update other fields
        edit.name = request.POST.get("name")
        edit.mobile = request.POST.get("mobile")
        edit.email = request.POST.get("email")
        edit.passw = request.POST.get("password")
        edit.dob = request.POST.get("dob")
        edit.weight = request.POST.get("weight")
        edit.heightf = request.POST.get("heightf")
        edit.heighti = request.POST.get("heighti")
        edit.start = request.POST.get("start")
        edit.membershipplan = request.POST.get("membershipplan")
        edit.trainer = request.POST.get("trainer")
        edit.gender = request.POST.get("gender")
        edit.feeamount = request.POST.get("feeamount")
        edit.pay = request.POST.get("pay")

        try:
            edit.save()
            # Redirect with success message
            return redirect(reverse('admin_tables2') + f'?member_id={edit.member_id}&member_name={edit.name}')
        except ValueError as e:
            # Handle validation errors
            error_message = str(e)
            return redirect(error_message)

    return render(request, 'back/admin_medit.html', {'edit': edit})


def admin_tdetail(request,trainer_id):
    # Retrieve the member with the given ID
    trainer = Trainer.objects.get(pk=trainer_id)            
        # Pass the member data to the template
    return render(request, 'back/admin_tdetail.html', {'details': trainer})

def admin_tdelete(request, trainer_id):
    try:
        trainer = Trainer.objects.get(pk=trainer_id)
        trainer_name = trainer.tname
        trainer.delete()
        # Redirect with delete_success parameter and member information
        return redirect(reverse('admin_trainer') + f'?delete_success=true&trainer_id={trainer_id}&trainer_name={trainer_name}')
    except registerm.DoesNotExist:
        # Handle if the object does not exist
        # Redirect back to the admin tables page
        return redirect('admin_trainer')
    
def admin_tedit(request,trainer_id):
    edit = Trainer.objects.get(pk=trainer_id)
    error = ""  # Define error variable

    if request.method == "POST":
                # Update other fields
        edit.tname = request.POST.get("name")
        edit.mobile = request.POST.get("mobile")
        edit.email = request.POST.get("email")

        edit.dob = request.POST.get("dob")
        edit.weight = request.POST.get("weight")
        edit.heightf = request.POST.get("heightf")
        edit.heighti = request.POST.get("heighti")
        edit.gender = request.POST.get("gender")
        edit.amount = request.POST.get("amount")
        edit.membernumber = request.POST.get("membernumber")
        edit.start =request.POST.get("paydate")    
            
        edit.save()

            # Redirect with success message
        return redirect(reverse('admin_trainer') + f'?trainer_id={edit.trainer_id}&trainer_name={edit.tname}')
    return render(request, 'back/admin_tedit.html', {'edit': edit, 'error': error})

def admin_reg_trainer(request):
    return render(request,'back/admin_reg_trainer.html')




def error(request):
    return render(request,'back/error.html')

def gym_imga_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('image')
        for file in files:
            filename = file.name
            # Save the file to the media/gymmedia folder
            with open(os.path.join(settings.MEDIA_ROOT, 'gymmedia', filename), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Create GymImage object for the file
            GymImages.objects.create(image=os.path.join('gymmedia', filename))
        return redirect('gym_imga_upload')
    images = GymImages.objects.all()
    return render(request, 'back/gym_imga_upload.html', {'images': images})
    
def gym_imgdelete(request,image_id):
    try:
        im = GymImages.objects.get(pk=image_id)
        im.delete()
        # Redirect with delete_success parameter and member information
        return redirect(reverse('gym_imga_upload') + f'?delete_success=true&image_id={image_id}')
    except registerm.DoesNotExist:
        # Handle if the object does not exist
        # Redirect back to the admin tables page
        return redirect('gym_imga_upload')
    

def custom_site(request):
    if request.method == "POST":
        # Retrieve form data
        gymname = request.POST.get("gymname")
        gymemail = request.POST.get("gymemail")
        mobile = request.POST.get("mobile")
        mgymtime = request.POST.get("mgymtime")
        egymtime = request.POST.get("egymtime")
        addressline1 = request.POST.get("addressl1")
        addressline2 = request.POST.get("addressl2")
        addressline3 = request.POST.get("addressl3")
        addressline4 = request.POST.get("addressl4")
        addressline5 = request.POST.get("addressl5")
        addressline6 = request.POST.get("addressl6")
        maplink = request.POST.get("maplink")

        instalink = request.POST.get("instalink")
        fblink = request.POST.get("fblink")
        ytlink = request.POST.get("ytlink")
        ownername = request.POST.get("ownername")
        experience = request.POST.get("experience")
        opend = request.POST.get("opend")
        
        GymImage.objects.all().delete()  # Delete all existing entries
        
        ownerimg = request.FILES.get("ownerimg")
        if ownerimg:
            # Check image size and format
            if ownerimg.content_type.startswith('image'):
                if ownerimg.size < 5000000:
                    fs = FileSystemStorage()
                    filename = fs.save(ownerimg.name, ownerimg)
                    url = fs.url(filename)
                    # Create a new GymImage object and save it
                    gym_image = GymImage.objects.create(
                       
                        gymname=gymname,
                        gymemail=gymemail,
                        mobile=mobile,
                        mgymtime=mgymtime,
                        egymtime=egymtime,
                        picname=filename,
                        picurl=url,
                        addressline1=addressline1,
                        addressline2=addressline2,
                        addressline3=addressline3,
                        addressline4=addressline4,
                        addressline5=addressline5,
                        addressline6=addressline6,
                        maplink =maplink,
                        instalink=instalink,
                        fblink=fblink,
                        ytlink=ytlink,
                        ownername=ownername,
                        experience=experience,
                        opend=opend
                    )
                    return redirect('display_gym_info')  # Redirect to avoid resubmission
                else:
                    error = "Please upload an image with size less than 5MB."
            else:
                error = "Please upload a valid image format."
        else:
            error = "Please upload an image."
            
        return render(request, 'back/error.html', {'error': error}) 

    gym = GymImage.objects.all()  # Query all GymImage objects
    return render(request, 'back/custom_site.html', {'gym_images': gym})

        
def display_gym_info(request):
    gym_images = GymImage.objects.all()
    return render(request, 'back/custom_site.html', {'gym_images': gym_images})        







def admin_mdetail(request,member_id):    
   # Retrieve the member with the given ID
    member = registerm.objects.get(pk=member_id)
    end_date = calculateEndDate(member.start.strftime('%Y-%m-%d'), member.membershipplan)
    due_days = calculateDueDays(end_date)
    member.enddate = end_date
    member.duedays = due_days
            
        # Pass the member data to the template
    return render(request, 'back/admin_mdetail.html', {'details': member})

def admin_expaire(request):
        # Get all members
    all_members = registerm.objects.all()
    
    # Filter active members
    active_members = []
    for member in all_members:
        if member.start:
            end_date = calculateEndDate(member.start.strftime('%Y-%m-%d'), member.membershipplan)
            due_days = calculateDueDays(end_date)
            if due_days is not None and due_days <= 0:
                member.enddate = end_date
                member.duedays = due_days
                member.status = "Expaire"
                active_members.append(member)

    return render(request, 'back/admin_active.html', {'data': active_members})



def admin_active(request):
    # Get all members
    all_members = registerm.objects.all()
    
    # Filter active members
    active_members = []
    for member in all_members:
        if member.start:
            end_date = calculateEndDate(member.start.strftime('%Y-%m-%d'), member.membershipplan)
            due_days = calculateDueDays(end_date)
            if due_days is not None and due_days > 0:
                member.enddate = end_date
                member.duedays = due_days
                member.status = "Active"
                active_members.append(member)

    return render(request, 'back/admin_active.html', {'data': active_members})

                
    
def admin_total(request):
    # Get all members
    all_members = registerm.objects.all()
    
    # Initialize counters
    total_members = all_members.count()
    total_active_members = 0
    total_inactive_members = 0
    
    # Calculate active and inactive members
    for member in all_members:
        if member.start:
            end_date = calculateEndDate(member.start.strftime('%Y-%m-%d'), member.membershipplan)
            due_days = calculateDueDays(end_date)
            if due_days is not None and due_days > 0:
                total_active_members += 1
            else:
                total_inactive_members += 1

    return render(request, 'back/admin_total.html', {'total_members': total_members,'total_active_members': total_active_members,'total_inactive_members': total_inactive_members
    })
def admin_siteuser(request):
    datasite = Onsite.objects.all()

    return render(request, 'back/admin_siteuser.html', {'datasite': datasite})


def memberfromsite(request):
    if request.method == "POST":
        # Handle form submission
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        
        # Check if a user with similar name and mobile already exists
        existing_user = Onsite.objects.filter(name=name, mobile=mobile).exists()
        if existing_user:
            error="! User already exists with similar Name and Mobile number."
            return render(request, 'front/membership.html', {'error': error})
        
        # Save form data to the Onsite table
        Onsite.objects.create(name=name, email=email, mobile=mobile, gender=gender)
        
        # Query all Onsite objects including the newly added one
        datasite = Onsite.objects.all()

        return render(request, 'back/admin_siteuser.html', {'datasite': datasite})
    else:
        # If it's a GET request, render the empty form
        return render(request, 'back/admin_siteuser.html')


def admin_onsitereg(request,siteuser_id):
    siteuser = Onsite.objects.get(pk=siteuser_id)

    return render(request, 'back/admin_onsitereg.html', {'siteuser': siteuser})    
    

def admin_onsiteedit(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        passw = request.POST.get("password")
        dob = request.POST.get("dob")
        weight = request.POST.get("weight")
        heightf = request.POST.get("heightf")
        heighti = request.POST.get("heighti")
        start = request.POST.get("start")
        membershipplan = request.POST.get("membershipplan")
        trainer = request.POST.get("trainer")
        feeamount = request.POST.get("feeamount")
        pay = request.POST.get("pay") 
        siteuser_id = request.POST.get("siteuser_id")
        
        # Get the Onsite object
        site = Onsite.objects.get(pk=siteuser_id)
        # Delete the existing Onsite entry
        site.delete()

        try:
            # Check if an image was uploaded
            img = request.FILES['memberimg']
            # Check image size and format
            if img.content_type.startswith('image') and img.size < 5000000:
                fs = FileSystemStorage()
                filename = fs.save(img.name, img)
                url = fs.url(filename)
                # Create a new entry in the registerm table
                data = registerm.objects.create(
                    name=name,
                    mobile=mobile,
                    email=email,
                    gender=gender,
                    passw=passw,
                    picname=filename,
                    picurl=url,
                    dob=dob,
                    weight=weight,
                    heightf=heightf,
                    heighti=heighti,
                    start=start,
                    membershipplan=membershipplan,
                    trainer=trainer,
                    feeamount=feeamount,
                    pay=pay
                )  
                return redirect('admin_tables2')  # Redirect to avoid resubmission
            else:
                error = "Please upload a valid image with size less than 5MB."
        except Exception as e:
            error = "An error occurred: " + str(e)
        return render(request, 'back/error.html', {'error': error})    

    return render(request, 'back/admin_table2.html')





def add_product(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        price = request.POST.get('price')
        details = request.POST.get('details')
        images = request.FILES.getlist('images')  # Get list of uploaded images

        # Create a new Product instance
        product = Product.objects.create(name=name, price=price, details=details)

        # Create ProductImage instances for each uploaded image
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        # Redirect to the product list page or another page
        return redirect('product_list')
    else:
        # Render the form page if it's a GET request
        return render(request, 'back/add_product.html')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.name = request.POST.get('product_name')
        product.price = request.POST.get('product_price')
        product.details = request.POST.get('product_details')
        product.count = request.POST.get('product_count', 0)  # Assuming product count is optional
        product.save()

        # Update product images
        for i in range(1, 5):
            image_field = f'product_image{i}'
            image = request.FILES.get(image_field)
            if image:
                ProductImage.objects.create(product=product, image=image)

        return redirect('product_list')  # Redirect to product list page

    return render(request, 'back/edit_product.html', {'product': product})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_list')  # Redirect to product list page

def product_list(request):
    products = Product.objects.all()
    return render(request, 'back/product_list.html', {'products': products})
















def add_protein(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        price = request.POST.get('price')
        details = request.POST.get('details')
        images = request.FILES.getlist('images')  # Get list of uploaded images

        # Create a new Product instance
        product = supliment.objects.create(sname=name, sprice=price, sdetails=details)

        # Create ProductImage instances for each uploaded image
        for image in images:
           suplimentImage.objects.create(sproduct=product, simage=image)

        # Redirect to the product list page or another page
        return redirect('protein_list')
    else:
        # Render the form page if it's a GET request
        return render(request, 'back/add_protein.html')

def edit_protein(request, product_id):
    product = supliment.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.sname = request.POST.get('product_name')
        product.sprice = request.POST.get('product_price')
        product.sdetails = request.POST.get('product_details')
        product.scount = request.POST.get('product_count', 0)  # Assuming product count is optional
        product.save()

        # Update product images
        for i in range(1, 5):
            image_field = f'product_image{i}'
            image = request.FILES.get(image_field)
            if image:
                suplimentImage.objects.create(supliment=product, simage=image)

        return redirect('protein_list')  # Redirect to product list page

    return render(request, 'back/edit_protein.html', {'supliment': product})

def delete_protein(request, product_id):
    product = supliment.objects.get(id=product_id)
    product.delete()
    return redirect('protein_list')  # Redirect to product list page

def protein_list(request):
    products =supliment.objects.all()
    return render(request, 'back/protein_list.html', {'supliment': products})











def add_equipment(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        price = request.POST.get('price')
        details = request.POST.get('details')
        images = request.FILES.getlist('images')  # Get list of uploaded images

        # Create a new Product instance
        product = equipment.objects.create(ename=name, eprice=price, edetails=details)

        # Create ProductImage instances for each uploaded image
        for image in images:
            equipmentImage.objects.create(equipment=product, eimage=image)

        # Redirect to the product list page or another page
        return redirect('equipment_list')
    else:
        # Render the form page if it's a GET request
        return render(request, 'back/add_equipment.html')

def edit_equipment(request, product_id):
    product = equipment.objects.get(id=product_id)
    
    if request.method == 'POST':
        product.ename = request.POST.get('product_name')
        product.eprice = request.POST.get('product_price')
        product.edetails = request.POST.get('product_details')
        product.ecount = request.POST.get('product_count', 0)  # Assuming product count is optional
        product.save()

        # Update product images
        for i in range(1, 5):
            image_field = f'product_image{i}'
            image = request.FILES.get(image_field)
            if image:
                equipmentImage.objects.create(equipment=product, eimage=image)

        return redirect('equipment_list')  # Redirect to product list page

    return render(request, 'back/edit_equipment.html', {'equipment': product})

def delete_equipment(request, product_id):
    product = equipment.objects.get(id=product_id)
    product.delete()
    return redirect('equipment_list')  # Redirect to product list page

def equipment_list(request):
    products = equipment.objects.all()
    return render(request, 'back/equipment_list.html', {'equipment': products})


def add_blog(request):
    blogd = Blog.objects.all()
    if request.method == 'POST':
        # Get form data from POST request
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        date = request.POST.get('date')
        categories = request.POST.get('categories')
        image = request.FILES.get('image')

        # Create a new blog object
        blog = Blog(
            title=title,
            content=content,
            author=author,
            date=datetime.strptime(date, '%Y-%m-%d').date(),  # Assuming date is in 'YYYY-MM-DD' format
            categories=categories,
            image=image
        )
        blog.save()
        blog = Blog.objects.all()
        return render(request, 'back/add_blog.html', {'blogs': blog})
    else:
        
        return render(request, 'back/add_blog.html', {'blogs': blogd})
    
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete() 
    
    return redirect('add_blog')
    