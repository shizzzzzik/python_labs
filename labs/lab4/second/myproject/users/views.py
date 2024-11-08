from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json

# Створення нового користувача (POST)
@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'message': 'User created', 'user_id': user.id}, status=201)

# Отримання користувача за id (GET)
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'age': user.age
    })

# Оновлення користувача за id (PUT)
@csrf_exempt
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        user.username = data['username']
        user.email = data['email']
        user.age = data['age']
        user.save()
        return JsonResponse({'message': 'User updated'})

# Видалення користувача за id (DELETE)
@csrf_exempt
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted'})