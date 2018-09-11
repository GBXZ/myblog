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
		p_count = p.page_range #该段代码实现，点击上一页和下一页功能，如果分别把x、y两个参数放在上一页和下一页连接上
		if nid=="":
			nid = 1
			x = 1
		elif nid == "1":
			x = 1
		else:
			x = int(nid)-1
		print(nid,x)
		if nid == str(p.num_pages):
			y = p.num_pages
		else:
			y =int(nid) + 1
		page = p.page(nid)	
		return render(request,"blog/lw-index.html",locals())

class Wenzhang(View):
	def get(self,request,nid):
		wenzhang = Article.objects.filter(id = int(nid))
		shang = int(nid)-1      #这段代码是获取上一页id
		if nid == 1:           #当传过来id = 1 时，上一页id也为1
			shang == 1
		'''
		 #如果当shang不存在数据库，而且shang>0, 上做自减，知道有一条不满足，则跳出，获得当前shang值
		'''
		while not Article.objects.filter(id = shang) and shang > 0:  
			shang -= 1
		'''
		#如果当前做自减的shang值等于0，则把他赋值为，上面的nid，说明，这是最前面一个，
		比如当前nid = 3，id 2、1都没数据，前面不停做自减，最终会减到0，
		'''
		if shang == 0:  
			shang = int(nid)
		shang_article = Article.objects.filter(id = shang)              #获取文章标题
		#下一页
		'''
		首先把所有id都取出来，放在一个列表中，进行排序，取出最大那一个，作为最大界限
		'''
		id_count = []
		all_wenzhang = Article.objects.all()
		for p in all_wenzhang:
			id_count.append(p.id)
		id_count.sort()
		xia = int(nid) + 1
		'''
		如果int(nid) == id 中最大值，就令xia = int（nid） 
		'''
		if int(nid) == id_count[-1]:
			xia = int(nid)
		#如过xia不再id_count这个列表中，那么就进行自加，直到在这个列表，跳出while，得到当前xia值，当然自加不能超过id_count最大值
		while xia not in id_count and xia < id_count[-1]:
			xia += 1
		#如果超过最大值，就等于最大值
		if xia> id_count[-1]:
			xia = id_count[-1]
		xia_article = Article.objects.filter(id = xia)  #为了获取文章标题	                   
		return render(request,"blog/lw-article-fullwidth.html",locals())


# Create your views here.
