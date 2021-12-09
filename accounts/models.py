from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, identify_hasher
from django.contrib.auth.models import UserManager
from django.db.models import EmailField, CharField, BooleanField, DateTimeField


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None, fullname=None, is_staff=None, is_active=True, is_admin=None,
                    **extra_fields):
        """ Create and save a user with the given username, email, and password. """
        if not email:
            raise ValueError('The given email must be set.')
        if not password:
            raise ValueError('The given password must be set.')

        email = self.normalize_email(email)
        # username = self.model.normalize_username(username)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active

        user.save(using=self._db)
        return user

    # def create_user(self, username, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, password=None, name=None, **extra_fields):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=True)
        return user
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        #
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')
        #
        # return self._create_user(username, email, password, **extra_fields)

    def create_staffuser(self, email, password=None, name=None, **extra_fields):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=False)
        return user


class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=255)
    name = CharField(max_length=255, null=True, blank=True)
    fullname = CharField(max_length=255, blank=True, null=True)
    staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    admin = BooleanField(default=False)
    time_registration = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'  # параметр по которому будет происходить авторизация, аргументом передаем поле по которому будет происходить логин
    REQUIRED_FIELDS = []  # при регистрации нового пользователя(супера через консоль) можно задать какие поля будут обязатеельные для указания

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):  # в случае отсутствия имени меняем на другое значение
        if self.name:
            return self.name
        return self.email

    def get_full_name(self):
        if self.fullname:
            return self.fullname
        return self.email

    # права для входа в админку, эти ф-ции пишем если переопределяем стандартного пользователя

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        try:
            _alg = identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)
        # if not self.id and not self.staff and not self.admin:
        #     self.password = make_password(self.password) # make_passwodr - импортируемая, предназначенная сделать из текстового пароля захэшированый
        # print(self.password)
        # super(User, self).save(*args, **kwargs)

