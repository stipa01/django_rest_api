from django.urls import path
from . import views

app_name = 'accidents'

# define the urls
urlpatterns = [
    path('diagnostics/', views.diagnostics, name='diagnostics'),
    path('diagnostics/<int:pk>/', views.diagnostic_detail, name='diagnostic-detail'),
]
