# Generated by Django 2.2.1 on 2019-06-09 22:04

import auth_api.managers
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid',
                 models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UID пользователя')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Пользователь активен')),
                ('is_staff', models.BooleanField(blank=True, default=False, verbose_name='Статус админа')),
                ('is_superuser', models.BooleanField(blank=True, default=False, verbose_name='Статус супер-админа')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телефон')),
                ('email', models.CharField(max_length=128, unique=True, verbose_name='Почта')),
                ('join_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата первого входа')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('id',),
            },
            managers=[
                ('objects', auth_api.managers.UserManager()),
            ],
        ),
    ]
