from rest_framework import serializers

from  rest.models import Dummy


WEEKDAY = [
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
]

MONTH = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
]

class DummySerializer(serializers.Serializer):

    class Meta:
        model = Dummy
        fields = [
            'id',
            'day',
            'pre_seeded',
            'weekday',
            'month',
            'year',
            'created_at',
            'updated_at',
        ]

    id = serializers.IntegerField(read_only=True)
    day = serializers.IntegerField(required=True)
    weekday = serializers.ChoiceField(choices=WEEKDAY, required=True)
    month = serializers.ChoiceField(choices=MONTH, required=True)
    year = serializers.IntegerField(required=True)
    pre_seeded = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True, format='%d-%m-%Y %H:%M:%s', required=False)
    updated_at = serializers.DateTimeField(read_only=True, format='%d-%m-%Y %H:%M:%s', required=False)

    def create(self, validated_data):
        return Dummy.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.day = validated_data.get('day', instance.day)
        instance.weekday = validated_data.get('weekday', instance.weekday)
        instance.month = validated_data.get('month', instance.month)
        instance.year = validated_data.get('year', instance.year)
        instance.save()

        return instance