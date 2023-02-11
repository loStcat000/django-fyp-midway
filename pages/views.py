from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserDataForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse

from .models import Food, FoodCategory, Image

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def User_Data(request):
        if request.method == "POST":
            form = UserDataForm(request.POST)
            if form.is_valid():
                form.save ()
                messages.success(request, "Registration successful." )
                return redirect('login')
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
        form = UserDataForm()
        return render (request=request, template_name="UserData.html", context={"user_data":form})

def food_list_view(request):
    '''
    It renders a page that displays all food items
    Food items are paginated: 4 per page
    '''
    foods = Food.objects.all()

    for food in foods:
        food.image = food.get_images.first()

    # Show 4 food items per page
    page = request.GET.get('page', 1)
    paginator = Paginator(foods, 4)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'pages': pages,
        'title': 'Food List'
    })


def food_details_view(request, food_id):
    '''
    It renders a page that displays the details of a selected food item
    '''
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    food = Food.objects.get(id=food_id)

    return render(request, 'food.html', {
        'categories': FoodCategory.objects.all(),
        'food': food,
        'images': food.get_images.all(),
    })