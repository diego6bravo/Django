# importar los settings del proyecto
import os
import django
# import sys

########## En Shell (Para agregar datos y tener en cuenta la clave foránea):

# Establecer la configuración del proyecto
# sys.path.append('c:/Users/USUARIO/Documents/IT/Python/django/myproject')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

## Luego importa los modelos
# from myapp.models import Llantas

# # Crear una nueva categoría
# categoria = Llantas(marca_moto='Pulsar')
# categoria.save()

#### Para actualizar (update)
# val = Menu.objects.get(id=1)
# val.descripcion='Comentarios que se actualizarán.'
# val.save()


# #### Llenar BD con lista Opción 1 #### 
# from myapp.models import Menu

# d = Menu(
#     nombre='Diego',
#     ingredientes='Carne, papas',
#     precio=15000,
#     categoria_id=categoria  # Asignamos la categoría obtenida
# )
# d.save()  # Guardamos el nuevo objeto en la base de datos


# #### Llenar BD con lista Opción 2 #### 
# from myapp.models import MenuRest

# val1 = MenuRest(producto='Papaya', precio='2500')
# val1.save()

# val2 = MenuRest(producto='Melón', precio='3200')
# val2.save()

# val3 = MenuRest(producto='Manzana', precio='200')
# val3.save()

# val4 = MenuRest(producto='Pera', precio='13700')
# val4.save()


from myapp.models import Empleado

val1 = Empleado(name='Diego Garcia', email='1@1.com', contact='34534543')
val1.save()

val2 = Empleado(name='Ines Bravo', email='2@2.com', contact='34543534')
val2.save()

val3 = Empleado(name='Pedro Garcia', email='3@3.com', contact='375432000345')
val3.save()

val4 = Empleado(name='Eliana', email='4@4.com', contact='67867867')
val4.save()