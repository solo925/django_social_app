from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .forms import signUp,UserEditForm,ProfileEditForm
from .models import profile
from django.contrib import messages

@login_required
def edit(request):
    if request.method =='POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"profile updated successfully")
        else:
            messages.error(request,"error updating your")
    else:
            user_form =UserEditForm(instance=request.user)
            profile_form = ProfileEditForm(instance=request.user.profile)
            
    return render(request,'account/edit.html',{'user_form':user_form,'profile_form':profile_form})


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section':'dashboard'})


def user_login(request):
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data

			#if submitted data is valid you authenticate the user agains the database using the authenticate method and return the User object if the credentials are correct
			user = authenticate(request,
				username = cd['username'],
				password = cd['password'])

			#excecute if user have a value other than none
			if user is not None:
				if user.is_active:
					#if the user is active you you log the user into the website.you set the user in the session by using the login() method and return the 
					#Authenticated successfully message

					login(request,user)
					return HttpResponse('Authenticated'\
						'successfully')

				#execute if a user is not active
				else:
					return HttpResponse('Disabled account')

           #execute if a user have  a none value
			else:
				return HttpResponse('invalid login')

		#if the form is not valid return the original form/request is not POST
	else:
		form = LoginForm()
	return render(request,'account/login.html',{'form':form})

#user creation form in django.contruib.auth.forms
def register(request):
    if request.method =='POST':
        form =signUp(request.POST)
        if form.is_valid():
            form.save()
            person = request.user.username
            profile.objects.create(user = person)
            
            #after successfull registration redict the user to login page
            return render(request,'account/register_done.html')
        else:
            pass
            
    else:
            form = signUp()
    return render(request,'account/register.html',{'form':form})
