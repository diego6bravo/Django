from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.template import loader
from django.urls import reverse


def index(request): 
    return HttpResponse("Hello, que más. Vista del index de mi app.") 

def otrapagina(request): 
    return HttpResponse("Esto carga otra vista de la app.") 


######## Plantillas vista con HTML HttpResponse
def lemon(request): 
    template = loader.get_template('little_lemon/restaurante.html') 
    context={}  
    return HttpResponse(template.render(context, request)) 


###### Otra vista simple con render request
def little(request):  
    context={'name':'Algo que presentar'}  
    return render(request, 'little_lemon/restaurante.html', context) 


######### Lenguaje de plantilla DTL
def litlogueo(request): 
    context={'user':'dgarcia'} 
    return render(request, 'little_lemon/restaurante.html', context) 


##### Vista For
def vistafor(request): 
    langs = ['Python', 'Java', 'PHP', 'Ruby', 'Rust'] 
    return render(request, 'little_lemon/restaurante.html', {'langs':langs}) 


##### Ejemplo Vista tupla con HTML
def tabmenu(request):
    precios_productos = {'tabla_productos': [
        {'nombre':'pollo','precio':'2500'},
        {'nombre':'pescado', 'precio':'400'},
        {'nombre':'carne', 'precio':'10200'},
        {'nombre':'huevos', 'precio':'17300'},
    ]}
    return render(request, 'little_lemon/restaurante.html', precios_productos)


#### Vista extrayendo datos de la bd
from .models import MenuRest
def menubd(request):
    objetos = MenuRest.objects.all()
    diccionario = {'productos':objetos}
    return render(request, 'little_lemon/restaurante.html', diccionario)


####### Otra vista con HTML interno
def cobros(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 


######## http solicitudes
def home(request):
    path = request.path
    scheme = request.scheme
    address = request.META['REMOTE_ADDR']
    path_info = request.path_info

    msg = f"""<br>
    <br>Path: {path}
    <br>Scheme: {scheme}
    <br>address: {address}
    <br>Path Info: {path_info}
    """
    return HttpResponse(msg)


######### Formulario
def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# from django.contrib.auth.decorators import login_required ## Logueo requerido para esta vista
# @login_required ## Logueo requerido para esta vista
def showform(request): 
    return render(request, "form.html") 

def getform(request): 
    if request.method == "POST": 
        id=request.POST['id'] 
        name=request.POST['name'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id))


############ Ejercicio capturar info en URL
def menu(request, plato):
    items = {
        'pasta':'hecha de mierda',
        'pizza':'es la torre torcida',
        'sopa':'la que me tomé hoy, era de pesacado',
    }

    descripcion = items[plato]

    return HttpResponse(f"<h2> {plato} <h2>" + descripcion)


############ Ejercicio bebidas en URL
def drinks(request, drinks_name):
    drinks_tipos = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice = drinks_tipos[drinks_name]

    return HttpResponse(f"<h2> {drinks_name} <h2>" + choice)
    

######## Redirigir
def myview(request): 
    return HttpResponsePermanentRedirect(reverse('newapp:index'))


######## Manejo de errores
def my_error(request):
    condition = True
    if condition==True: 
        return HttpResponseNotFound('<h1>Página no encontrada</h1>') 
    else: 
        return HttpResponse('<h1>Página encontrada ahora</h1>')
    

######## Denegar permiso a usuario anónimo de vista
# from django.core.exceptions import PermissionDenied ######## Denegar permiso anónimo a vista  
def content(request):
    # if request.user.is_anonymous(): 
    #     raise PermissionDenied() 
    content = '<h1>Contenido WEB</h1>'
    return HttpResponse(content)


####### Formularios
from .forms import LogForm  # Importar formulario
from django.shortcuts import redirect

def formul(request):
    # form = LogForm() # Si es GET vuleve a crear una instancia vacía del formulario
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            # nombre = form.cleaned_data['nombre']
            return redirect ('formul')
    else:
        form = LogForm()  # Si es GET, mostrar formulario vacío
        # return HttpResponse('Paila, hay algo mal mijo arregle esa mierda')

    return render(request, 'formulario.html', {'form_dicc': form})


### Denegar permiso acceso a menos que loguee
def testpermission(user): 
    if user.is_authenticated() and user.has_perm("myapp.change_category"): 
        return True 
    else: 
        return False 
from django.contrib.auth.decorators import user_passes_test 
@user_passes_test(testpermission) 
def change(request): 
    return HttpResponse('Hola cambio vista')



### Listas con Detalle id Plantilla Figma
from .models import Empleado

def home_figma(request):
    return render(request, 'Figma/figma.html')

def list_detalle(request):
    listdetalle = {'empleados':Empleado.objects.all()}
    return render(request, 'Figma/figma.html', listdetalle)

def mostrar_list_detalle(request, id):
    if id:
        listdetalle = Empleado.objects.get(id=id)
    else:
        listdetalle = ''
    return render(request, 'Figma/listado_detalle.html', {'listado_dicc':listdetalle})



## Vistas basadas en clases (Genéricas)

# Vista de Plantilla
# Sólo plantillas planas sin interacción con la BD
from django.views.generic.base import TemplateView 
class Figma(TemplateView):
    template_name = 'Figma/figma.html'

# Listas
from django.views.generic.list import ListView
class ListaEmpleados(ListView):
    model = Empleado
    template_name = 'Figma/figma.html'
    # context_object_name = 'empleados'  # Cambiar 'object_list' por 'empleados'

# Crear
from django.views.generic.edit import CreateView
class CrearEmpleados(CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'Figma/figma.html'
    success_url = '/myapp/figma_view/'

# Detalle
# No se puede iterar, muestra sólo un objeto
from django.views.generic.detail import DetailView
class DetalleEmpleados(DetailView):
    model = Empleado
    template_name = 'Figma/figma.html'
    context_object_name = 'detail_emp'

# Actualizar
from django.views.generic.edit import UpdateView 
class ActualizarEmpleados(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'Figma/figma.html'
    success_url = '/myapp/figma_view/'

# Borrar
from django.views.generic.edit import DeleteView 
class BorrarEmpleados(DeleteView):
    model = Empleado
    template_name = 'Figma/figma.html'
    success_url = '/myapp/figma_view/'





## Para aplicar permisos en una vista basada en clases,
## debe utilizar PermissionRequiredMixin y establecer el atributo allow_required
## de la clase de vista en el permiso que desea aplicar.
# from django.contrib.auth.mixins import PermissionRequiredMixin 
# from django.views.generic import ListView 

# from .models import Product 

# class ProductListView(PermissionRequiredMixin, ListView): 
#     permission_required = "myapp.view_product" 
#     template_name = "product.html" 
#     model = Product


## Bloqueo de permisos mediante URL
# from django.conf.urls import url 
# from django.contrib.auth.decorators import login_required, permission_required 

# urlpatterns = [ 
#     url(r'^users_only/', login_required(myview)), 

#     url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview)), 
# ] 
