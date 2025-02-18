from django.contrib import admin

from .models import Credentials, RemoteJob

# Register your models here.
admin.site.register(Credentials)
admin.site.register(RemoteJob)
