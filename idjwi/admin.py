from django.contrib import admin

#Importing models
from .models import Name, Address,Contact, People, Container, Item
admin.site.register([Name,Address, Contact, People, Container, Item])
