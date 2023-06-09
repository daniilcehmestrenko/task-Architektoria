# Generated by Django 3.1 on 2023-04-06 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название базы')),
                ('image', models.ImageField(upload_to='base')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название материала')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='materils')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название опции')),
                ('image', models.ImageField(upload_to='options')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('percent_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.base', verbose_name='База')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.material', verbose_name='Материалы')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.option', verbose_name='Опции')),
                ('sizes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.size', verbose_name='Размеры')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='Изображение')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('slug', models.SlugField()),
                ('properties', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.property')),
            ],
        ),
    ]
