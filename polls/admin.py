from django.contrib import admin

# Register your models here.
from .models import Candidate, Rate, Details

admin.site.register(Candidate)
admin.site.register(Rate)
admin.site.register(Details)

