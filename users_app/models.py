from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from users_app.managers import MyAccountManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Имя пользователя', max_length=25, unique=True)
    email = models.EmailField(verbose_name='Email пользователя', max_length=40, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Дата последнего визита', auto_now=True)
    # временно выставил default=True, в дальнейшем, напишу код, который будет менять статус пользователю после подтверждения email
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # по дефолту имя пользователя=email, я изменил его на username
    USERNAME_FIELD = 'username'
    
    # поля обязательные для заполнения
    REQUIRED_FIELDS = ['email']
    
    # менеджер моделей, у него будет несколько функций
    objects = MyAccountManager()
    
    # магический метод для вывода в админке
    def __str__(self) -> str:
        return f"{self.username} - {self.email}"
    
    # переопределение метода delete, при удалении пользователя, 
    # инфрмация о нем будет со статусом is_activ = False, т.е. из базы не удалится
    def delete(self):
        self.is_active =False
        self.save()
