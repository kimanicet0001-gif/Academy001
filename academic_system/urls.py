from django.contrib import admin
from django.urls import path, include
from users.views import home   # OK maintenant

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name="home"),

    path('users/', include('users.urls')),
]