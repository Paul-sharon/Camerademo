
from django.contrib import admin
from django.urls import path
from camapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.print),
    path('', views.print),
]
