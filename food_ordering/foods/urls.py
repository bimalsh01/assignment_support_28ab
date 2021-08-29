from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage),
    path('category_form', views.category_form),
    path('get_category', views.get_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.category_update_form),

    path('food_form', views.food_form),
    path('get_food', views.get_food),
    path('delete_food/<int:food_id>', views.delete_food),
    path('update_food/<int:food_id>', views.food_update_form),

    path('get_category_user', views.show_categories),
    path('get_food_user', views.show_foods),

]