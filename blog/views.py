# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Entries, Categories, TagModel, Comments
from django.template import Context

# Create your views here.

def index(request, page=1):
	# 글 목록을 보여주는 함수
	# 기본적인 request말고도 page도 인자로 넘겨받는다(기본값 = 1)

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

	try:
		current_entry = Entries.objects.get(id=int(entry_id))
	except:
		return HttpResponse('current_entry False.')

	try:
		prev_entry = current_entry.get_previous_by_created()
	except:
		prev_entry = None

	try:
		next_entry = current_entry.get_next_by_created()
	except:
		next_entry = None

	comments = Comments.objects.filter(Entry=current_entry)


	context = {
		'page_title':page_title,
		'current_entry':current_entry,
		'prev_entry':prev_entry,
		'next_entry':next_entry,
		'comments':comments
	}

	return render(request, 'read.html', context)

def write_form(request):
	# 글을 쓰는 화면 출력
	page_title = '블로그 글 쓰기 화면'

	categories = Categories.objects.all()

	context = {
		'page_title':page_title,
		'categories':categories
	}
	return render(request, 'write.html', context)

def add_post(request):

	# 타이틀 검사
	if 'title' in request.POST:
		if len(request.POST['title']) == 0:
			return HttpResponse('글자를 입력하세요.')
		else:
			entry_title = request.POST['title']
	else: 
		return HttpResponse('False')

	# 내용 검사
	if 'content' in request.POST:
		if len(request.POST['content']) == 0:
			return HttpResponse('글자를 입력하세요.')
		else:
			entry_content = request.POST['content']
	else:
		return HttpResponse('False')

	# 카테고리 검사
	if 'category' in request.POST:
		entry_category_title = request.POST['category']
		for category in Categories.objects.all():
			if category.Title == entry_category_title:
				entry_category = category
	else:
		return HttpResponse('False')

	# 태그 검사
	if 'tags' in request.POST:
		tags = map(lambda str: str.strip(), request.POST['tags'].split(','))
		# tags = []
		# split_tags = unicode(request.POST['tags']).split(',')
		# for tag in split_tags:
		#  	 tag_list.append(tag.strip())
		# tags에 깔끔하게 잘라진 tag의 리스트가 저장된다.
		tag_list = []
		for tag in tags:
		    tag_list.append(TagModel.objects.get_or_create(Title=tag)[0])
		# tag_list에 튜플 자료형 중 obj만 추가한다.

	else:
		tag_list = []

	# 새로 만든 글을 DB에 저장 - 1차 저장
	new_entry = Entries(Title=entry_title, Content=entry_content, Category=entry_category)
	# new_entry = Entries()
 	# new_entry.Title = entry_title
 	# new_entry.Content = entry_content
 	# new_entry.Category = entry_category 와 같은 코드이다.
	try:
		new_entry.save()
	except:
		return HttpResponse('글 생성 중 오류.')
 	# 1차 저장 완료

 	# tag가 존재하는 경우 태그까지 2차 저장
	for tag in tag_list:
 		new_entry.Tags.add(tag)
	if len(tag_list) > 0:
		try:
			new_entry.save()
		except:
			return HttpResponse('글 생성 중 오류.')
	# 2차 저장 완료

	# 성공 안내 메시지
	return HttpResponse('%s번 글을 제대로 써넣었습니다.' % new_entry.id)

def add_comment(request):
	
	# 이름 검사
	if 'name' in request.POST:
		if len(request.POST['name']) == 0:
			return HttpResponse('이름을 입력하세요.')
		else:
			cmt_name = request.POST['name']
	else: 
		return HttpResponse('False in name')

	# 비밀번호 검사
	if 'password' in request.POST:
		if len(request.POST['password']) == 0:
			return HttpResponse('비밀번호를 입력하세요.')
		else:
			cmt_password = request.POST['password']
	else: 
		return HttpResponse('False in password')

	# 내용 검사
	if 'content' in request.POST:
		if len(request.POST['content']) == 0:
			return HttpResponse('내용을 입력하세요.')
		else:
			cmt_content = request.POST['content']
	else: 
		return HttpResponse('False in content')

	# 댓글을 달 글 확인
	if 'entry_id' in request.POST:
		try:
			entry = Entries.objects.get(id=request.POST['entry_id'])
		except:
			return HttpResponse('그런 글은 없지롱')
	else:
		return HttpResponse('False in entry_id')


	try:
		new_cmt = Comments(Name=cmt_name, Password=cmt_password, Content=cmt_content, Entry=entry)
		new_cmt.save()
		return HttpResponse('댓글 입력 완료.')
	except:
		return HttpResponse('False.')

	return HttpResponse('False in final.')
