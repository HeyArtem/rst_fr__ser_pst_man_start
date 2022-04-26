from .serializers import(
    HairColorSerializer,
    GirlsListSerializer,
    GirlsDetailSerializer
)
from trenia_telki.models import(
    Girls,
    HairColor
)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


#вывод всех постов
class GirlsListView(generics.ListAPIView):
    queryset = Girls.objects.all()
    serializer_class = GirlsListSerializer
    
    
# детальный вывод поста
class GirlsDetailView(generics.RetrieveAPIView):
    queryset = Girls.objects.all()    
    serializer_class = GirlsDetailSerializer
    permission_classes = (IsAuthenticated, )
    
    # # этот сериалайзер тоже подходит
    # serializer_class = GirlsListSerializer
    
    
# создание поста
class GirlsCreateView(generics.CreateAPIView):
    queryset = Girls.objects.all()
    serializer_class = GirlsDetailSerializer
    

# удаление поста
class GirlsDestroyView(generics.DestroyAPIView):
    queryset = Girls.objects.all()
    serializer_class = GirlsDetailSerializer
