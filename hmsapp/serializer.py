from rest_framework import  serializers
from .models import Case,Appointment,Bill, Medication, Service
from users.models import CustomUser as User
from django.db.models import fields
from users.serializer import CustomUserSerializer 


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Medication
        fields='__all__' 

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields='__all__'
        

class CaseListSerializer(serializers.ModelSerializer):
    patient = CustomUserSerializer(read_only=True, many=False)
    doctor = CustomUserSerializer(read_only=True, many=False)
    medication = MedicationSerializer(read_only=True, many=False)
    service = ServiceSerializer(read_only=True, many=False)
    class Meta:
        model = Case
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'        
     
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
      model=Appointment
      fields='__all__'

class AppointmentListSerializer(serializers.ModelSerializer):
    patient = CustomUserSerializer(read_only=True, many=False)
    doctor = CustomUserSerializer(read_only=True, many=False)
    class Meta:
        model = Appointment
        fields = '__all__'      

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'  

class BillListSerializer(serializers.ModelSerializer):
    case = CaseListSerializer(read_only=True, many=False)
    class Meta:
        model = Bill
        fields = '__all__'                      




