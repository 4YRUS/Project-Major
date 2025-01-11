from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import random
from django.http import JsonResponse, HttpResponse
from .imagereader import read_image
import base64
from .models import Customer, Product, Order, Tag, Images
from django.core.files.base import ContentFile

def read_canvas(path):
    text = read_image(path)
    print(text)
    return text

def home(request):
    text = "Hey Ssup??!! Draw or Write any thing, let me guess"
    image_url = ""
    if request.method == "POST":
        filename = 'uploaded_image.png'  
        image_data = base64.b64decode(request.POST['image'].split("base64,")[1])
        image_file = ContentFile(image_data, name=filename)
        uploaded_image = Images.objects.create(image=image_file)
        image_url = uploaded_image.image.url
        text = read_canvas("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\work\\" + image_url)
        print(text)

    return render(request, 'home.html', {'message': text, "url": image_url})

def work1(request):
    return render(request, 'work1.html', {})

def forfetch(request):
    if request.method == "GET":
        # image = Images.objects.all()[0].image.url
        return JsonResponse({"message": "hello world"})