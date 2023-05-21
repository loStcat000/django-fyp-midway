from django import forms

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import UserDataForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from datetime import datetime
from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Food, FoodCategory, Image, Weight, FoodLog
from .forms import FoodForm, ImageForm, WeightForm
from django.db.models import Q


class FoodListView(ListView):
    model = Food
    template_name =( 'food_list_admin.html')
    context_object_name = 'foods'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

class FoodDeleteView(DeleteView):
     model = Food
     success_url = reverse_lazy('food_list_admin')
     template_name = 'food_confirm_delete.html'


class FoodUpdateView(UpdateView):
    model = Food
    template_name =  'food_update.html'
    success_url = reverse_lazy('food_list_admin')
    form_class = FoodForm
    
def index(request):
    
    return render(request, 'index.html')


def search(request):
    

    
    query = request.GET.get('q')
    results = Food.objects.filter(
        Q(food_name__icontains=query) |
        Q(category__category_name__icontains=query)
    )

    for food in results:
        food.image = food.get_images.first()

    context = {'results': results, 'query': query}
    return render(request, 'search_results.html', context)

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
    paginator = Paginator(foods, 8)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'food_list.html', {
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


def food_add_view(request):
    if not request.user.is_superuser:
        return HttpResponse(status=403) 
    '''
    It allows the user to add a new food item
    '''
    ImageFormSet = forms.modelformset_factory(Image, form=ImageForm, extra=2)

    if request.method == 'POST':
        food_form = FoodForm(request.POST, request.FILES)
        image_form = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

        if food_form.is_valid() and image_form.is_valid():
            new_food = food_form.save(commit=False)
            new_food.save()

            for food_form in image_form.cleaned_data:
                if food_form:
                    image = food_form['image']

                    new_image = Image(food=new_food, image=image)
                    new_image.save()

            return render(request, 'food_add.html', {
                'categories': FoodCategory.objects.all(),
                'food_form': FoodForm(),
                'image_form': ImageFormSet(queryset=Image.objects.none()),
                'success': True
            })
        
        else:
            return render(request, 'food_add.html', {
                'categories': FoodCategory.objects.all(),
                'food_form': FoodForm(),
                'image_form': ImageFormSet(queryset=Image.objects.none()),
            })

    else:
        return render(request, 'food_add.html', {
            'categories': FoodCategory.objects.all(),
            'food_form': FoodForm(),
            'image_form': ImageFormSet(queryset=Image.objects.none()),
        })




@login_required
def food_log_view(request):
    '''
    It allows the user to select food items and 
    add them to their food log
    '''
    today = date.today()


    if request.method == 'POST':
        foods = Food.objects.all()
        
        # get the food item selected by the user
        food = request.POST['food_consumed']
        food_consumed = Food.objects.get(food_name=food)
        
        


         # get the currently logged in user
        user = request.user
        


        # add selected food to the food log
        food_log = FoodLog(user=user, food_consumed=food_consumed,  )
        food_log.save()

    else: # GET method
        foods = Food.objects.all()
        
    # get the food log of the logged in user
    user_food_log = FoodLog.objects.filter(user=request.user, food_entry_date__date = today)  

    

    return render(request, 'food_log.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'user_food_log': user_food_log

    })
@login_required
def food_log_delete(request, food_id):
    '''
    It allows the user to delete food items from their food log
    '''
    # get the food log of the logged in user
    food_consumed = FoodLog.objects.filter(id=food_id)

    if request.method == 'POST':
        food_consumed.delete()
        return redirect('food_log')
    
    return render(request, 'food_log_delete.html', {
        'categories': FoodCategory.objects.all()
    })


@login_required
def weight_log_view(request):
    '''
    It allows the user to record their weight
    '''
    if request.method == 'POST':

        # get the values from the form
        weight = request.POST['weight']
        entry_date = request.POST['date']

        # get the currently logged in user
        user = request.user

        # add the data to the weight log
        weight_log = Weight(user=user, weight=weight, entry_date=entry_date)
        weight_log.save()

    # get the weight log of the logged in user
    user_weight_log = Weight.objects.filter(user=request.user)
    
    return render(request, 'user_profile.html', {
        'categories': FoodCategory.objects.all(),
        'user_weight_log': user_weight_log
    })

