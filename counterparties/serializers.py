from rest_framework import serializers
from .models import Contractor, ContractorType


class ContractorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorType
        fields = ('name',)


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = (
            'name',
            'boss_first_name',
            'boss_second_name',
            'boss_last_name',
            'phone',
            'inn',
            'ogrn',
            'okpo',
            'okato',
            'address',
            'bank',
            'account',
            'type',
            'bik',
        )






"""
name = serializers.CharField(max_length=100)
    boss_first_name = serializers.CharField(max_length=40)  # Имя
    boss_second_name = serializers.CharField(max_length=40)  # Отчество
    boss_last_name = serializers.CharField(max_length=40)  # Фамилия
    
    phone = serializers.CharField(max_length=10)
    inn = serializers.CharField(max_length=12)  # ИНН
    ogrn = serializers.CharField(max_length=15)  # ОГРН
    okpo = serializers.CharField(max_length=9)  # ОКПО
    okato = serializers.CharField(max_length=11)  # ОКАТО
    address = serializers.CharField(max_length=100)
    bank = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    account = serializers.CharField(max_length=20)  # счет
    type = serializers.StringRelatedField(many=False)
    bik = serializers.CharField(max_length=9)  # БИК атрибут банков

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

"""

