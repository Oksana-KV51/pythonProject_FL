from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        if 'login_username' in request.POST:
            # Обработка формы входа
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('catalog:product_list')
            else:
                # Обработка неудачной попытки входа
                return render(request, 'users/register.html', {'form': form, 'login_error': 'Неправильное имя пользователя или пароль'})
        else:
            # Обработка формы регистрации
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user_profile = form.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('catalog:product_list')
            else:
                print(form.errors)
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog:product_list')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль')
    return render(request, 'users/login.html')
