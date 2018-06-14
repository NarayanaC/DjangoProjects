from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from mysite.core.forms import SignUpForm
from django.http import HttpResponse
# from firstApp.models import 
# from firstApp.functions import handle_uploaded_file  
# from django.http import HttpResponseRedirect
# from firstApp.decorators import deco_log
# from django.template import RequestContext
# from django.views.generic import ListView, DetailView
# from django.template.loader import render_to_string
from django.core.mail import send_mail
from firstApp import models
from .models import Student_tab, auth_ext, employee, csv_files
from .forms import StudentForm, SignUpForm, authentication_form, ExtendedNew, File_uploading
from django.contrib import auth
from django.template.context_processors import csrf
import csv, sys, os
# from django.conf.settings import PROJECT_ROOT

# from settings import BASE


	

# Create your views here.
def home(request):
	#return HttpResponse('templates/index.html')
	return render(request,'firstApp/index.html')
	
# def header(request):
# 	return render(request,'firstApp/header.html')


def AboutUs(request):
	return render_to_response('firstApp/about_us.html')


@login_required
def ViewUsers(request):
	
	users = Student_tab.objects.all()
	return render(request,'firstApp/view_register.html',{'users':users})

def ViewExt(request):
	users = auth_user_extended.objects.all()
	return render(request,'firstApp/ext_view.html',{'users':users})



def RegisterNow(request):
	form = StudentForm(request.POST or None)

	if form.is_valid():
		form.save()
		users = Student_tab.objects.all()
		return render(request,'firstApp/view_register.html',{'users':users})
	
	return render(request,'firstApp/register.html',{'form':form})



def testgit(request):
	form = StudentForm(request.POST or None)

	if form.is_valid():
		form.save()
		users = Student_tab.objects.all()
		return render(request,'firstApp/view_register.html',{'users':users})
	
	return render(request,'firstApp/register.html',{'form':form})





# def csv_files(request):
# 	c = {}
#     c.update(csrf(request))
#     # form = authentication_form(request.POST)
#     return render(request, 'firstApp/register.html', c)


def CSV_files(request):
	form = File_uploading(request.POST, request.FILES)

	if form.is_valid():
		# handle_uploaded_file(request.FILES['file'])  
        # return HttpResponse("File uploaded successfuly")  

		form.save()
		return redirect("add_csv")
		
		return render(request,'firstApp/index.html')
	
	# return render(request,'firstApp/register.html',{'form':form})


def add_csv(request):
    cs_data = csv_files.objects.get(id=6)
    # for i in cs_data:
    file_ = open(os.path.join(PROJECT_ROOT, 'Book11.csv'))
        # data = csv.reader(open("static '/media/'i.file"), delimiter=",")
    for row in file_:
            if row[0] != 'name':
                post = employee()
                post.name = row[0]
                post.phone = row[1]
                post.address = row[2]
                post.role = row[3]
                post.save()

                return HttpResponse("File added successfuly")




