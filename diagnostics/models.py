from django.db import models


# Create your models here.
class Vehicle(models.Model):
    vehicle_id = models.CharField(max_length=100, primary_key=True)
    model = models.CharField(max_length=100)
    car_year = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    bus_type = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_id


class EvDiagnostic(models.Model):
    # title
    vehicle = models.ForeignKey(Vehicle, related_name='ev_vehicle', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    battery_charge = models.FloatField(default=0)
    battery_health = models.CharField(max_length=50, default='Good')
    battery_temperature = models.FloatField(default=0)
    run_hours = models.FloatField(default=0)
    distance_covered = models.FloatField(default=0)
    speed = models.FloatField(default=0)
    state = models.CharField(max_length=20, default='Active')
    battery_voltage = models.FloatField(default=0)
    battery_current = models.FloatField(default=0)
    motor_speed = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return self.vehicle.vehicle_id


class EngineDiagnostic(models.Model):
    # title
    vehicle = models.ForeignKey(Vehicle, related_name='engine_vehicle', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    fuel_level = models.FloatField(default=0)
    engine_rpm = models.FloatField(default=0)
    engine_coolant_temp = models.FloatField(default=0)
    run_hours = models.FloatField(default=0)
    distance_covered = models.FloatField(default=0)
    speed = models.FloatField(default=0)
    state = models.CharField(max_length=20, default='Active')
    battery_voltage = models.FloatField(default=0)
    throttle_position = models.FloatField(default=0)
    maf_flow_rate = models.FloatField(default=0)
    engine_load = models.FloatField(default=0)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    engine_power = models.FloatField(default=0)
    barometric_pressure = models.FloatField(default=0)
    air_intake_temp = models.FloatField(default=0)
    fuel_type = models.CharField(max_length=100, default='Biodiesel_Ethanol')
    engine_runtime = models.CharField(max_length=20, default='0')
    timing_advance = models.FloatField(default=0)
    equiv_ratio = models.FloatField(default=0)

    def __str__(self):
        return self.vehicle.vehicle_id


class TroubleCode(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='trouble_code_vehicle', on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    trouble_code_system = models.CharField(max_length=100)
    condition_description = models.CharField(max_length=500)
    alarm_on = models.CharField(default='ON', max_length=20)
    notification_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    clearance_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.code


class ServiceCenters(models.Model):
    service_center_name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return self.service_center_name


class MaintenanceSchedules(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='related_vehicle', on_delete=models.CASCADE, null=True, blank=True)
    service_center = models.ForeignKey(ServiceCenters, related_name='related_service_center', on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=100)
    alarm = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.vehicle.vehicle_id
