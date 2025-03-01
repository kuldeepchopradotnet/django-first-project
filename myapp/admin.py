from django.contrib import admin
from myapp.models import CustomUser  # ✅ Use absolute import
# Register your models here.


admin.site.register(CustomUser)