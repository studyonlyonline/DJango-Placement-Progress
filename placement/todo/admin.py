from django.contrib import admin
from .models import Category, Question, Tags

# Register your models here.
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Tags)