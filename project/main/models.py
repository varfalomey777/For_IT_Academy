from typing import Any

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ForeignKey
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    car_brand = models.CharField(blank=True,null=True,max_length=20,verbose_name="Марка авто ")
    car_model = models.CharField(blank=True,null=True,max_length=20,verbose_name="Модель авто ")
    name_user = models.CharField(max_length=20,verbose_name="Ваше имя ")
    number_user = models.IntegerField(verbose_name="Контактный телефон ")
    cost = models.IntegerField(verbose_name="Стоимость авто ")
    year = models.IntegerField(verbose_name="Год выпуска ")
    content = models.TextField(verbose_name="Описание авто ")
    photo=models.ImageField(verbose_name="Фотография авто ",upload_to='all_photos/%Y/%m/%d/')
    city = models.CharField(max_length=20, verbose_name="Продажа в городе ")
    time_create=models.DateTimeField(auto_now_add=True)
    key=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    tag=models.ForeignKey("Tag",blank=True,null=True,on_delete=models.CASCADE)


    def __str__(self) -> Any:
        return f"{self.name}, {self.cost}, {self.year}, {self.content}, {self.photo}," \
               f" {self.city}, {self.time_create}, {self.name_user}, {self.number_user}"




class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="+"
    )
    name = models.CharField(blank=True, null=True, max_length=200)
    tel = models.IntegerField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self) -> Any:
        return f"{self.user}"

class Tag(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self) -> Any:
        return f"{self.name}"