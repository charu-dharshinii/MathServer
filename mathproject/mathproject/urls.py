from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofrightcylinder/',views.surf_area,name="surfaceareaofrightcylinder"),
    path('',views.surf_area,name="surfaceareaofrightcylinderroot")
]