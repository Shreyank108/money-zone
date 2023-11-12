from django.contrib import admin
from .models import Package, Course, PackageTaken, Earning
# Register your models here.
admin.site.register(Package)
admin.site.register(Course)
admin.site.register(PackageTaken)
admin.site.register(Earning)
