import email
from email import message
from unicodedata import name
from django.shortcuts import render,redirect
from note.forms import Contactform
from note.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def g_overview(request):
    return render(request,'g_overview.html')

def g_body(request):
    return render(request,'g_body.html')

def amenities(request):
    return render(request,'amenities.html')

def n_board(request):
    return render(request,'n_board.html')

def br_staff(request):
    return render(request,'br_staff.html')

def affiliation(request):
    return render(request,'aff.html')

def career(request):
    return render(request,'career.html')

def gallery(request):
    return render(request,'gallery.html')

def contact(request):
    cform=Contactform(request.POST or None)
    if cform.is_valid():
        cform.save()
        return redirect("home")
    return render(request,'contact.html',{'form':cform})
