# Generated by Django 4.1.4 on 2022-12-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0004_profilemodel_alter_consertmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='timemodel',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط شروع شده است'), (2, 'فروش بلیط تمام شده است'), (3, 'این سانس کنسل شده است'), (4, 'در حال فروش بلیط')], verbose_name='وضعیت'),
        ),
    ]
