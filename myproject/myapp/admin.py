from django.contrib import admin

### Registrar Modelos de BD
from .models import Menu
admin.site.register(Menu)

from .models import Referencias
admin.site.register(Referencias)

from .models import CategoriaMenu
admin.site.register(CategoriaMenu)

from .models import Logger
admin.site.register(Logger)


### Administrar usuarios, modificar permisos establecidos por otros más robustos
from django.contrib.auth.models import User 
admin.site.unregister(User) 

from django.contrib.auth.admin import UserAdmin 
@admin.register(User) 

class NewAdmin(UserAdmin): 
    readonly_fields = ['date_joined', 'last_login']

    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
    
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True
        return form


###### Trabajar permisos
from .models import Person 
# admin.site.register(Person) # Es mejor usar el decorador, esta opción es más larga

### Decorador que permite registrar al admin y ver en 2 columnas
@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", ) # Añade buscador por first_name


