from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages, auth
from ootdapp.models import Profile
from django.contrib.auth import authenticate, login

# Create your views here.


class Index(View):
    def get(self, request):
        return render(request, '')


def home(request):
    return render(request, 'index.html')


def product(request):
    return render(request, 'product.html')


# def login(request):
#     return render(request, 'login.html')


# def register(request):
#     return render(request, 'register.html')


def search(request):
    return render(request, 'search.html')


def signup(request):
    print('sign up')
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(request.POST)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist!')

                print("taken")
                return redirect('/signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken!')
                print("exist")
                return redirect('/signup/')
            else:
                user_model = User.objects.create_user(
                    first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user_model.save()

                # user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('/login/')
        else:
            messages.info(request, 'password do not match!')
            print("do not match")
            return redirect('/signup/')
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ('There was an error, please try again'))
            return redirect('/login/')
    return render(request, 'login.html')
