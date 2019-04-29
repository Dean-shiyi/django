from django.db import models

# Create your models here.


class MovieKind(models.Model):
    '''
    电影类型
    '''
    name = models.CharField(max_length=255, verbose_name='电影类型')
    desc = models.CharField(max_length=255, verbose_name='电影类型描述')

    def __str__(self):
        return self.name


class MovieDetall(models.Model):
    title = models.CharField(max_length=255,verbose_name='电影标题',unique=True)
    desc = models.CharField(max_length=1000,verbose_name='电影简介',default='暂无简介')
    online_time = models.DateField(verbose_name='上映日期')
    # uplode to上传到哪个地方
    img = models.ImageField(upload_to='movie',null=True,default=None,blank=True)

    # kind = models.ForeignKey(MovieKind，default=None)   只能设置一个类型描述
    kind = models.ManyToManyField(MovieKind)

    def __str__(self):
        return self.title



