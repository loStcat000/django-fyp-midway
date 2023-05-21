from django import forms
from .models import UserData, Food, Image, Weight
from django.forms.widgets import DateInput

class UserDataForm(forms.ModelForm):
    
    class Meta:
        model = UserData
        fields = ("gender", "age",  "birthday", "height", "weight", "activitylevel")

class FoodForm(forms.ModelForm):
    '''
    A ModelForm class for adding a new food item
    '''
    class Meta:
        model = Food
        fields = ['food_name', 'quantity', 'calories', 'fat', 'carbohydrates', 'protein', 'category']

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ImageForm(forms.ModelForm):
    '''
    A ModelForm class for adding an image to the food item
    '''
    class Meta:
        model = Image
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.visible_fields()[0].field.widget.attrs['class'] = 'form-control'


#Weight Form#
class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = ['weight', 'entry_date']
        widgets = {
            'entry_date': DateInput(attrs={'type': 'date'})
        }