def ExtendInfo(request):
	# form = Extend(request.POST or None)
	form = ExtendedNew(request.POST or None)

	if form.is_valid():
		form.save()
		# users = auth_user_extended.objects.all()
		users = auth_ext.objects.all()
		return render(request,'firstApp/ext_view.html',{'users':users})
	
	return render(request,'firstApp/add_ext.html',{'form':form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
       
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'firstApp/index.html')
    else:
        form = SignUpForm()
        # form2 = Extend()
    return render(request, 'firstApp/signup.html', {'form': form})


@login_required
def UpdateUser(request, id):
	user = Student_tab.objects.get(id=id) 
	form = StudentForm(request.POST or None, instance=user)

	if form.is_valid():
		form.save()
		users = Student_tab.objects.all()
		return render(request,'firstApp/view_register.html',{'users':users})
	
	return render(request,'firstApp/editregister.html',{'form':form, 'user':user})


@login_required
def DeleteteUser(request, id):
	user = Student_tab.objects.get(id=id)
	users = Student_tab.objects.all()

	user.delete()
	return render(request,'firstApp/view_register.html',{'user':user,'users':users })



def login(request):
    c = {}
    c.update(csrf(request))
    # form = authentication_form(request.POST)
    return render(request, 'firstApp/login.html', c)


# def auth_view(request):
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#     user = auth.authenticate(username=username, password=password)
#     details = auth_ext.objects.select_related('User')
#     with users.auth_ext.get(user.id == user) as addittive:
#         for i in addittive:
#             if user is not None and i.designation == manager:
#                 auth.login(request, user)
#                 return render(request, 'firstApp/index.html')
#             elif user is not None and i.designation == hr:
#                 auth.login(request, user)
#                 return render(request, 'firstApp/view_register.html')
#             else:
#                 return render(request, 'firstApp/about_us.html')

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    # return HttpResponse(user)
    detail = auth_ext.objects.get(user=user)
    # if user is False:
    # 	return HttpResponse('Incorrect Username or Password')
    if user is not None and detail.designation == 'manager':
        auth.login(request, user)
        request.session['id'] = user.id
        request.session['username'] = user.username
        request.session['email'] = user.email
        return render(request, 'firstApp/dashboard.html')
    elif user is not None and detail.designation == 'hr':
        auth.login(request, user)
        return render(request, 'firstApp/view_register.html')
    elif user is not None and detail.designation == 'employee':
        auth.login(request, user)
        return HttpResponse('Hey Employee Whats upp!!!')
        # return render(request, 'firstApp/view_register.html')
    else:
        return render(request, 'firstApp/about_us.html')






def logout(request):
        auth.logout(request)
        return render(request, 'firstApp/index.html') 



def delete_user_sessions(user):
    user.sessions.delete()


    # details = auth_ext.objects.all().select_related('user')
    # for i in details:
    	# return HttpResponse(i.designation)
    	# if i.designation == 'manager':
     #    	auth.login(request, user)
     #    	return render(request, 'firstApp/index.html')
    	# elif user is not None and i.designation == 'hr':
     #    	auth.login(request, user)
     #    	return render(request, 'firstApp/view_register.html')
    	# else:
     #    	return render(request, 'firstApp/about_us.html')
    	

    
        
    #     return render(request, 'firstApp/index.html')
    # elif user is not None and details.designation == hr:
    #     auth.login(request, user)
    #     return render(request, 'firstApp/view_register.html')
    # else:
    #     return render(request, 'firstApp/about_us.html')

            
    
   # if i.designation == 'manager':
    	# 	return render(request, 'firstApp/index.html')
    	# else:
    	# 	return HttpResponse(Error)     




# if user is not None and details.designation == manager:
    #     auth.login(request, user)
    #     return render(request, 'firstApp/index.html')
    # elif user is not None and details.designation == hr:
    #     auth.login(request, user)
    #     return render(request, 'firstApp/view_register.html')
    # else:
    #     return render(request, 'firstApp/about_us.html')



        # if user is not None and user.is_role == manager:
        #     auth.login(request, user)
        #     return render(request, 'firstApp/index.html')
        # elif user is not None and not user.is_superuser:
        #     auth.login(request, user)
        #     return render(request, 'firstApp/view_register.html')
        # else:
        #     return render(request, 'firstApp/about_us.html') 

       
# def auth_view(request):
#     form = authentication_form(request.POST or None)
#     if form.is_valid():
# 	    username = form.cleaned_data.get('username')
# 	    password = form.cleaned_data.get('password')
# 	    user = auth.authenticate(username=username, password=password)

# 	    if user is not None and user.is_active:
# 	        auth.login(request, user)
# 	        return render(request, 'firstApp/index.html')
# 	    else:
# 	        return render(request, 'firstApp/about_us.html')


    # def login(request):
    #     c = {}
    #     c.update(csrf(request))
    #     return render_to_response('login.html', c)
