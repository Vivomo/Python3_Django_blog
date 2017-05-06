from datetime import datetime

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=120, verbose_name='标题', default='', null=False)
    summary = models.CharField(max_length=300, verbose_name='概要', default='', null=True)
    content = models.TextField()
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateTimeField(default=datetime.now, verbose_name='更新时间')

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name


