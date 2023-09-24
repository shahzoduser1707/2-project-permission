from django.contrib import admin
from .models import PhoneModel
from config.forms import PhoneForm


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    form = PhoneForm
    list_display = ('name','user')
    search_fields = ('name')
    
admin.site.register(PhoneModel, )
 