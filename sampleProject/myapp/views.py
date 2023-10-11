from django.shortcuts import render,redirect
from .models import userSignup
from .forms import userSignupForm,notesForm,updateForm,contactForm
from django.contrib import messages
from django.contrib.auth import logout
import requests,random
from django.core.mail import send_mail
from sampleProject import settings


# Create your views here.
def index(request):
    cuser=request.session.get('user')
    
    if request.method=='POST':  #root condition

        unm=request.POST['email']
        pwd=request.POST['password']
        user=userSignup.objects.filter(email=unm,password=pwd)

        uid=userSignup.objects.get(email=unm)
        print(uid.id)            
        if user:
                print("Logged in")
                #username=userSignup.objects.get('firstname')
                request.session['user']=unm #session creation
                request.session['uid']=uid.id
                return redirect('home')
                    
        else:
                print("Username/password incorrect !")
                messages.error(request,'Either username or password is incorrect')

    return render(request,'index.html',{'user':cuser})
    

def notes(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        myquery=notesForm(request.POST,request.FILES)
        if myquery.is_valid():
            myquery.save()
            print("Your query has been submitted")
            messages.info(request,"Your query has been submitted")
        else:
            print(myquery.errors)
            messages.error(request,"Something went wrong !")

    return render(request,'notes.html',{'user':cuser})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cid=userSignup.objects.get(id=uid)
    cuser=userSignup.objects.get(id=uid)

    if request.method=='POST':
        update=updateForm(request.POST,instance=cid)
        if update.is_valid():
            update.save()
            print('Your profile has been updated...')
            return redirect('/')
        else:
            print(update.errors)
    
    return render(request,'profile.html',{'user':user,'uid':cuser})

def about(request):
    cuser=request.session.get('user')
    return render(request,'about.html',{'user':cuser})

def contact(request):
    cuser=request.session.get('user')
    if request.method=='POST':
        contact=contactForm(request.POST)
        if contact.is_valid():
            contact.save()
            print("Your message has been sent successfully")
            #Email Sending
            user=request.POST['cntname']
            sub='Message received'
            msg=f'Hello {user} !\n We have just received your message !\nWe are pleased to inform you that your message is important to us. You will get a reply within next 48hrs after consideration.We Hope you have enjoyed our service :) !\nFor further query , contact us on : +919106761736 \nThank you.'
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['cntemail']]

            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)

            messages.info(request,'Your message has been sent !')
            
         
    return render(request,'contact.html',{'user':cuser})

def home(request):
    cuser=request.session.get('user')

    return render(request,'home.html',{'user':cuser})

def register(request):
    if request.method=='POST':
        newuser=userSignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Registered...")
            
            #Email Sending
            user=request.POST['firstname']
            sub='New User Registration'
            msg=f'Hello {user} !\n Welcome to NotesApp !\nWe are pleased to inform you that your account has been created successfully !\nFor further query , contact us on : +919106761736'
            from_email=settings.EMAIL_HOST_USER
            to_email=[request.POST['email']]

            send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)

            messages.info(request,'Registered successfully...')
                
            #OTP SMS Sending Code
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"

            querystring = {"authorization":"J1F6NWgRwOxC1Ar1Y8UIBvTDmy9KOzCv5L6hTPlGf9N5ppmUspy1npk6pkmM","variables_values":f"{otp}","route":"otp","numbers":"9106761736"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            (response.text)
            
            return redirect('/')
               
                
        else:
                print(newuser.errors)
                messages.error(request,'Please enter valid informations')
    
    return render(request,'register.html')

def userlogut(request):
    logout(request)
    return redirect('/')

def deletedata(request,id):
    uid=request.session.get('uid')
    cid=userSignup.objects.get(id=uid)
    userSignup.delete(cid)
    return redirect('/')