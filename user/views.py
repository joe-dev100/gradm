from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from user.form import LoginForm, UserCreationForm
from vente.models import Session
from .models import  PasswordResetRequest, User
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role')  # Get role from the form (student, teacher, or admin)
        
        # Create the user
        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        
        # Assign the appropriate role
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True

        user.save()  # Save the user with the assigned role
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('home:admin_dashboard')  # Redirect to the index or home page
    return render(request, 'auth/register.html')  # Render signup template


def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        
        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, 'Reset link sent to your email.')
        else:
            messages.error(request, 'Email not found.')
    
    return render(request, 'auth/forgot-password.html')  # Render forgot password template


def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.filter(token=token).first()
    
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')

    if request.method == 'POST':
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.user.save()
        messages.success(request, 'Password reset successful')
        return redirect('login')

    return render(request, 'auth/reset_password.html', {'token': token})  # Render reset password template


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def user_add(request):
    users = User.objects.all().order_by('username')
    form = UserCreationForm()
    context = {
        'users': users,
        'page': 'users',
        'form': form,
    }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            notified=form.cleaned_data['notified']
            type = form.cleaned_data['user_type']
            user=User.objects.create(username=username,password=password,email=email,notified=notified,user_type=type)
            user.set_password(password)
            user.save()

            messages.success(request, " Utilisateur ajouté avec succès")
            return redirect('user:user_list')
        messages.error(request, form.errors)
        return redirect('user:user_list')
    return render(request, 'auth/user_list.html', context)


def login_view(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':

        form = LoginForm(request.POST)

        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        utilisateur=User.objects.get(username=request.POST.get('username'))
        if user is not None:
            login(request, user)
            if user.is_admin:
                return redirect('dashboard:home_page')
            else:
                session=Session.objects.get(login=utilisateur)
                if session.EstOuvert:
                    return redirect('dashboard:teller_page')
                messages.error(request, ("La session n'est pas ouverte !"))
        else:
            messages.error(request, ("Authentification echouée"))
    
             
    return render(
        request, 'auth/login.html', context={'form': form, 'message': message})

def user_list(request):
    users = User.objects.all()
    form = UserCreationForm()
    context = {
        'users': users,
        'page': 'users',
        'form': form,
    }
    return render(request, 'auth/user_list.html', context)

def user_update(request,pk):
    user = User.objects.get(pk=pk)
    form = UserCreationForm(request.POST or None, instance=user)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "modification éffectuée avec succès")
            return redirect('user:user_list')
        messages.error(request, "Modification échouée verifier les données entrées")
        return redirect('user:user_list')
    context = {
        'form': form,
    }

    return render(request, 'auth/partial/_user_modal.html', context)


def user_delete(request, pk):
    User.objects.get(pk=pk).delete()

    users = User.objects.all().order_by('username')
    context = {
        'users': users,
        'page': 'users'
    }

    return HttpResponseRedirect(reverse('user:user_list'))

