#_*_encoding:utf-8_*_

from datetime import datetime

from django.db import models


class Writer(models.Model):
	username = models.CharField(max_length = 20,verbose_name = u"作者")
	for_self = models.CharField(max_length = 200,default="",verbose_name = u"自我介绍")
	picture = models.ImageField(upload_to = "writer/%Y/%m",verbose_name = u'作者头像',max_length = 100)
	add_time = models.DateField(auto_now_add = True,verbose_name = u"首次加入时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	
	class Meta:
		verbose_name = u"作者"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.username

class User_tag(models.Model):
	tags = models.CharField(max_length = 30,verbose_name = u"作者标签")
	user_tag_writer = models.ForeignKey(Writer,on_delete = models.CASCADE,verbose_name = u"作者" )
	add_time = models.DateField(auto_now_add = True,verbose_name= u"添加时间")
	
	class Meta:
		verbose_name = u"用户标签"
		verbose_name_plural = verbose_name

class User_view(models.Model):
	writer_view = models.TextField(verbose_name = u"作者语句")
	user_view_writer = models.ForeignKey(Writer,on_delete = models.CASCADE,verbose_name = u"作者" )
	add_time = models.DateField(auto_now_add = True,verbose_name= u"添加时间")

	class Meta:
		verbose_name = u"用户语句"
		verbose_name_plural = verbose_name

class Article(models.Model):
	title = models.CharField(max_length = 100,verbose_name = u"文章标题" )
	content = models.TextField(verbose_name = u"正文")
	jiexuan = models.CharField(max_length = 200,default="",verbose_name = u"文章节选")
	writer = models.ForeignKey(Writer,on_delete = models.CASCADE,verbose_name = u"作者")
	chatu = models.ImageField(upload_to="chatu/%Y/%m",verbose_name = u"文章插图",max_length = 100)
	add_time = models.DateField(auto_now_add = True,verbose_name = u"添加时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	article_tage = models.CharField(max_length = 50,verbose_name = u"文章标签")
	
	class Meta:
		verbose_name = u"文章"
		verbose_name_plural = verbose_name 
	
	def __str__(self):
		return self.title



class Comment(models.Model):
	name = models.CharField(max_length = 40,verbose_name = u"评论者名称")
	email = models.EmailField(verbose_name = u"评论者邮箱")
	customer_url = models.SlugField(verbose_name = u"评论者网站")
	comment = models.TextField(verbose_name = u"评论")
	add_time = models.DateField(auto_now_add = True,verbose_name = u"创建时间")
	comment_article = models.ForeignKey( Article,on_delete = models.CASCADE,verbose_name = u"文章")	
	class Meta:
		verbose_name = u"评论"
		verbose_name_plural = verbose_name
	def __str__(self):
		return self.name
	
class Banner(models.Model):
	image = models.ImageField(upload_to = "banner/%Y/%m",verbose_name = u"轮播图",max_length = 100)
	create_time = models.DateTimeField(default = datetime.now,verbose_name = u"创建时间")
	add_time = models.DateField(auto_now_add = True,verbose_name = u"添加时间")
	change_time = models.DateField(auto_now = True,verbose_name = u"最近修改时间")
	
	class Meta:
		verbose_name = u"轮播图"
		verbose_name_plural = verbose_name


# Create your models here.
