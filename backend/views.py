from django.shortcuts import render
from app.models import Contact

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        
        return render(request, 'index.html',{'msg':'Data saved successfully'})
    return render(request, 'index.html')

def admission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone
        )
        return render(request,"admission.html",{'msg':'Data saved successfully'})
    return render(request,"admission.html")    
