from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout         
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from .models import *

# Create your views here.
def home(request):
    user={'user':request.user}
    if request.user.is_authenticated:
        return render(request,'home.html',user)
    else:
        return redirect('user_login')



def sign_login(request):
    if request.method == 'POST':
        print("Received POST request")
        # For login
        if 'tutor' in request.POST:
            user = request.POST.get('username')
            print("Received POST request",user)

            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email_name = request.POST.get('email')
            pass1_name = request.POST.get('password1')
            pass2_name = request.POST.get('password2')
            # Add additional fields as needed
            print("Received POST request",user)


            # Create a new user (you need to define the User model or use your own logic)
            user = User.objects.create_user(username=user, first_name=first_name,last_name=last_name,email=email_name,password=pass1_name)
            print("Received POST request",user)
            group=Group.objects.get(name="Tutor")
            print("group-----------",group)
            user.groups.add(group)

            user = authenticate(request, username=user, password=pass1_name)
            print("Received POST request",user)

            if user is not None:
                print("Received POST request",user)

                login(request, user)
                return HttpResponse('success_page')  

        # For signup
        elif 'student' in request.POST:

            user = request.POST.get('username')
            print("Received POST request",user)

            first_name = request.POST.get('firstname')
            last_name = request.POST.get('lastname')
            email_name = request.POST.get('email')
            pass1_name = request.POST.get('password1')
            pass2_name = request.POST.get('password2')
            # Add additional fields as needed
            print("Received POST request",user)


            # Create a new user (you need to define the User model or use your own logic)
            user = User.objects.create_user(username=user, first_name=first_name,last_name=last_name,email=email_name,password=pass1_name)
            print("Received POST request",user)


            # Authenticate and login the new user
        
            print(user,"-------------------------")
            user = authenticate(request, username=user, password=pass1_name)
            print(user,"-------------------------")
            if user is not None:
                print(user,"-------------------------")
                login(request, user)
                # Add any additional logic after successful signup
                return HttpResponse('success_page')  # Redirect to a success page
    return render(request, 'sign_login.html')

def dashboard(request):
    if request.user.is_authenticated:
        courses=Course.objects.all()
        context={"courses":courses}
        return render(request,'dashboard.html',context)
    else:
        return redirect('user_login')

def user_login(request):
    if request.method=="POST":
        
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        user=authenticate(request,username=username ,password=password1)
        print(user,"-----------------------")
        if user is not None:
            login(request,user)
            return redirect('/dashboard/',{'message':'Logged In Successfully!'})
        else:
            return JsonResponse({'error':"Invalid Credentials"},status=400)
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect("home")


def detail(request,title):
    course = Course.objects.filter(title=title)
    context={"course":course}
    return render(request,'detail.html',context)