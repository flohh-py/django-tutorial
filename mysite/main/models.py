from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

NAMING_TYPE = [
    ('default', 'Default'),
    ('in', 'In'),
    ('out', 'Out'),
]

class Main(models.Model):
    title = models.CharField(max_length=140)


class NamingSeries(models.Model):
    serie = models.CharField(max_length=10)
    type = models.CharField(choices=NAMING_TYPE, default='default', null=True, max_length=10)
    number = models.IntegerField(default=1)
    fill = models.IntegerField(default=4)

    @classmethod
    def get_series(cls, serie=None, type='default'):
        get_s = cls.objects.get_or_create(serie=serie, type=type)
        s = get_s[0]
        if get_s[1]:
            return str(serie) +' - ' + str(s.number).zfill(s.fill)
        else:
            s.number = int(s.number) + 1
            s.save()
            return str(serie) +' - ' + str(s.number).zfill(s.fill)


class MainAccontManager(BaseUserManager):
    def create_user(self, email, user_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_manager', True)
        other_fields.setdefault('is_active', True)
        
        return self.create_user(email, user_name, password, is_superuser=True, **other_fields)


class MainUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=50, unique=True)

    is_manager = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = MainAccontManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

