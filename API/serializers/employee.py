from rest_framework import serializers
from API.models import Employee, Attachment
from API.serializers.attachment import AttachmentSerializer

from dateutil.relativedelta import relativedelta
from datetime import datetime

now = datetime.now()


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для модели Employee
    """
    id = serializers.IntegerField(required=False)
    attachment = AttachmentSerializer(many=False)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        age = int(relativedelta(now, validated_data['date_of_birth']).years)
        attachment: dict = validated_data.pop('attachment', None)
        if attachment is not None:
            attachment: Attachment = Attachment.objects.create(**attachment)
        instance: Employee = Employee.objects.create(age=age, attachment=attachment, **validated_data)

        return instance
