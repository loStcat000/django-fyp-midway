from django.urls import path
from pages import views
from .views import FoodListView, FoodUpdateView , FoodDeleteView
from .views import user_list, user_toggle

urlpatterns = [
    path('', views.index, name='index'),

    

    path('food/list/admin', FoodListView.as_view(), name='food_list_admin'),
    path('food/list/admin/<int:pk>/update/', FoodUpdateView.as_view(), name='food_update_view'),
    path('food/list/admin/<int:pk>/delete/', FoodDeleteView.as_view(), name='food_delete_view'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/toggle/', user_toggle, name='user_toggle'),

    path('userdata/',views.User_Data, name="userdata"),
    path('profile/weight', views.weight_log_view, name='weight_log'),
    path('profile/weight/update/<int:weight_id>', views.weight_log_edit, name='weight_log_edit'),
    path('profile/weight/delete/<int:weight_id>', views.weight_log_delete, name='weight_log_delete'),
     path('search/', views.search, name='search'),

    path('food/list', views.food_list_view, name='food_list'),
    path('food/add', views.food_add_view, name='food_add'),
    path('food/foodlog', views.food_log_view, name='food_log'), 
    

    path('food/foodlog1', views.exercise, name='food_log1'),
    path('exerciseindex', views.post_api_data, name='exercise_index'),

    path('food/foodlog/delete/<int:food_id>', views.food_log_delete, name='food_log_delete'),
    path('food/<str:food_id>', views.food_details_view, name='food_details'),
    

    path('categories', views.categories_view, name='categories_view'),
    path('categories/<str:category_name>', views.category_details_view, name='category_details_view'),
]
