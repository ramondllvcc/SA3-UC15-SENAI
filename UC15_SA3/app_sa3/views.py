from django.shortcuts import render

def home(request):
    return render(request, 'html/home.html', {'image_path': 'img/img_home.jpg'})


def cadastro(request):
    return render(request, 'html/cadastro.html')

def login(request):
    return render(request, "html/login.html")