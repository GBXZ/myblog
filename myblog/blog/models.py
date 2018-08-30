#_*_encoding:utf-8_*_

from datetime import datetime

from django.db import models


class Writer(models.Model):
	username = models.CharField(max_length = 20,verbose_name = u"作者")
	picture = models.ImageField(upload_to = "writer/%Y/%m",verbose_name = u'作者头像',max_length = 100)
	user_tag = models.CharField(max_length = 100,verbose_name = u"作者标签")
	user_view = models.TextField(verbose_name = u"作者语句")
	add_time = models.DateField(auto_now_add = True,verbose_name = u"首次加入时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	
	class Meta:
		verbose_name = u"作者"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.username


class Comment(models.Model):
	name = models.CharField(max_length = 40,verbose_name = u"评论者名称")
	email = models.EmailField(verbose_name = u"评论者邮箱")
	customer_url = models.SlugField(verbose_name = u"评论者网站")
	comment = models.TextField(verbose_name = u"评论")
	add_time = models.DateField(auto_now_add = True,verboser_name = u"创建时间")	
	class Meta:
		verbose_name = u"评论"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name
	
class Banner(models.Model):
	image = models.ImageField(upload_to = "banner/%Y/%m",verbose_name = u"轮播图",max_length = 100)
	add_time = models.DateField(auto_now_add = True,verbose_name = u"添加时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	
	class Meta:
		verbose_name = u"轮播图"
		verbose_name_plural = verbose_name


class Article(models.Model):
	title = models.CharField(max_length = 100,verbose_name = u"文章标题" )
	content = models.TextField(verbose_name = u"正文")
	writer = models.ForeignKey(Writer,on_delete = models.CASCADE,verbose_name = u"作者")
	chatu = models.ImageField(upload_to="chatu/%Y/%m",verbose_name = u"文章插图",max_length = 100)
	add_time = models.DateField(auto_now_add = True,verbose_name = u"添加时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	comment_total = models.Comment	

# Create your models here.
