#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
#在这里创建视图
def index(request):
	"""学习笔记首页"""
	return render(request,'index.html')
	#return HttpResponse("index Test")
