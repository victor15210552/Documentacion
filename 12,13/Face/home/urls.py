from django.conf.urls import include,url
from django.conf import settings
from django.contrib.auth.views import *
from django.conf.urls.static import static
from .views import (SignUp, Perfil_View, Perfil_Update, Friend_List, Community_List,Add_Friend,
	Delete_Friend, Register_Publication, Report_Publication, Score_Publication,
	Unscored_Publication, Register_Comment, Score_Comment,Perfil_Detail)

urlpatterns = [

	    url(r'^$',login,{'template_name': 'home/index.html'}, name='login'),
    url('logout/',logout_then_login, name='logout'),

	url(r'signup/', SignUp.as_view(), name='signup'),

	url(r'^perfil_view/$', Perfil_View.as_view(),name='perfil_view'),


	url(r'^update_perfil/$', Perfil_Detail.as_view(), name='perfil_update'),


	url(r'^friend_list/$', Friend_List.as_view(), name='friend_list'),
	url(r'^community_list/$', Community_List.as_view(), name='community_list'),
	url(r'^add_friend/(?P<pk>[\w-]+)/(?P<friend>[\w-]+)/$', Add_Friend, name='add_friend'),
	url(r'^delete_friend/(?P<pk>[\w-]+)/(?P<friend>[\w-]+)/$', Delete_Friend, name='delete_friend'),
	url(r'^register_publication/$', Register_Publication.as_view(), name='register_publication'),
	url(r'^report_publication/$', Report_Publication.as_view(), name='report_publication'),
	url(r'^score_publication/(?P<pk>[\w-]+)/$',Score_Publication , name='score_publication'),
	url(r'^unscored_publication/(?P<pk>[\w-]+)/$',Unscored_Publication , name='unscored_publication'),
	url(r'^detail_publication/(?P<pk>[\w-]+)/$', Register_Comment.as_view(), name='detail_publication'),
	url(r'^score_comment/(?P<publication>[\w-]+)/(?P<comment>[\w-]+)/$',Score_Comment , name='score_comment'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
