from django.db import models
# 在网站开发的初始阶段 一般都先编写我们的数据模型
# Create your models here.

# 创建音乐网站数据
class Music(models.Model):
    # 编写字段
    id = models.AutoField(max_length=11, db_column='music_id', primary_key=True)
    # 定义字段数据的数据类型 字符串 blank 该字段数据不能允许为空
    name = models.CharField(max_length=255, db_column='music_name', blank=False)
    singer = models.CharField(max_length=255, db_column='singer', blank=False)

    came_from = models.CharField(max_length=255, db_column='came_from', blank=True)
    kbps = models.CharField(max_length=255, db_column='music_kbps', blank=True)
    size = models.CharField(max_length=255, db_column='music_size', blank=True)
    language = models.CharField(max_length=255, db_column='music_language', blank=True)
    released_data = models.CharField(max_length=255, db_column='released_data', blank=True)
    url = models.CharField(max_length=255, db_column='bdyun_url', blank=False)
    password = models.CharField(max_length=255, db_column='bdyun_password', blank=True)

    # 内部类
    class Meta:
        # 表名
        db_table = 'music_info'

        # 在管理系统做中文显示的
        verbose_name = '音乐'
        verbose_name_plural = verbose_name