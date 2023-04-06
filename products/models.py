from django.db import models


class Product(models.Model):
    image = models.ImageField(
        upload_to='products',
        verbose_name='Изображение'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    slug = models.SlugField()
    properties = models.OneToOneField(
        'Property',
        on_delete=models.PROTECT,
        null=True
    )


class Property(models.Model):
    materials = models.ForeignKey(
        'Material',
        on_delete=models.PROTECT,
        verbose_name='Материалы'
    )
    options = models.ForeignKey(
        'Option',
        on_delete=models.PROTECT,
        verbose_name='Опции'
    )
    base = models.ForeignKey(
        'Base',
        on_delete=models.PROTECT,
        verbose_name='База'
    )
    sizes = models.ForeignKey(
        'Size',
        on_delete=models.PROTECT,
        verbose_name='Размеры'
    )


class Material(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название материала'
    )
    slug = models.SlugField(
        unique=True
    )
    image = models.ImageField(
        upload_to='materils'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


class Option(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название опции'
    )
    image = models.ImageField(
        upload_to='options'
    )
    price = models.IntegerField()


class Base(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название базы'
    )
    image = models.ImageField(
        upload_to='base'
    )
    price = models.IntegerField()


class Size(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()
    percent_price = models.IntegerField()
