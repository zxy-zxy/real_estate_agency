from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import truncatechars

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление', default=timezone.now, db_index=True
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира', max_length=50, db_index=True
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
    )
    address = models.TextField(
        'Адрес квартиры', help_text='ул. Подольских курсантов д.5 кв.4'
    )
    floor = models.CharField(
        'Этаж', max_length=3, help_text='Первый этаж, последний этаж, пятый этаж'
    )

    rooms_number = models.IntegerField('Количество комнат в квартире', db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров', null=True, blank=True, db_index=True
    )

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания', null=True, blank=True, db_index=True
    )

    new_building = models.NullBooleanField('Является ли новостройкой', null=True)

    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул')

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    def get_owners(self):
        return [owner for owner in self.owner_set.all()]


class Owner(models.Model):
    owner_initials = models.CharField('ФИО владельца', max_length=200)
    owner_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_phone_pure = PhoneNumberField(
        blank=True, verbose_name='Нормализованный номер владельца'
    )
    owner_flats = models.ManyToManyField(Flat, verbose_name='Квартиры в собственности')

    def __str__(self):
        return f'{self.owner_initials} {self.owner_phone_pure}'

    def __repr__(self):
        return self.__str__()


class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name='Кто жаловался',
        null=True,
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.SET_NULL,
        verbose_name='Квартира, на которую пожаловались',
        null=True,
    )
    text = models.TextField(verbose_name='Текст жалобы', blank=True, max_length=5000)

    @property
    def short_text(self):
        return truncatechars(self.text, 100)

    def __str__(self):
        return f'Report by {self.user} with content: {self.short_text}'

    def __repr__(self):
        return self.__str__()
