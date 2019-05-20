from rest_framework import viewsets
from API.models import Employee
from API.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Customer
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
