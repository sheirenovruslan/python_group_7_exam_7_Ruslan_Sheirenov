from django.contrib import admin

from questionnare_app.models import Poll, Choice

# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)