from django.contrib import admin

from .models import ChatRoom, Messages
# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(Messages)