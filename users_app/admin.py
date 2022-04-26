from pyexpat import model
from django.contrib import admin
from users_app.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
