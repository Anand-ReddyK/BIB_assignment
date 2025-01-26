from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import ChatRoom

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('user_login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'auth/login.html')


def home_view(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'pages/home.html', {'rooms': rooms})

def chat_room(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    messages = room.conversation.all()
    return render(request, 'pages/chat_room.html', {
        'messages': messages,
        "room": room
        })
