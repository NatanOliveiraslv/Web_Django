from django.contrib import admin
from clients.models import Client, ClientSocialnetwork
# Register your models here.

admin.site.register(Client)
admin.site.register(ClientSocialnetwork)