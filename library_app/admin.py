from django.contrib import admin

# Register your models here.

from .models import Book, Admin

admin.site.register(Book)
admin.site.register(Admin)
