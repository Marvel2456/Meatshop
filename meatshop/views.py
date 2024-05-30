from django.shortcuts import render, redirect
from .models import Product, Contact
from django.contrib import messages

# Create your views here.

def homeView(request):
    product = Product.objects.all()
    return render(request, 'pages/home.html', {'product': product})

def aboutView(request):
    return render(request, 'pages/about.html')

def contactView(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']

        contact_us = Contact(name=name, email=email, phone_number=phone_number, message=message)

        contact_us.save()

        messages.success(request, 'Your request has been submitted thank you')
        return redirect('contact')
    return render(request, 'pages/contact.html')

def productView(request):
    product = Product.objects.all()
    return render(request, 'pages/products.html', {'product': product})