from django.contrib import admin
from .models import MenuItem, Chef, Contact,Order,BlogPost
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(Chef)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(BlogPost)