from django.utils import timezone
from django.db import models


TABLE_CHOICES = (('people', 'People'), ('enterprise','Enterprise'), ('item', 'Item'), ('address', 'Address'))
GENDER_CHOICES = (('Male','Male'),('Female','Female'),('Other','Other'))


class Name (models.Model):
    current_date = timezone.now()

    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,blank=False, null=False)
    nick_name = models.CharField(max_length=50,null=True,blank=True)
    surname = models.CharField(max_length=50,null=True,blank=True)
    family_name = models.CharField(max_length=50,null=True,blank=True)
    abbreviation = models.CharField(max_length=50,null=True,blank=True)
    prefix = models.CharField(max_length=50,null=True,blank=True)
    suffix = models.CharField(max_length=50,null=True,blank=True)
    signature = models.ImageField(null=True,blank=True, unique=True)
    picture = models.ImageField(null=True,blank=True)
    to_table = models.CharField(choices=TABLE_CHOICES, max_length=50)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add = True)


  

class Address (models.Model):
    owner_id = models.ForeignKey(Name, on_delete=models.CASCADE, default=0)
    address_type = models.CharField(max_length= 50,null=True,blank=True)
    street_number = models.CharField(max_length= 50,null=True,blank=True)
    street_name = models.CharField(max_length= 50,null=True,blank=True)
    city = models.CharField(max_length= 50,null=True,blank=True)
    county = models.CharField(max_length= 50,null=True,blank=True)
    town = models.CharField(max_length= 50,null=True,blank=True)
    state = models.CharField(max_length= 50,null=True,blank=True)
    province = models.CharField(max_length= 50,null=True,blank=True)
    country = models.CharField(max_length= 50,null=True,blank=True)
    zip_code = models.IntegerField(null=True,blank=True)
    longitude = models.IntegerField(null=True,blank=True)
    latitude =  models.IntegerField(null=True,blank=True)



class Contact(models.Model):
    contact_from_table = models.CharField(choices=TABLE_CHOICES, max_length=50)
    contact_for = models.ForeignKey(Name, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length= 50,null=True,blank=True)
    phone_number = models.IntegerField(default= 0,null=True,blank=True)
    emergency_phone_number = models.IntegerField(default= 0,null=True,blank=True)
    bank_name = models.CharField(max_length= 50,null=True,blank=True)
    account_number = models.IntegerField(default= 0,null=True,blank=True)
    routing_number = models.IntegerField(default= 0,null=True,blank=True)
    bank_card_number =  models.IntegerField(default=0,null=True,blank=True)
    bank_card_expiration_date = models.DateField(null=True,blank=True)
    bank_card_secret_code = models.IntegerField(default=0,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    work_email = models.EmailField(null=True,blank=True)
    backup_email = models.EmailField(null=True,blank=True)
    emergency_email = models.EmailField(null=True,blank=True)

class People (models.Model):
    names_id = models.ForeignKey(Name, on_delete=models.CASCADE)
    contacts_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    addresses_id = models.ForeignKey(Address, on_delete=models.PROTECT)
    date_of_birth = models.DateField(null=True,blank=True)
    height = models.CharField(max_length= 50,null=True,blank=True)
    weight = models.CharField(max_length=50,null=True,blank=True)
    hair_color = models.CharField(max_length=50,null=True,blank=True)
    eye_color = models.CharField(max_length=50,null=True,blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=50,null=True,blank=True)
    hire_date = models.DateField(null=True,blank=True)
    salary = models.IntegerField(default=0, null=True,blank=True)

class Item (models.Model):
    date_of_birth = models.DateField()
    height = models.CharField(max_length= 50,null=True)
    weight = models.CharField(max_length=50,null=True)
    shape = models.CharField(max_length=50,null=True)
    length = models.CharField(max_length=50,null=True)
    width = models.CharField(max_length=50,null=True)
    color = models.CharField(max_length=50,null=True)
    received_date = models.DateField(null=True)


class Container (models.Model):
    carrier = models.CharField(max_length=50, default=0)
    amount = models.CharField(max_length= 50,null=True)
    unit_price = models.CharField(max_length= 50,null=True)
    currency = models.CharField(max_length=50,null=True)
    received_date = models.DateField(null=True)
    arrival_date = models.DateField(null=True)
