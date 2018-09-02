import xadmin
from blog.models import Writer,Article,Banner,Comment

class WriterAdmin(object):
	list_display = ['username','picture','user_tag','user_view','add_time','change_time']
	search_fields = ['username','user_view','user_tag']
	list_filter = ['username','picture','user_tag','user_view','add_time','change_time']


class ArticleAdmin(object):
	list_display = ['title','content','writer','chatu','add_time','change_time','article_tage']
	search_fields = ["title","writer","article_tage"]
	list_filter =  ['title','content','writer','add_time','change_time','article_tage']


class BannerAdmin(object):
	list_display = ['image']
	list_filter = ['image','add_time','change_time']


class CommentAdmin(object):
	list_display = ["name","email","customer_url","comment","add_time","comment_article"]
	serch_fields =  ["name","email","customer_url","comment","comment_article"]
	list_filter = ["name","email","customer_url","comment","add_time","comment_article"]


xadmin.site.register(Writer,WriterAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(Comment,CommentAdmin)
