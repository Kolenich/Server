# Generated by Django 2.2.1 on 2019-05-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_auto_20190510_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Фотография'),
        ),
    ]