from django.db import models


class CategoriaMenu(models.Model):
    nombrecategoria = models.CharField(max_length=200)
# fk = CategoriaMenu.objects.get(pk=1) # Se hace en Shell


class Menu(models.Model):
    nombre = models.CharField(max_length = 100)
    ingredientes = models.CharField(max_length = 100)
    precio = models.IntegerField(null=True)
    categoria_id = models.ForeignKey(CategoriaMenu, on_delete=models.PROTECT, default=None) # Claves Foráneas
# d = Menu(nombre = 'Diego') # Instanciar para agregar fila a la BD, se hace en Shell 

    def __str__(self):
        return self.nombre + " : " + self.ingredientes

class Referencias(models.Model):
    plu = models.CharField(max_length = 100)
    codsap = models.CharField(max_length = 100)
    marca_vehiculo = models.CharField(max_length = 100)

class Llantas(models.Model):
    plu = models.CharField(max_length=100)
    codsap = models.CharField(max_length=100)
    marca_moto = models.CharField(max_length=100)

    class Meta:
        db_table = 'OINV'  # Nombre personalizado de la tabla

######### Ejemplo el usuario solo podrá seleccionar 1, 2, 3, 4, ese dato se llenará en la BD
SEMESTER_CHOICES = ( 
    ("1", "Civil"), 
    ("2", "Electrical"), 
    ("3", "Mechanical"), 
    ("4", "CompSci"), 
) 
 

class Student(models.Model): 
      semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = '1' 
        ) 


class College(models.Model): 
    CollegeID = models.IntegerField(primary_key = True) 
    name = models.CharField(max_length=50) 
    strength = models.IntegerField() 
    website=models.URLField() 

class Subject(models.Model): 
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 


#### Uno a uno
class Principal(models.Model): 
    CollegeID = models.OneToOneField( 
                College, 
                on_delete=models.CASCADE 
                ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 


class Teacher(models.Model): 
    TeacherID = models.IntegerField(primary_key=True) 
    subjectcode=models.ForeignKey( 
                Subject,  
                on_delete=models.CASCADE 
                  ) 
    Qualification = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50) 



############# Formularios
# from django import forms
# Clase que enviará los datos a la BD es la misma clase de forms.py (pero debo comentariarla y en su lugar usar la clase Meta)
# pero adecuado al modelo, también debo agregar a admin.py y registrar la clase Logger

# from django.utils import timezone

class Logger(models.Model):
     nombre = models.CharField(max_length=200)
     email = models.EmailField(max_length=200)
    # fecha = models.TimeField(help_text='Ponga una fecha válida', default=timezone.now)
     class Meta:
       permissions = [('can_edit_email', 'Can edit email')]

##### Trabajar permisos en admin
class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    ##### Muestra el contenido de la bd en forma concatenada en vez de simplemente el recuento
    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 
    


#### Vista extrayendo datos de la bd
class MenuRest(models.Model):
    producto = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)
    
    def __str__(self):
        return self.producto



######### Ejemplo de Testeo
from django.db import models

class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.first_name
    


#### Modelo para vistas basadas en clases
class Empleado(models.Model):   
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15)   
    class Meta:   
        db_table = "Empleado" 


    