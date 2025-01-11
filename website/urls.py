from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('work1/',views.work1,name='work1' ),
    path('fetch/',views.forfetch,name="fetch"),
    path('read/',views.read_canvas,name="read"),
]
