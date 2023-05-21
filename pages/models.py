from django.db import models
from accounts.forms import User
from django.conf import settings
from django.utils import timezone

class UserData(models.Model):
    Gender_Choices =[
    ('Male', "Male"),
    ( 'Female', "Female")
    ]
    Activity_Choices =[
                  ('1' ,'Sedentary (little to no exercise + work a desk job) '),
                  ('2' ,'Lightly Active : (light exercise 1-3 days / week)' ),
                  ('3', 'Moderately Active : (moderate exercise 3-5 days / week)'),
                  ('4','Very Active : (heavy exercise 6-7 days / week)'),
                  ('5' ,'Extremely Active: (very heavy exercise, hard labor job, training 2x / day)')
                ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='DEFAULT VALUE')
    gender = models.CharField(choices = Gender_Choices, max_length=100)
    birthday = models.DateField()
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    activitylevel = models.CharField(choices = Activity_Choices, max_length=100)
    
    def __str__(self):
            return f'{self.user}'

    

class FoodCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Categories'

    def __str__(self):
        return f'{self.category_name}'

    @property
    def count_food_by_category(self):
        return Food.objects.filter(category=self).count()   

class Food(models.Model):
 
    food_name = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=100.00)
    calories = models.IntegerField(default=0)
    fat = models.DecimalField(max_digits=7, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_category')

    
    
    def __str__(self):
        return f'{self.food_name} - category: {self.category}'
        

class Image(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='get_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.image}'


class FoodLog(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_entry_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Food Log'
        verbose_name_plural = 'Food Log'

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.food_name} on {self.food_entry_date}'


class Weight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()

    class Meta:
        verbose_name = 'Weight'
        verbose_name_plural = 'Weight'

    def __str__(self):
        return f'{self.user.username} - {self.weight} kg on {self.entry_date}'