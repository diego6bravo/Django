# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BookingForm, AgregarMenu
from .models import Menu
# from django.utils.text import slugify # URL amigables


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


def menu(request):
    menu_data = {'menuItem':Menu.objects.all()}
    return render(request, 'menu.html', menu_data)


def agregar_menu(request):
    if request.method == 'POST': 
        form_agregar = AgregarMenu(request.POST) 
        if form_agregar.is_valid(): 
            form_agregar.save() 
            return redirect('menu') 
    else: 
        form_agregar = AgregarMenu() 
        return render(request, 'agregar_menu.html', {'form_agregar': form_agregar})
    

def menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk) if pk else None

    if request.method == 'POST':
        form_edit = AgregarMenu(request.POST, instance=menu_item)  # Cargar el formulario con los datos enviados
        if form_edit.is_valid():
            form_edit.save()
            return redirect('menu_item', pk=menu_item.pk)  # Redirigir tras guardar los cambios
    else:
        form_edit = AgregarMenu(instance=menu_item)  # Cargar formulario prellenado

    return render(request, 'menu_item.html', {
        'menu_item_dicc': menu_item,
        'edit_menu': form_edit,  # Pasar el formulario al contexto
    })



# def menu_item(request, pk=None):
#     if pk:
#         menu_item = Menu.objects.get(pk=pk)
#         # slugified_name = slugify(menu_item.nombre) # URL amigables
#     else:
#         menu_item = None

#     return render(request, 'menu_item.html', {'menu_item_dicc': menu_item})
#   # return render(request, 'menu_item.html', {'menu_item':menu_item,'slugified_name':slugified_name})