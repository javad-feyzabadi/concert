# Generated by Django 4.1.4 on 2022-12-14 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام')),
                ('family', models.CharField(max_length=100, verbose_name='فامیل')),
                ('gender', models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], verbose_name='جنسیت')),
                ('profileimage', models.ImageField(upload_to='profileimage/', verbose_name='عکس پروفایل')),
                ('credit', models.IntegerField(default=0, verbose_name='اعتبار')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربری')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل',
            },
        ),
    ]
