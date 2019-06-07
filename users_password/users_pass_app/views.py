from django.shortcuts import render
from users_pass_app.forms import UserForm, UserProfileDataForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render (request, 'users_pass_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    regsitered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile = UserProfileDataForm(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile.save(commit =False)
            profile.user = user


            if 'profile_image' in request.FILES:
                profile.profile_image = request.FILES['profile_image']
            profile.save()
            registered =True

        else:
            print(user_form.errors, user_profile.errors)
    else:
        user_form = UserForm()
        user_profile = UserProfileDataForm()

    return render(request, 'users_pass_app/registration.html' ,{'UserForm': user_form , 'UserProfileData' :user_profile, 'registered':register })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user =authenticate(username =username ,password= password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')

        else:
            print('someone tried to login and failed')
            print("username: {} and password {}".format(username, password))
            return HttpResponse('invalid lgin details supplied')
    else:
        return render(request, 'users_pass_app/login.html', {})
