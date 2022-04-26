from django.contrib import admin
from .models import Girls, HairColor


# отображение а админке моего сайта
@admin.register(Girls)
class GirlsAdmin(admin.ModelAdmin):
    search_fields = ['name'] #поиск по имени    
    list_filter = ['status', 'hair_color', 'weight', 'growth'] # фильтр справа
    
# отображение а админке раздел цвет волос
@admin.register(HairColor)
class GirlsAdmin(admin.ModelAdmin):
    model = HairColor
    
    


