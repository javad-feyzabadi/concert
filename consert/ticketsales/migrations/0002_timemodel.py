# Generated by Django 4.1.4 on 2022-12-11 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdatetime', models.DateTimeField()),
                ('seats', models.IntegerField()),
                ('status', models.IntegerField(choices=[('start', 'فروش بلیط شروع شده است'), ('end', 'فروش بلیط تمام شده است'), ('cancle', 'این سانس کنسل شده است'), ('sales', 'در حال فروش بلیط')])),
                ('consert', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.consertmodel')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketsales.locationmodel')),
            ],
        ),
    ]