def weight_log_edit(request, weight_id):
    '''
    It allows the user to edit a weight record in their weight log
    '''
    weight_recorded = get_object_or_404(Weight, id=weight_id, user=request.user)

    if request.method == 'POST':
        form = WeightForm(request.POST, instance=weight_recorded)
        if form.is_valid():
            form.save()
            return redirect('weight_log')
    else:
        form = WeightForm(instance=weight_recorded)

    return render(request, 'weight_log_edit.html', {
        'form': form,
        'weight_recorded': weight_recorded,
        'categories': FoodCategory.objects.all()
    })

@login_required
def weight_log_delete(request, weight_id):
    '''
    It allows the user to delete a weight record from their weight log
    '''
    # get the weight log of the logged in user
    weight_recorded = Weight.objects.filter(id=weight_id) 

    if request.method == 'POST':
        weight_recorded.delete()
        return redirect('weight_log')
    
    return render(request, 'weight_log_delete.html', {
        'categories': FoodCategory.objects.all()
    })


def categories_view(request):
    '''
    It renders a list of all food categories
    '''
    return render(request, 'categories.html', {
        'categories': FoodCategory.objects.all()
    })


def category_details_view(request, category_name):
    '''
    Clicking on the name of any category takes the user to a page that 
    displays all of the foods in that category
    Food items are paginated: 4 per page
    '''
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    category = FoodCategory.objects.get(category_name=category_name)
    foods = Food.objects.filter(category=category)

    for food in foods:
        food.image = food.get_images.first()

    # Show 4 food items per page
    page = request.GET.get('page', 1)
    paginator = Paginator(foods, 8)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'food_category.html', {
        'categories': FoodCategory.objects.all(),
        'foods': foods,
        'foods_count': foods.count(),
        'pages': pages,
        'title': category.category_name
    })

def exercise(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/caloriesburned?activity='
        api_request = requests.get (api_url + query, headers = {'X-Api-Key': 'rlF8lbgjxthP9CWP94NU2A==iXEYoB7UpOYtfT9Y'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e: 
            api = " oops! your requested exercise was not found."
            print (e)
        return render(request, 'food_log1.html',{
            'api':api
            })
    else:
        return render(request, 'food_log1.html',{'activity':'Enter a valid exercise'})
    

'''api for exercise index'''
def exerciseindex(request):
    import json
    import requests

    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle=biceps'
        response = requests.get (api_url , headers ={'X-Api_Key': 'kELJsTw/wyxwiijafbI+xA==HFqUpMC1PJqQSw5k'})
        try:
            api = json.loads(response.content)
            print(response.content)
        except Exception as e: 
            api = " oops! your requested exercise was not found."
            print (e)
        return render(request, 'exercise_index.html',{
            'api':api
            })
    else:
        return render(request, 'exercise_index.html',{'api':'Enter a valid exercise'})
    

'''exerciseindex'''
def post_api_data(request):
    import json
    import requests
    
   
    if request.method == 'POST':
        query = request.POST['query']
    # Define the URL of the API endpoint and the data to be sent
        url = 'https://api.api-ninjas.com/v1/exercises?muscle='

    # Make the POST request to the API
        response = requests.get(url +query , headers={'X-Api-Key': 'kELJsTw/wyxwiijafbI+xA==HFqUpMC1PJqQSw5k'})

    # Check if the request was successful
        try:
        # If successful, process the response content and render a template
            api = json.loads(response.content)
            print(response.content)
        except Exception as e: 
            api = " oops! your requested exercise was not found."
            print (e)
        return render(request, 'exercise_index.html',{'api':api})
    else:

        query = 'biceps'
            # Define the URL of the API endpoint and the data to be sent
        url = 'https://api.api-ninjas.com/v1/exercises?muscle='
                
            # Make the POST request to the API
        response = requests.get(url +query , headers={'X-Api-Key': 'kELJsTw/wyxwiijafbI+xA==HFqUpMC1PJqQSw5k'})

            # Check if the request was successful
        try:
                # If successful, process the response content and render a template
                    api = json.loads(response.content)
                    print(response.content)
        except Exception as e: 
                    api = " oops! your requested exercise was not found."
                    print (e)
        return render(request, 'exercise_index.html',{'api':api})
    

'''admin deactivate function'''

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'user_list.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_toggle(request, user_id):
    user = User.objects.get(id=user_id)
    status = request.POST.get('status')
    if status == '0':
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect('user_list')