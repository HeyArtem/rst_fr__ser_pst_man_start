Создал простую модель девушки (без many to many), сериалайзеры (все посты, детальный просмотр, создание, удаление). В моделях использовал новые поля  (PositiveBigIntegerFiel, DecimalField), создал модель user (+superuser), так же использовал 'djoser', тестил все через postman.
$ mkdir REST_framework — создаем директорию
$ ls
перемещаемся в нее
$ python3 -m venv venv — djangorestfeameworkсоздали вирт окружение
$ source venv/bin/activate — активирую venv (только для установки пакетов)
$ pip install -U pip setuptools django pillow djangorestframework — устанавливаю необходимые библиотеки
$ code . - открываю 
активация venv
$ django-admin startproject app =создал прект app
$ cd app
$ ./manage.py startapp blog_app =создал приложение blog_app 

регистрируем приложением в settings
создаем модель в models.py
перед тем, как создать суперпользователя, делаю миграции
$ ./manage.py makemigrations
$ ./manage.py migrate

создаю суперпользователя (админа)
$ ./manage.py createsuperuser
запускаю сервер
$ ./manage.py runserver

регистрируем в admin.py(что бы появился в админке)
в папке своего приложения создаем api, фаил serializers.py, он будет сеарилизовать обьекты pythom в json
во views пишу представление
создаю urls.py
подключаем наш urls.py в главном urls (в urls проекта)
тестирую в браузере


# создание user
создаю новое приложение users_app
$ ./manage.py startapp users_app

регистрирую его в setings.py
in user_app/models
создаю модель пользователя наследуясь от AbstractBaseUser,, это нам даст возможность гибкой кастомизации пользователя в дальнейшем
create: users_app/managers.py
дописать импорт в users_app/models.py

в settings нужно указать модель, которую мы будем использаовать для юзер модели

# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users_app.User'


устанавливаем djoser , библитека будет нам давать работать с разными url-ми
(https://djoser.readthedocs.io/en/latest/index.html#):

$ pip install djoser


добавляю djoser и token в settings

теперь нужно прописать настройки рест_фрэймворка (в settings):
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
		# 'rest_framework.authentication.BasicAuthentication',
		# 'rest_framework_simplejwt.authentication.JWTAuthentication',
	),
}

в app/urls.py  подключаю обычные end-point-ы у joser-a
$ ./manage.py makemigrations
$ ./manage.py migrate (если у же был создан админ, до этого, то будет ошибка. Нужно удалить db.sqlite3, 0001_initial.py(файлы миграций из всех приложений!!) и после опять повторить обе команды: make & migrate)



регистрирую в админке (in users_app/admin.py)

#Django REST framework работа с postman

открываю postman и документацию с эндпоинтами
https://djoser.readthedocs.io/en/latest/base_endpoints.html

создаю пользователя:
в postman сoздаю новую вкладку:
	POST
	http://127.0.0.1:8000/api/auth/users/
	Body
	form-data
	username — user1
	email - user1@gmail.com
	password = user1USER1
		→Send

	создался пользователь


сгенерирую обычный токен:
https://djoser.readthedocs.io/en/latest/token_endpoints.html
в postman сoздаю новую вкладку:
	POST
	http://127.0.0.1:8000/api/auth/token/login/
	Body
	form-data
	username — user1
	email - user1@gmail.com
	password = user1USER1
		→Send
        
        
создаю несколько постов в админке, буду тестировать аутентификацию, поэтому на вьюхе на детльный просмотр у меня стоит
	# детальный вывод поста
	class GirlsDetailView(generics.RetrieveAPIView):
	queryset = Girls.objects.all() 
	serializer_class = GirlsDetailSerializer
	permission_classes = (IsAuthenticated, )


Нужно вписать token:
	GET
	http://127.0.0.1:8000/api/detail/1/
	headers
	Autorization - token f1249ee0d189bcc9ab13a29ab44391e71d4a1398
	
		→Send



что бы разлогинится:
в postman сoздаю новую вкладку:
	POST
	http://127.0.0.1:8000/api/auth/token/logout/
	headers
	Autorization — Token f1249ee0d189bcc9ab13a29ab44391e71d4a1398	
		→Send



кто я (токен получил новый, т. к. старый разлогигил):
	POST
	http://127.0.0.1:8000/api/auth/users/me/
	headers
	Autorization — token 8c3998e467dc35b89d69b7c95c2ab57ff661de42				
        →Send

