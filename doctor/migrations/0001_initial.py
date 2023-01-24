# Generated by Django 4.1.5 on 2023-01-23 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направлении',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=255, verbose_name='Отчество')),
                ('datetime', models.DateField(verbose_name='Год рождения')),
                ('experience', models.IntegerField(verbose_name='Стаж')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.direction', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'информация о докторе',
                'verbose_name_plural': 'информация о докторов',
            },
        ),
    ]