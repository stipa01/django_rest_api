from rest_framework import serializers
from . import models


class EvDiagnosticSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')

    class Meta:
        model = models.EvDiagnostic
        fields = ['id', 'vehicle_id', 'created_at', 'battery_charge', 'battery_health', 'battery_temperature',
                  'run_hours', 'distance_covered', 'speed', 'state', 'battery_voltage', 'battery_current',
                  'motor_speed', 'lat', 'lng']


class EngineDiagnosticSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')

    class Meta:
        model = models.EngineDiagnostic
        fields = ['id', 'vehicle_id', 'created_at', 'fuel_level', 'engine_rpm', 'engine_coolant_temp',
                  'run_hours', 'distance_covered', 'speed', 'state', 'battery_voltage', 'throttle_position',
                  'maf_flow_rate', 'engine_load', 'lat', 'lng', 'engine_power', 'barometric_pressure',
                  'air_intake_temp', 'fuel_type', 'engine_runtime', 'timing_advance', 'equiv_ratio']


class TroubleCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TroubleCode
        fields = ['id', 'vehicle_id', 'code', 'trouble_code_system', 'condition_description', 'alarm_on',
                  'notification_date', 'clearance_date']


class MaintenanceScheduleSerializer(serializers.HyperlinkedModelSerializer):
    vehicle_id = serializers.ReadOnlyField(source='vehicle.vehicle_id')
    service_center = serializers.ReadOnlyField(source='service_center.service_center_name')

    class Meta:
        model = models.MaintenanceSchedules
        fields = ['id', 'vehicle_id', 'description', 'service_center', 'status', 'date']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = ['vehicle_id', 'model', 'car_year', 'state', 'bus_type']


class ServiceCenterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ServiceCenters
        fields = ['service_center_name', 'description', 'location', 'lat', 'lng']
