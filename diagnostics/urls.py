from django.urls import path
from . import views

app_name = 'health'

# define the urls
urlpatterns = [
    path('diagnostics/', views.diagnostics, name='diagnostics'),
    path('diagnostics/<int:pk>/', views.diagnostic_detail, name='diagnostic-detail'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<str:pk>/', views.vehicle_detail, name='vehicle-detail'),
    path('trouble-codes/', views.trouble_codes, name='trouble-codes'),
    path('trouble-codes/<int:pk>/', views.trouble_code_detail, name='trouble-code-detail'),
    path('maintenance-schedules/', views.maintenance_schedules, name='maintenance-schedules'),
    path('maintenance-schedules/<int:pk>/', views.maintenance_schedule_detail, name='maintenance-schedules-detail'),
    path('service-centers/<str:pk>/', views.service_center_detail, name='service-centers-detail'),
    path('service-centers/', views.service_centers, name='service-centers'),
    path('ev-diagnostics/<int:pk>/', views.ev_diagnostic_detail, name='ev-diagnostics-detail'),
    path('ev-diagnostics/', views.ev_diagnostics, name='ev-diagnostics'),
    path('engine-diagnostics/<int:pk>/', views.engine_diagnostic_detail, name='engine-diagnostics-detail'),
    path('engine-diagnostics/', views.engine_diagnostics, name='engine-diagnostics'),
]
