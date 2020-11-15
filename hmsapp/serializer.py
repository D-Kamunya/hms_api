from rest_framework import  serializers
from .models import Case,Appointment
from users.models import CustomUser as User
from django.db.models import fields




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name','role', 'email')   

class CaseListSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True, many=False)
    doctor = UserSerializer(read_only=True, many=False)
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
    patient = UserSerializer(read_only=True, many=False)
    doctor = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Appointment
        fields = '__all__'      
        


