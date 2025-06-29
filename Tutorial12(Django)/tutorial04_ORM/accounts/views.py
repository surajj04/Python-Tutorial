from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request, "error.html", {
                "error_msg": "Invalid credentials",
                "error_code": "401"
            })
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, "error.html", {
                    "error_msg": "User already exist!!!",
                    "error_code": "400"
                })
            elif User.objects.filter(email=email).exists():
                return render(request, "error.html", {
                    "error_msg": "Email already exist!!!",
                    "error_code": "400"
                })
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print('password not match...')
            return render(request, "error.html", {
                "error_msg": "Passwords do not match",
                "error_code": "400"
            })
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def error(request):
    return render(request, "error.html", {"error_msg": "Something went wrong", "error_code": "Oops!"})
