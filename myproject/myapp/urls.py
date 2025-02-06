from django.urls import path
from . import views
# from .views import save_message, home3
# from .views import home5_view, home6

# urlpatterns = [
#     path('', views.home, name='home'),  # Home page
#     path('home2/', views.home2, name='home2'),  # Form page
#     path('save-message/', save_message, name='save_message'),
#     path('home3/', home3, name='home3'),
#     path('home4/', views.home4, name='home4'),
#     path("home5/", views.home5_view, name="home5"),
#     path('home5-view/', home5_view, name='home5_view'),
#     path("home6/", home6, name="home6"),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('home2/', views.home2, name='home2'),
    path('save-message/', views.save_message, name='save_message'),
    path('home3/', views.home3, name='home3'),
    path('home4/', views.home4, name='home4'),
    path('home5/', views.home5_view, name='home5'),  # Ensure this line is correct
    path('home6/', views.home6, name='home6'),
]