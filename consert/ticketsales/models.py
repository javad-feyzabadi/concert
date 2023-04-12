from django.db import models
from jalali_date import date2jalali,datetime2jalali
from accounts.models import ProfileModel



class ConsertModel(models.Model):
    class Meta:
        verbose_name = 'کنسرت'
        verbose_name_plural = 'کنسرت'
    name = models.CharField(max_length = 100,verbose_name=' نام کنسرت')
    singername = models.CharField(max_length = 100,verbose_name='خواننده')
    length = models.IntegerField(verbose_name='زمان کنسرت')
    poster = models.ImageField(upload_to = 'consertimage/',verbose_name='پوستر',null = True)

    def __str__(self):
        return self.name

class LocationModel(models.Model):
    class Meta:
        verbose_name = 'مکان کنسرت'
        verbose_name_plural = 'مکان کنسرت'
    name = models.CharField(max_length = 100,verbose_name='نام مکان')
    address = models.CharField(max_length = 500,default='تهران-برج میلاد',verbose_name='آدرس')
    phone = models.CharField(max_length = 11,null = True,verbose_name='تلفن')
    capacity = models.IntegerField(verbose_name='گنجایش')

    def __str__(self):
        return self.name
class TimeModel(models.Model):
    class Meta:
        verbose_name = 'زمان '
        verbose_name_plural = 'زمان '
    consert = models.ForeignKey('ConsertModel',on_delete=models.PROTECT,verbose_name='کنسرت')
    location = models.ForeignKey('LocationModel',on_delete = models.PROTECT,verbose_name='مکان')
    startdatetime = models.DateTimeField(verbose_name='ساعت و تاریخ')
    seats = models.IntegerField(verbose_name='صندلی')

    Start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_choices =(
        (Start,'فروش بلیط شروع شده است'),
        (End,'فروش بلیط تمام شده است'),
        (Cancle,'این سانس کنسل شده است'),
        (Sales,' در حال حاضر فروش بلیط شروع شده است'),

    )
    status = models.IntegerField(choices=status_choices,verbose_name='وضعیت')

    def __str__(self):
        return "Time: {}, consert: {}, location: {}".format(self.startdatetime,self.consert.name,self.location.name)

    def get_jalali_date(self):
        return datetime2jalali(self.startdatetime)


class TicketModel(models.Model):
    class Meta:
        verbose_name = 'بلیط'
        verbose_name_plural = 'بلیط'
    profilemodel = models.ForeignKey(ProfileModel,on_delete = models.PROTECT,verbose_name='پروفایل')
    timemodel = models.ForeignKey('TimeModel',on_delete = models.PROTECT,verbose_name='زمان')
    name = models.CharField(max_length = 100,verbose_name='نام')
    price = models.IntegerField(verbose_name='قیمت')
    ticketimage = models.ImageField(upload_to = 'ticketimage/',verbose_name='عکس')

    def __str__(self):
        return self.name