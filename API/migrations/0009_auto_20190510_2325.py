# Generated by Django 2.2.1 on 2019-05-10 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('API', '0008_auto_20190510_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments', verbose_name='Файл')),
                ('file_name', models.CharField(max_length=500, verbose_name='Имя файла')),
                ('file_mime', models.CharField(max_length=500, verbose_name='Расширение файла')),
                ('file_size', models.IntegerField(verbose_name='Размер файла')),
                ('uploaded', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Вложение',
                'verbose_name_plural': 'Вложения',
            },
        ),
        migrations.RemoveField(
            model_name='employee',
            name='photo',
        ),
        migrations.AddField(
            model_name='employee',
            name='attachment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                       to='API.Attachment', verbose_name='Фотография'),
        ),
    ]
