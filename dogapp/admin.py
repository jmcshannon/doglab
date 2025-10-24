from django.contrib import admin
from .models import Dog, Breed
# Register your models here.

class DogAdmin(admin.ModelAdmin):
    pass

class BreedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)