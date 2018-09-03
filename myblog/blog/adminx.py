import xadmin
from blog.models import Writer,Article,Banner,Comment,User_tag,User_view

class WriterAdmin(object):
	list_display = ['username','picture','add_time','change_time']
	search_fields = ['username']
	list_filter = ['username','picture','add_time','change_time']


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

class User_tagAdmin(object):
	list_display = ["tags","user_tag_writer","add_time"]
	serch_fields =  ["tags","user_tag_writer"]
	list_filter = ["tags","user_tag_writer","add_time"]

class User_viewAdmin(object):
	list_diplay = ["writer_view","user_view_writer","add_time"]
	serch_fields =  ["writer_view","user_view_writer"]
	list_filter = ["writer_view","user_view_writer","add_time"]

xadmin.site.register(Writer,WriterAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(User_tag,User_tagAdmin)
xadmin.site.register(User_view,User_viewAdmin)
