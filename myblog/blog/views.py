from django.shortcuts import render
from django.views.generic.base import View
from blog.models import Banner,Writer,User_tag,User_view,Article
from django.core.paginator import Paginator


class Index(View):
	def get(self,request,nid):
		banners = Banner.objects.all() 
		writer = Writer.objects.all()
		user_tag = User_tag.objects.all()
		user_view = User_view.objects.all()
		articles = Article.objects.all().order_by("id")  #需要对取出数据进行排序，因为p = Paginator(articles,4)是无序的
		p = Paginator(articles,4)
		if nid=="":
			nid = 1
		p_count = p.page_range #该段代码实现，点击上一页和下一页功能，如果分别把x、y两个参数放在上一页和下一页连接上
		if nid =="" or nid == 1:
			x = 1
		else:
			 x = int(nid)-int(1)
		if nid == p.num_pages:
			y = p.num_pages
		else:
			y =int(nid)+int(1)
		page = p.page(nid)		
		return render(request,"blog/lw-index.html",locals())

class Wenzhang(View):
	def get(self,request,nid):
		wenzhang = Article.objects.filter(id = int(nid))
		return render(request,"blog/lw-article-fullwidth.html",locals())


# Create your views here.
