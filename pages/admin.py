from django.contrib import admin
from .models import UserData, FoodCategory, Food, Image
# Register your models here.


admin.site.register(UserData),
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Image)