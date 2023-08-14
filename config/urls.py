
from django.contrib import admin
from django.urls import path
from myapp.views import fun, contact, hello,numbers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fun),
   path("contacts/", contact),
   path('hello/<str:first_name>/', hello),
   path('numbers/<int:num1>/<int:num2>', numbers)
]
#mysite.com/ =>index=>hello world