from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from easydoc.validators import phone, alpha_all, login, email


# Класс менеджера должен переопределить методы create_user() и create_superuser().
class UserManager(BaseUserManager):
    def create_user(self, username, name, password=None, **kwargs):
        if not username:
            raise ValueError('имя логина обязательно')
        if not name:
            raise ValueError('имя пользователя обязательно')

        user = self.model(username=username)
        if kwargs.get('email'):
            user.email = kwargs.get('email')
        if kwargs.get('name'):
            user.name = kwargs.get('name')

        user.set_password(password)
        user.is_admin = False
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **kwargs):
        """
            Used for: python manage.py createsuperuser
        """
        user = self.create_user(username, password, **kwargs)
        user.name = 'admin'
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'

    # Имя логина авторизации
    username = models.CharField(verbose_name=u'логин для входа в систему', unique=True, max_length=30, db_index=True,
                                validators=[login])

    # Отображаемое имя пользователя
    pseudonym = models.CharField(verbose_name=u'псевдоним пользователя в системе', unique=True, max_length=30, db_index=True,
                            validators=[alpha_all])
    # Авторизация будет происходить по E-mail
    email = models.EmailField(verbose_name=u'электронная почта', unique=True, max_length=255, validators=[email])
    # Имя - не является обязательным
    first_name = models.CharField(verbose_name=u'имя пользователя', max_length=40, blank=True, null=True)
    # Фамилия - также не обязательна
    last_name = models.CharField(verbose_name=u'фамилия пользователя', max_length=40, blank=True, null=True)
    # слоган или статус - куда же без него. Наследство от соц. сетей
    tag_line = models.CharField(verbose_name=u'статус', max_length=140, blank=True, null=True)
    photo = models.ImageField(verbose_name=u'аватар', blank=True, null=True,
                              default='defaultprofileimage.jpg')
    phone = models.CharField(verbose_name=u'контактный телефон', max_length=12, validators=[phone], null=True)

    # Атрибут суперпользователя
    is_admin = models.BooleanField(default=False, null=False)

    # Сохраняем время создания и обновления аккаунта пользователя.
    # Устанавливая auto_now_add=True, мы говорим Джанго автоматически
    # ставить время при создании, причем далее поле будет нередактируемым.
    #  Аналогично и auto_now=True, разница в том, что поле каждый раз обновляется с обновлением объекта
    date_joined = models.DateTimeField(verbose_name=u'дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=u'последнее обновление', auto_now=True)
    # логинимся по email
    USERNAME_FIELD = 'username'
    # обязательное поле
    REQUIRED_FIELDS = ['pseudonym', 'email', ]

    objects = UserManager()

    def __unicode__(self):
        return '%d: %s' % (self.id, self.pseudonym)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True
