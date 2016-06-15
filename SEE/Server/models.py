#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User,AbstractUser
sex_state=(('m','male'),('f','female'))

class Doctor(models.Model):
    user = models.OneToOneField(User, default=None)
    username = models.CharField('username', max_length=30)
    sex = models.CharField('sex', max_length=2, choices=sex_state, blank=True)
    age = models.IntegerField('age', default=0, blank=True)
    dept = models.CharField('department', max_length=50, blank=True)
    post = models.CharField('post', max_length=50, blank=True)
    title = models.CharField('title', max_length=50, blank=True)
    phone = models.IntegerField('phone', blank=True)
    address = models.CharField('address', max_length=50, blank=True)
    hospital = models.CharField('hospital', max_length=50, blank=True)
    class Meta:
        verbose_name = 'doctor'
        verbose_name_plural = 'doctor'

    def __unicode__(self):
        return self.user.username

class Patient(models.Model):
    user    = models.OneToOneField(User, default=None)
    username = models.CharField('username', max_length=30)
    birthday = models.DateTimeField('birth day', blank=True, null=True)
    add     = models.CharField('address', max_length=50, blank=True)
    health  = models.CharField('health', max_length=200, blank=True)
    ps      = models.CharField('ps', max_length=200, blank=True)
    idnum   = models.IntegerField('idcard', blank=True)
    occupation = models.CharField('occupation', max_length=50, blank=True)
    diagnose = models.TextField('diagnose',default='nothing', blank=True)
    sex		= models.CharField('sex', max_length=2, choices=sex_state, blank=True)

    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patient'

    def __unicode__(self):
        return self.user.username

class Key_Store(models.Model):
    key = models.CharField('key', max_length=30)

    class Meta:
        verbose_name = 'api_key'
