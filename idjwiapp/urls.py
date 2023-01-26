from django.contrib import admin,flatpages
from django.urls import path

# You have to import views in order to create their urls
from idjwi.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page)
]
