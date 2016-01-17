# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entries
from django.template import Context

# Create your views here.

def index(request, page=1):
	# 글 목록을 보여주는 함수
	# 기본적인 request말고도 page도 인자로 넘겨받는다(기본값 = 1)
	if isinstance(page, int) == False:
		page = 1
	# page가 적절한 int 값으로 들어왔는지 검사

	page_title = '블로그 글 목록 화면'

	# 페이지 수 계산
	per_page = 5
	start_pos = (int(page)-1)*per_page
	end_pos = start_pos+per_page

	res = Entries.objects.count()/5
	if (Entries.objects.count()%5) > 0:
		remain = 1
	else:
		remain = 0
	page_num = int(res) + int(remain) + 1
	# page_num은 실제 페이지 수보다 +1

	entries = Entries.objects.all().order_by('-created')[start_pos:end_pos]
 	# Entries.objects.all()로 모든 Entries를 부러오고, 한 페이지에 5개씩 보여진다
	context = {
		'page_title':page_title,
		'entries':entries,
		'current_page':page,
		'range':range(page_num)
		#range로 0,1,2,3... 배열 생성 -> 전달
	}

	return render(request, 'index.html', context)
	# 첫번째 엔트리 타이틀을 출력, encode('utf-8')은 문자열을 아스키 문자형으로 변환

def read(request, entry_id=None):
	# 하나의 글을 보여주는 함수, entry_id를 넘겨받는다
	page_title = '블로그 글 읽기 화면'

	current_entry = Entries.objects.get(id=int(entry_id))

	try:
		prev_entry = current_entry.get_previous_by_created()
	except:
		prev_entry = None

	try:
		next_entry = current_entry.get_next_by_created()
	except:
		next_entry = None


	context = {
		'page_title':page_title,
		'current_entry':current_entry,
		'prev_entry':prev_entry,
		'next_entry':next_entry
	}

	return render(request, 'read.html', context)

