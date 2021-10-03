"""CNAB Parser API serializers"""
from dateutil.rrule import rrule, HOURLY
from rest_framework import serializers
from api.models import CnabImport, Shop
from backend.models import ImportTemplate

class ListStoresSerializer(serializers.ModelSerializer):
    """List stores serializer"""

    class Meta:
        model = Shop
        fields = '__all__'


class CreateCnabImportSerializer(serializers.ModelSerializer):
    """"Create CNAB Import serializer"""

    id = serializers.IntegerField(read_only=True)

    template_id = serializers.PrimaryKeyRelatedField(
        source='template',
        queryset=ImportTemplate.objects.all(),
        write_only=True
    )

    execution_datetime = serializers.DateTimeField(
        write_only=True
    )

    recurrence_rule = serializers.CharField(
        read_only=True
    )

    class Meta:
        model = CnabImport
        fields = [
            'id',
            'template_id',
            'file',
            'execution_datetime',
            'recurrence_rule'
        ]

    def create(self, validated_data):
        run_date = validated_data.pop('execution_datetime')
        rrule_date = CnabImport.convert_time_start_to_utc_date(run_date)
        validated_data['recurrence_rule'] = str(
            rrule(
                freq=HOURLY,
                dtstart=rrule_date,
                until=None,
                count=1,
                interval=1
            )
        )
        return super().create(validated_data)
