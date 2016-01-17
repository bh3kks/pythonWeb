# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, page=1):
	# 기본적인 request말고도 page도 인자로 넘겨받는다(기본값 = 1)
	return HttpResponse('안녕, 여러분')