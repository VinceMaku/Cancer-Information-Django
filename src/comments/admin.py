from django.contrib import admin

# Register your models here.
from .models import (Comment, UserComment)


admin.site.register(Comment)
admin.site.register(UserComment)