from django.urls import path
from . import views

app_name = 'diagnostics'

# define the urls
urlpatterns = [
    path('', views.accidents, name='accidents'),
    # path('', views.AccidentView.as_view(), name='accidents'),
    path('<int:pk>/', views.accident_detail, name='accident-detail'),
]
