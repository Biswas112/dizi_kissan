<<<<<<< HEAD
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerce.urls'))
]
=======
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('ecommerce.urls'))
]
>>>>>>> 235f43ea45fb7904dfdbcdba5ee43e48947246b1
