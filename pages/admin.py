from django.contrib import admin

# Register your models here.
from .models import complaint,location,witness
admin.site.register(complaint)
admin.site.register(location)
admin.site.register(witness)