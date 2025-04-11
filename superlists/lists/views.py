from django.shortcuts import render, redirect

from .models import Item, List
# Create your views here.



def home_page(request):
    return render(request, 'home.html',)


def view_list(request, pk):
    'представление списка'
    list_ = List.objects.get(id=pk)

    return render(request, 'list.html', {'list': list_})
    

def new_list(requset):
    list_ = List.objects.create()
    Item.objects.create(text=requset.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(requset, pk):
    list_ = List.objects.get(id=pk)
    Item.objects.create(text=requset.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')