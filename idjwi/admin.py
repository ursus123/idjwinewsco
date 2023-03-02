from django.contrib import admin

#Importing models
from idjwi.models import Name, Address,Contact, People, Container, Item, TimeRange
admin.site.register([Name,Address, Contact, People, Container, Item, TimeRange])
