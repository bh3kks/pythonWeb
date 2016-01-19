from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
	# 우리가 쓸 주소체계의 규칙을 정의
	# Examples: ('주소 규칙', '실행할 행동 지정')
	url(r'^blog/$', views.index),
	# /blog/ : index함수를 실행한다 (맨 처음 화면)
	url(r'^blog/page/(?P<page>[0-9]+)/$', views.index), 
	# /blog/page/숫자 : 글 목록의 쪽 번호를 의미
	# (?P<page>d+)는 (d+)를 넘겨줄 때, page라는 이름으로 넘겨주는 것!
	url(r'^blog/entry/(?P<entry_id>[0-9]+)/$', views.read),
	# /blog/entry/숫자 : 특정 글 하나 가져와서 출력
	url(r'^blog/write/$', views.write_form),
	# /blog/write/ : 블로그에 글 쓰기
	url(r'^blog/add/post/$', views.add_post),
	# /blog/add/post/ : 폼 내용을 전송할 주소?
	url(r'^blog/add/comment/$', views.add_comment),
	# 댓글 추가
	url(r'^blog/del/comment/(?P<cmt_id>[0-9]+)/$', views.del_comment),
	# 댓글 삭제
	url(r'^blog/del/comment/(?P<cmt_id>[0-9]+)/result/$', views.del_comment_result),
	# 댓글 삭제 - 결과

    url(r'^admin/', include(admin.site.urls)),
)
