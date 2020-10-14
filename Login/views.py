from django.shortcuts import render ,redirect ,HttpResponse
# Create your views here.
from .models import UserData ,ClgId
from .forms import RegistrationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login ,logout


def login(request) :
    context={
        'id':'20'
    }
    return render(request,"Login/login.html",context)

def registration(request):
        if request.method=="POST":
            print(request.body)
            if 'login' in request.POST:
                check_if_user = User.objects.filter(username=request.POST['username']).exists()
                check_if_password = User.objects.filter(password=request.POST['password']).exists()
                print(check_if_user)
                print(check_if_password)
                if check_if_user and check_if_password:
                    return render(request, "Login/instruction_page.html")
                else:
                    context = {
                      'error': 'True'
                    }
                    return render(request,'Login/login.html',context)

            elif 'signup' in request.POST:
                context = {
                    'id': '20'
                }
                return render(request, 'Login/registration.html', context)


def exams(request):
    context={
        'id':'20'
    }
    return render(request,'Login/exams.html',context)
def submit(request):
    context={
        'id':'20'
    }
    return render(request,'Login/submit.html',context)
def technical(request):
    context={
        'id':'20'
    }
    return render(request,'Login/technical.html',context)
def timer(request):
    context={
        'id' :'20'
    }
    return render(request,'Login/timer.html',context)

def logout(request):
    context ={
        'success':'user logout'
    }
    return render(request,'Login/login.html',context)

def PostForm(request):
    print("dadhahda")
    if request.method == 'POST':
        print("dhahdahda")
        print(request.body)
        form=RegistrationForm(request.POST)
        temp_model = UserData.objects.create(f_name=request.POST['f_name'] ,l_name=request.POST['l_name'] ,username=request.POST['username'],password=request.POST['password'],cn_password=request.POST['cn_password'],city=request.POST['city'] , phone_number=request.POST['phone_number'] ,prn_number=request.POST['prn_number'] ,gender=request.POST['gender'] ,clg_name=request.POST['clg_name'])
        temp_model.save()
        user_model = User.objects.create(username=request.POST['username'], password=request.POST['password'])
        user_model.save()
        clg_model = ClgId.objects.create(clg_name=request.POST['clg_name'])
        clg_model.save()
        if form.is_valid() :
            form.save()
            print(form)
            print(form)
            return render("data submitted successfully")
        else :
            return render(request,'Login/instruction.html',{'form':form})







