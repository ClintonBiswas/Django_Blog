from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App_Login.forms import singupFrom, userprofilechange, Profilepic



def sign_up(request):
    form = singupFrom()
    register = False
    if request.method == 'POST':
        form = singupFrom(data=request.POST)
        if form.is_valid():
            form.save()
            register = True

    dict = {'form':form, 'register':register}
    return render(request, 'App_Login/signup.html', context = dict)


def login_page(request):
     form = AuthenticationForm()
     if request.method == 'POST':
         form = AuthenticationForm(data = request.POST)
         if form.is_valid():
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                 login(request, user)
                 return HttpResponseRedirect(reverse('index'))
     return  render(request, 'App_Login/login.html', context = {'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context = {})

@login_required
def user_change(request):
    curent_user = request.user
    form = userprofilechange(instance = curent_user)
    if request.method == 'POST':
        form = userprofilechange(request.POST, instance= curent_user)
        if form.is_valid():
            form.save()
            form = userprofilechange(instance = curent_user)
    return render(request,'App_Login/change_profile.html', context={'form':form})


@login_required
def pass_change(request):
    curent_user = request.user
    changed = False
    form = PasswordChangeForm(curent_user)
    if request.method == 'POST':
        form = PasswordChangeForm(curent_user, data = request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request,'App_Login/change_pass.html', context = {'form':form, 'changed':changed})

@login_required
def add_pro_pic(request):
    form = Profilepic()
    if request.method == 'POST':
        form = Profilepic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit = False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_profilepic.html', context = {'form':form})
@login_required
def change_profile_pic(request):
    form = Profilepic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = Profilepic(request.POST,request.FILES, instance = request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request,'App_Login/add_profilepic.html', context = {'form':form})
