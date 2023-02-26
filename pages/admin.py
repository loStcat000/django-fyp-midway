from django.contrib import admin
from .models import UserData, FoodCategory, Food, Image, FoodLog, Weight
# Register your models here.


admin.site.register(UserData),
admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Image)
admin.site.register(FoodLog)
admin.site.register(Weight)