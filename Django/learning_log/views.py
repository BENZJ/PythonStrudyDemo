#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Topic,Entry
from django.core.urlresolvers import reverse
from .forms import TopicForm,EntryForm
#在这里创建视图
def index(request):
	"""学习笔记首页"""
	return render(request,'learning_log/index.html')
	#return HttpResponse("index Test")

def topics(request):
	"""显示所有的主题"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics':topics}
	return render(request,'learning_log/topics.html',context)

def topic(request,topic_id):
	"""显示单个主题及其所有的条目"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic':topic,'entries':entries}
	return render(request,'learning_log/topic.html',context)

def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		#未提交数据创建一个新的表单
		form = TopicForm()
	else:
		#POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topics'))
			# return HttpResponseRedirect(reverse(''))
	context = {'form':form}
	return render(request,'learning_log/new_topic.html',context)

def new_entry(request,topic_id):
	"""在特定的主题中添加条目"""
	topic = Topic.objects.get(id=topic_id)

	if request.method !='POST':
		#未提交数据表单
		form = EntryForm()
	else:
		# POST提交的数据，对数据进行处理
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('topic',args=[topic_id]))

	context = {'topic':topic,'form':form}
	return render(request,'learning_log/new_entry.html',context)

def edit_entry(request,entry_id):
	"""编辑条目"""
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic
	if request.method != 'POST':
		#初次请求，使用当前条目填充表单
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('topic', args=[topic.id]))
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_log/edit_entry.html', context)
