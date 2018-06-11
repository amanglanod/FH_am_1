from django.contrib import admin

# Register your models here.
from .models import Candidate, Rate

admin.site.register(Candidate)
admin.site.register(Rate)

