from django.shortcuts import render,redirect
from .models import registerm
from .models import Trainer
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

from django.http import HttpResponse
from .models import Product  # Import your Product model
from django.db import connection
from django.utils import timezone
from datetime import datetime
from django.core.files.storage import FileSystemStorage   #similar file dalte hai to url conflict ko solve krega

def index(request):
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
                return HttpResponse("Data inserted successfully.")
            else:
                return HttpResponse("Record already exists.")
        else:
            return HttpResponse("Please fill in all required fields.")

    return render(request, 'front/index.html')

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
    return render(request,'front/about.html')

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
    return render(request,'front/footer.html')

#def navbar(request):
  #  return render(request,'navbar.html')



def location(request):
    return render(request,'front/location.html')

def NewMemberData(request):
    return render(request,'front/NewMemberData.html')
def memberdata(request):
    return render(request,'front/memberdata.html')
def Memberlist(request):
    return render(request,'front/Memberlist.html')
def Membership(request):
    return render(request,'front/membership.html')
def product(request):
     products = Product.objects.all()  # Fetch all products from the database
     return render(request, 'front/product.html', {'products': products})
def productdata(request):
    return render(request,'front/productdata.html')
def trainer(request):
    return render(request,'front/trainer.html')

#adimn back k liye 
def panel(request):
    return render(request,'back/admin_home.html')
def admin_404(request):
    return render(request,'back/admin_404.html')

def admin_blank(request):
    return render(request,'back/admin_blank.html')

def admin_buttons(request):
    return render(request,'back/admin_buttons.html')

def admin_cards(request):
    return render(request,'back/admin_cards.html')

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
    return render(request,'back/admin_register.html')


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
                    
                    return redirect('admin_tables2')
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
       
        try:
            img = request.FILES['trainerimg']
            
            # Check image size and format
            if str(img.content_type).startswith('image'):
                if img.size < 5000000:
                    fs = FileSystemStorage()
                    filename = fs.save(img.name, img)
                    url = fs.url(filename)
                    # Create a new Trainer object and save it
                    trainer = Trainer.objects.create(tname=name, email=email, mobile=mobile, passw=password, picname=filename, picurl=url, dob=dob, weight=weight, heightf=heightf, heighti=heighti, gender=gender, amount=amount, membernumber=membernumber)
                    return render(request, 'back/admin_trainer.html', {'trainer': trainer})
                else:
                    error = "Please upload an image with size less than 5MB."
            else:
                error = "Please upload a valid image format."
            return render(request, 'back/error.html', {'error': error}) 
            
        except:
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
        else:
            item.enddate = None
            item.duedays = None
    return render(request,'back/admin_tables2.html',{'data':data})

def admin_reg_trainer(request):
    return render(request,'back/admin_reg_trainer.html')


def admin_utilities_animation(request):
    return render(request,'back/admin_utilities_animation.html')

def admin_utilities_border(request):
    return render(request,'back/admin_utilities_border.html')

def admin_utilities_color(request):
    return render(request,'back/admin_utilities_color.html')

def admin_utilities_other(request):
    return render(request,'back/admin_utilities_other.html')

def error(request):
    return render(request,'back/error.html')
def admin_expaire(request):
    return render(request,'back/admin_expaire.html')
def admin_active(request):
    return render(request,'back/admin_active.html')
def admin_total(request):
    return render(request,'back/admin_total.html')