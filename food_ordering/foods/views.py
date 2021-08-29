from django.shortcuts import render, redirect
from .forms import CategoryForm, FoodForm
from django.contrib import messages
from .models import Category, Food
from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os

def homepage(request):
    return render(request, 'foods/homepage.html')


@login_required
@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category added successfully')
            return redirect("/foods/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add category')
            return render(request, 'foods/category_form.html', {'form_category':form})
    context ={
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'foods/category_form.html', context)

@login_required
@admin_only
def get_category(request):
    categories =  Category.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_category':'active'
    }
    return render(request, 'foods/get_category.html', context)


@login_required
@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted Successfully')
    return redirect('/foods/get_category')



@login_required
@admin_only
def category_update_form(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Category updated successfully')
            return redirect("/foods/get_category")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update category')
            return render(request, 'foods/category_update_form.html', {'form_category':form})
    context ={
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'foods/category_update_form.html', context)

@login_required
@admin_only
def food_form(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Food added successfully')
            return redirect("/foods/get_food")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add food')
            return render(request, 'foods/food_form.html', {'form_food':form})
    context ={
        'form_food': FoodForm,
        'activate_food': 'active'
    }
    return render(request, 'foods/food_form.html', context)


@login_required
@admin_only
def get_food(request):
    foods =  Food.objects.all().order_by('-id')
    context = {
        'foods':foods,
        'activate_food':'active'
    }
    return render(request, 'foods/get_food.html', context)


@login_required
@admin_only
def delete_food(request, food_id):
    food = Food.objects.get(id=food_id)
    os.remove(food.food_image.path)
    food.delete()
    messages.add_message(request, messages.SUCCESS, 'Food Deleted Successfully')
    return redirect('/foods/get_food')


@login_required
@admin_only
def food_update_form(request, food_id):
    food = Food.objects.get(id=food_id)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Food updated successfully')
            return redirect("/foods/get_food")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update food')
            return render(request, 'foods/food_form.html', {'form_food':form})
    context ={
        'form_food': FoodForm(instance=food),
        'activate_food': 'active'
    }
    return render(request, 'foods/food_update_form.html', context)


def show_categories(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_category_user': 'active'
    }
    return render(request, 'foods/show_categories.html', context)


def show_foods(request):
    foods = Food.objects.all().order_by('-id')
    context = {
        'foods':foods,
        'activate_food_user': 'active'
    }
    return render(request, 'foods/show_foods.html', context)

