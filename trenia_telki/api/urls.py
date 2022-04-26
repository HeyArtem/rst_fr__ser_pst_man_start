from django.urls import path
from trenia_telki.api.views import(
    GirlsListView,
    GirlsDetailView,
    GirlsCreateView,
    GirlsDestroyView
)

urlpatterns = [
    path('', GirlsListView.as_view()),
    path('detail/<int:pk>/', GirlsDetailView.as_view()), # для аутентифицированного пользователя
    path('create/', GirlsCreateView.as_view()),
    path('destroy/<int:pk>/', GirlsDestroyView.as_view()),
]
