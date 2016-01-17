
from django.db import models

# Create your models here.

class Categories(models.Model):
	# Category의 외래 키
	Title = models.CharField(max_length=40, null=False)

class TagModel(models.Model):
	# Tags의 MTM
	Title = models.CharField(max_length=20, null=False)	

class Entries(models.Model):
	# 기본적인 블로그 글의 구조
	# id = 0
	# 글의 일련 번호 - 숫자형, id는 장고에서 자동으로 만들어서 관리	
	# 굳이 정의할 필요 없다 - 알아서 +1을 해서 저장
	Title = models.CharField(max_length=80, null=False)
	Content = models.TextField(null=False)
	# 제목과 내용 - 문자형(각각 길이제한)
	# 문자형은 CharField(256글자), TextField(훨씬 긴 글자)
	# max_length속성으로 최대 길이 지정, null값은 False로 반드시 입력해야 함
	created = models.DateTimeField(auto_now_add=True, auto_now=True)
	# 작성 일시 - 날짜/시간형
	# DateTimeField - auto_now_add는 처음 생성될 때, auto_now는 저장될 때
	Category = models.ForeignKey(Categories)
	# 글 카테고리 - 숫자형
	# 각 카테고리는 여러개의 글을 가리키고 있다(many-to-one 관계) = 외래키(ForeignKey)로 정의
	# Cateogry가 Categories라는 클래스를 외래키로 가리킨다.
	Tags = models.ManyToManyField(TagModel)
	# 꼬리표 - 문자형(20)
	# 하나의 글이 여러개의 태그를 가질 수 있다 (many-to-many 관계) = ManyToManyField
	# Tags가 TagModel이라는 클래스와 MTM관계를 갖는다
	Comments = models.PositiveSmallIntegerField(default=0, null=True)
	# 댓글 수 - 숫자형
	# 숫자형은 IntegerField(큰숫자형), SamllIntergerField(작은숫자형) (양수만 다루려면 앞에 Positive)

class Comments(models.Model):
	# 댓글 모델
	Name = models.CharField(max_length=20, null=False)
	Password = models.CharField(max_length=32, null=False)
	Content = models.TextField(max_length=500, null=False)
	created = models.DateTimeField(auto_now_add=True, auto_now=True)
	Entry = models.ForeignKey(Entries)
	# 여러개의 댓글은 하나의 글을 가리킨다. (Many Comments - One Entries)