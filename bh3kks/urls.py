from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
	# 우리가 쓸 주소체계의 규칙을 정의
	# Examples: ('주소 규칙', '실행할 행동 지정')
	url(r'^blog/$', views.index),
	# /blog/ : index함수를 실행한다 (맨 처음 화면)
	url(r'^blog/page/(?P<page>d+)/$', views.index), 
	# /blog/page/숫자 : 글 목록의 쪽 번호를 의미
	# (?P<page>d+)는 (d+)를 넘겨줄 때, page라는 이름으로 넘겨주는 것!


    url(r'^admin/', include(admin.site.urls)),
)
