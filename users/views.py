from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('chagen-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            
            messages.success(request, f'Your account has been updated!')
            return redirect('chagen-home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        

    

    return render(request, 'users/profile.html', {'form': u_form})