from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import next
from.forms import nextForm
from django.contrib.auth import authenticate, logout
def disp(request):
    return HttpResponse("obulamma")
def func1(request):
    return HttpResponse("haritha")
def index(request):
    data = next.objects.all()
    dict = {'empdata': data}
    return render(request, 'index.html', dict)
def create(request):
    if request.method=='POST':

        form=nextForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/index/')
    else:
            form=nextForm()
    return render(request,'create.html',{'form':form})
def edit(request,name):
     empdata=next.objects.get(name=name)
     form=nextForm(instance=empdata)
     return render(request,'update.html',{'form':form,'name':name})
def delete(request,name):
    empdata=next.objects.get(name=name)
    empdata.delete()
    return redirect('/index/')

def update(request,name):
    empdata=next.objects.get(name=name)
    form=nextForm(request.POST,instance=empdata)
    if form.is_valid():
        form.save()
        return redirect('/index/')
    return render(request,'update.html',{'form':form,'name':name})

def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('password')
        user=authenticate(username=uname,password=pwd)

        if user:
            return redirect('/index/')
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return redirect('/login/')
def home(request):
    return render(request,'home.html')




# Create your views here.
