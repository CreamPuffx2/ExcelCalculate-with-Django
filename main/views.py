from django.shortcuts import render, redirect
from random import randint
from .models import User

# Create your views here.
def index(request):
    return render(request, "main/index.html")


def signup(request):
    return render(request, "main/signup.html")


def join(request):
    print(request)
    name = request.POST["signupName"]
    email = request.POST["signupEmail"]
    pw = request.POST["signupPW"]
    user = User(user_name=name, user_email=email, user_password=pw)
    user.save()

    code = randint(1000, 9999)
    response = redirect("main_verifyCode")
    response.set_cookie("code", code)
    response.set_cookie("user_id", user.id)

    # 이메일 발송 함수 호출

    return response


def signin(request):
    return render(request, "main/signin.html")


def verifyCode(request):
    return render(request, "main/verifyCode.html")


def verify(request):
    return redirect("main_index")


def result(request):
    return render(request, "main/result.html")
