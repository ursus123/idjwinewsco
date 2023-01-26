# Every time you create a view you have to go to the urls.py to add its urls
# These are necessay libraries that needs to be imported
from django.shortcuts import render

# Creating Views for Our Models you have to import all the models first
from .models import Name, People, Contact, Container, Address

#

def home_page(request):
    names = Name.objects.all
    people = People.objects.all
    contacts = Contact.objects.all
    context = {'Names':names,
               'People':people,
               'Contacts':contacts}
    return render(request, "home.html", context=context)

