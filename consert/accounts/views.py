from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from ticketsales.views import ConsertListView
from accounts.models import ProfileModel
from . forms import RegisterForm
from ticketsales import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . forms import ProfileEditForm,UserEditForm

def loginview(request):
    #POST method
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        #successful information
        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        #wrong information
        else:
            context = {
                'username':username,
                'errormessage':'User With This Profile Was Not Found'
            }
            return render(request,'accounts/login.html',context)
   #GET method
    else:
        return render(request,'accounts/login.html',{})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse(views.ConsertListView))
    
@login_required
def profileview(request):
    profile = request.user.profile
    context = {
        'profile':profile,
    }
    return render(request,'accounts/profile.html',context)

def registerview(request):
    if request.method == 'POST':
        profileregisterform = RegisterForm(request.POST,request.FILES)
        if profileregisterform.is_valid():
            user = User.objects.create_user(
            username = profileregisterform.cleaned_data['username'],
            email = profileregisterform.cleaned_data['email'],
            password = profileregisterform.cleaned_data['password'],
            first_name = profileregisterform.cleaned_data['first_name'],
            last_name = profileregisterform.cleaned_data['last_name'])
            user.save()
            profilemodel = ProfileModel(user = user,
            profileimage = profileregisterform.cleaned_data['profileimage'],
            gender = profileregisterform.cleaned_data['gender'],
            credit = profileregisterform.cleaned_data['credit'])
            profilemodel.save()
            return HttpResponseRedirect(reverse(loginview))
    else:
        profileregisterform = RegisterForm()


    context = {
        'formregister':profileregisterform
    }
    return render(request,'accounts/register.html',context)

def profileeditview(request):

    if request.method == 'POST':
        profileeditform = ProfileEditForm(request.POST,request.FILES,instance = request.user.profile)
        usereditform = UserEditForm(request.POST,instance = request.user)
        if profileeditform.is_valid() and usereditform.is_valid():
            profileeditform.save()
            usereditform.save()
            return HttpResponseRedirect(reverse(profileview))
            
    else:
        profileeditform = ProfileEditForm(instance = request.user.profile)
        usereditform = UserEditForm(instance = request.user)

    context = {
        'profileeditform':profileeditform,
        "usereditform":usereditform,
        "profileimage":request.user.profile.profileimage
    }

    return render(request,'accounts/profileedit.html',context)
