from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from landing_page.validate import validate_password
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.db import IntegrityError, OperationalError
from landing_page.email import confirm_email
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


#imported models
from user_profile.models import Profile
from notification.models import Welcome_Notification, Notification
# Create your views here.


def signup(request):
    """ view to hadel signup"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        hashed_password = make_password(password)

        try:
            #create user account
            if validate_password(request, password, confirm_password):
                user = User.objects.create_user(username=email,
                                                email=email,
                                                password=password)

                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.save()

                #create user profile
                user_profile = Profile.objects.create(
                    user = user,
                    email = email,
                    first_name = user.first_name,
                    last_name = user.last_name,
                    is_verified = True,
                )
                user_profile.save()
                #confirm_email(request, email, user_profile.token)

                messages.success(request, "your account has been registered successfully check email for verification")
                return redirect('login')
        except IntegrityError:
            messages.warning(request, 'user already exits')
        
    if request.user.is_authenticated:
        return redirect('dash_board')
    return render(request, 'landing_page/signup.html')

def verify_account(request, auth_token):
    """for verification of account"""
    profile_obj = Profile.objects.filter(token=auth_token).first()
    profile_obj.is_verified = True
    profile_obj.save()
    messages.success(request, 'account verifed successfully. pleaae login')
    return redirect('login')

def resend_verification(request):
    """ resends verification if user dose not see it at first"""
    if request.method == 'POST':
        email = request.POST['email']
        try:
            profile_obj = Profile.objects.get(user__username=email)
            confirm_email(request, email, profile_obj.token)
            messages.success(request, 'confirmation email has been set')
        except Profile.DoesNotExist:
            messages.warning(request, 'sorry this email is not registerd. signup')
            return redirect('signup')
    return render(request, 'landing_page/verify_account.html')

def log_in(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                profile_obj = Profile.objects.get(user=user)
                if profile_obj.is_verified:
                    login(request, user)

                    if profile_obj.first_time_login:
                        for notification in Welcome_Notification.objects.all():
                            Notification.objects.create(
                                user=request.user,
                                title=notification.title,
                                message=notification.message
                            )
                    
                    profile_obj.first_time_login = False
                    profile_obj.save()
                    messages.success(request, 'Login successful')
                    return redirect(reverse('dash_board'))
                
                else:
                    messages.warning(request, 'Please verify your account to login')
                    return render(request, 'landing_page/verify_account.html')
            
            except Profile.DoesNotExist:
                messages.warning(request, 'User profile does not exist')
        
        else:
            messages.error(request, 'Username and/or password incorrect')
    
    return render(request, 'landing_page/sign_in.html')

def log_inDemoUser(request):
    username = 'favourokerri767@gmail.com'
    password = '123456789'
    user = authenticate(request, username=username, password=password)

    if user is not None:
        try:
            profile_obj = Profile.objects.get(user=user)
            if profile_obj.is_verified:
                login(request, user)

                if profile_obj.first_time_login:
                    for notification in Welcome_Notification.objects.all():
                        Notification.objects.create(
                            user=request.user,
                            title=notification.title,
                            message=notification.message
                        )
                    
                profile_obj.first_time_login = False
                profile_obj.save()
                messages.success(request, 'Login successful')
                return redirect(reverse('dash_board'))
                
            else:
                messages.warning(request, 'Please verify your account to login')
                return render(request, 'landing_page/verify_account.html')
            
        except Profile.DoesNotExist:
            messages.warning(request, 'User profile does not exist')
        
    else:
        messages.error(request, 'Username and/or password incorrect')
    
    return render(request, 'landing_page/sign_in.html')


def log_out(request):
    """ handel logout"""
    logout(request)
    messages.success(request, "logout successfull")
    return redirect('signup')
