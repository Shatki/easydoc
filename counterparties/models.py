from django.db import models
from easydoc.validators import numeric, phone, email
from .constants import PERSON, COMPANY, BANK, GOV_BANK, GOV_COMPANY
from users.models import User


class Bank(models.Model):
    class Meta:
        verbose_name = 'банк'
        verbose_name_plural = 'банки'
        db_table = 'banks'

    name = models.CharField(verbose_name=u'наименование компании', max_length=50)
    full_name = models.CharField(verbose_name=u'полное наименование компании', max_length=100)
    # контакты
    address = models.CharField(verbose_name=u'адрес банка', max_length=100, null=True, blank=True)
    post_address = models.CharField(verbose_name=u'почтовый адрес банка', max_length=100, null=True, blank=True)
    email = models.CharField(verbose_name=u'e-mail банка', max_length=50, null=True, blank=True, validators=[email])
    site = models.CharField(verbose_name=u'сайт банка', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name=u'контактный телефон', max_length=15, validators=[phone],
                             null=True, blank=True)
    # реквизиты
    account = models.CharField(verbose_name=u'банковский счёт', max_length=20,
                               validators=[numeric], null=True, blank=True)  # счет
    bik = models.CharField(verbose_name=u'БИК', unique=True, max_length=9, db_index=True,
                           validators=[numeric], blank=True, null=True)  # БИК атрибут банков
    kpp = models.CharField(verbose_name=u'КПП', max_length=9, validators=[numeric],
                           null=True, blank=True)  # ИНН
    inn = models.CharField(verbose_name=u'ИНН', unique=True, max_length=12, validators=[numeric],
                           null=True, blank=True)  # ИНН
    ogrn = models.CharField(verbose_name=u'ОГРН', unique=True, max_length=15, validators=[numeric],
                            null=True, blank=True)  # ОГРН
    # коды
    okpo = models.CharField(verbose_name=u'ОКПО', max_length=9, validators=[numeric], null=True, blank=True)  # ОКПО
    okato = models.CharField(verbose_name=u'ОКАТО', max_length=11, validators=[numeric], null=True, blank=True)  # ОКАТО

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


# Create your models here.
class CounterpartType(models.Model):
    class Meta:
        verbose_name = 'вид контрагента'
        verbose_name_plural = 'виды контрагентов'
        db_table = 'counterpart_type'

    COUNTERPART_CHOICES = (
        (PERSON, 'Физическое лицо'),
        (COMPANY, 'Коммерческая организация'),
        (BANK, 'Банк'),
        (GOV_BANK, 'Центральный банк'),
        (GOV_COMPANY, 'Государственная учреждение'),
    )

    name = models.CharField(verbose_name=u'вид контрагента', unique=True, default=PERSON,
                            max_length=100, blank=False, choices=COUNTERPART_CHOICES)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Counterpart(models.Model):
    # Контрагент
    # Наименование компании - не обязательна для физ лиц
    class Meta:
        verbose_name = 'контрагент'
        verbose_name_plural = 'контрагенты'
        db_table = 'counterparties'
        # ordering = ('name',)

    name = models.CharField(verbose_name=u'наименование компании', max_length=100)
    full_name = models.CharField(verbose_name=u'полное наименование компании', max_length=100)
    # контакты
    address = models.CharField(verbose_name=u'юридический адрес', max_length=100, null=True, blank=True)
    post_address = models.CharField(verbose_name=u'почтовый адрес', max_length=100, null=True, blank=True)
    email = models.CharField(verbose_name=u'e-mail', max_length=50, null=True, blank=True, validators=[email])
    site = models.CharField(verbose_name=u'сайт', max_length=50, null=True, blank=True)
    phone = models.CharField(verbose_name=u'контактный телефон', max_length=15, validators=[phone],
                             null=True, blank=True)
    boss_first_name = models.CharField(verbose_name=u'имя руководителя', max_length=40, blank=True, null=True)  # Имя
    boss_second_name = models.CharField(verbose_name=u'отчество руководителя', max_length=40, blank=True,
                                        null=True)  # Отчество
    boss_last_name = models.CharField(verbose_name=u'фамилия руководителя', max_length=40, blank=True,
                                      null=True)  # Фамилия
    # реквизиты
    account = models.CharField(verbose_name=u'банковский счёт', max_length=20,
                               validators=[numeric], null=True, blank=True)  # счет
    bik = models.CharField(verbose_name=u'БИК', unique=True, max_length=9, db_index=True,
                           validators=[numeric], blank=True, null=True)  # БИК атрибут банков
    kpp = models.CharField(verbose_name=u'КПП', max_length=9, validators=[numeric],
                           null=True, blank=True)  # ИНН
    inn = models.CharField(verbose_name=u'ИНН', unique=True, max_length=12, validators=[numeric],
                           null=True, blank=True)  # ИНН
    ogrn = models.CharField(verbose_name=u'ОГРН', unique=True, max_length=15, validators=[numeric],
                            null=True, blank=True)  # ОГРН
    # коды
    okpo = models.CharField(verbose_name=u'ОКПО', max_length=9, validators=[numeric], null=True, blank=True)  # ОКПО
    okato = models.CharField(verbose_name=u'ОКАТО', max_length=11, validators=[numeric], null=True, blank=True)  # ОКАТО
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name=u'банк', blank=True, null=True)
    # персонал
    employees = models.ManyToManyField(User, verbose_name=u'сотрудники', blank=True)

    def __unicode__(self):
        return '%d: %s' % (self.id, self.name)

    def __str__(self):
        return self.name

    def get_boss_full_name(self):
        return ' '.join([self.boss_first_name, self.boss_second_name, self.boss_last_name])

    def get_boss_short_name(self):
        return ' '.join([self.boss_first_name, self.boss_second_name])
