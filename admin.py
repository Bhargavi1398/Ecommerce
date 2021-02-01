from django.contrib import admin
from testapp.models import Ecommerce,Conformation

# Register your models here.
class EcommerceAdmin(admin.ModelAdmin):
    list_display=['name','price','category','about','discounted_price','image']
class ConformationAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','phone_no','address','email','city','state','pincode','landmark']

admin.site.register(Ecommerce,EcommerceAdmin)
admin.site.register(Conformation,ConformationAdmin)
