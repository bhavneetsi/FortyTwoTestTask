from django.contrib import admin
from .models import Contact, Request, ObjectLog
# Register your models here.
admin.site.register(Contact)
admin.site.register(Request)
admin.site.register(ObjectLog)
