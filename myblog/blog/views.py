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
		articles = Article.objects.all()
		p = Paginator(articles,4)
		if nid=="":
			nid = 1
		p_count = p.page_range
		page = p.page(nid)		
		return render(request,"blog/lw-index.html",locals())


# Create your views here.
