import requests 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
import requests  # 👈 Add this line

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'items/add_item.html', {'form': form})

# 🆕 New view to fetch data from Flask


def get_flask_message(request):
    try:
        response = requests.get('http://flask:5000')  # "flask" is the Docker service name
        message = response.text
    except requests.exceptions.RequestException as e:
        message = f"Error contacting Flask service: {e}"

    return render(request, 'items/flask_message.html', {'message': message})


def home(request):
    return HttpResponse("Hello from Django!")
