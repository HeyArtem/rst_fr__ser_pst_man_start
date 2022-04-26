from dataclasses import fields
from pyexpat import model
from trenia_telki.models import(
    Girls, 
    HairColor
)
from rest_framework import serializers


#сериализация цвета волос
class HairColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HairColor
        fields = '__all__'
        
        
#вывод всех постов
# так же его можно подключать к детальному выводу
class GirlsListSerializer(serializers.ModelSerializer):
    
    hair_color = HairColorSerializer()
    
    class Meta:
        model = Girls
        
        #вывожу все поля, но в своей последовательности
        fields = (
            'id',
            'name',
            'girls_description',
            'hair_color',
            'growth',
            'weight',
            'status',
            'update_list_date',
            'listing_date',
        )
        
        
#работа с отдельным постом (редактирование, просмотр, удаление)
# -так же я использую этот сериалайзер для создания поста
#  но когда я прописывал здесь "hair_color = HairColorSerializer()"
#  то выводилась ошибка, а впосте ""hair_color": null"
#  а без вписывания hair_color можно выбрать
# -так же я использую этот сериалайзер для удаления поста
class GirlsDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Girls
        fields = '__all__'
