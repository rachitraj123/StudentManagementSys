from django.shortcuts import render,redirect
from django.http import *
from .models import *
from django.contrib import messages
from django.db.models import Q
from .forms import CustomUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    Students = Student.objects.all()
    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            Student.objects.create(
                Name=name,
                Email = email,
            )
            messages.success(request,'Student added succesfully!!')
            return render(request, 'index.html',{
                'Students':Students,
            })
        elif 'update' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            updated_student = Student.objects.get(id=id)
            updated_student.Name = name
            updated_student.Email = email
            updated_student.save()
            
            messages.success(request,'Student Data Updated Successfully!!')
            return render(request, 'index.html',{
                'Students':Students,
            })
        elif 'del' in request.POST:
            id = request.POST.get('id')
            student = Student.objects.get(id=id)
            student.delete()
            messages.success(request,'Student Data Deleted Successfully!!')
            return render(request, 'index.html',{
                'Students':Students,
            })
        elif 'read' in request.POST:
            email = request.POST.get('data')
            if email.lower() == 'all':
                return render(request,'index.html',{
                    'Students':Students,
                })
            students = Student.objects.filter(Q(Email__icontains=email))
            return render(request,'index.html',{
                'Students':students,
            })
    else:
        return render(request, 'index.html',{
                'Students':Students,
            })



def Registerform(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentadd:login')
        else:
            return render(request,'registerform.html',{
                'form':form,
            })

    else:
        form = CustomUserForm()
    return render(request, 'registerform.html', {
        'form': form,
    })
        
def Login(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST.get('Username'),password = request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect('studentadd:index')
            messages.success('user logger in succesfully!!!')
        else:
            error_message = 'User not found!!'
            return render(request,'login.html',{
                'error':error_message,
            })
            
    else:
        return render(request,'login.html')
    
def Logout(request):
    logout(request)
    return redirect('studentadd:index')