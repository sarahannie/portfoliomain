from django.shortcuts import render, HttpResponse

# Create your views here.
def Homepage(request):
    return render(request, 'home/homepage.html')

def Contactpage(request):
    return render(request, 'contact/contactpage.html')

def Aboutpage(request):
    return render(request, 'about/aboutpage.html')

def Servicepage(request):
    return render(request, 'service/servicepage.html')

def Projectpage(request):
    return render(request, 'project/projectpage.html')
