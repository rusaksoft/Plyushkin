from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import *
import bacumon

def detail(request, action_id):
    return HttpResponse("You're looking at action %s." % action_id)

def index(request):
	actions = Action.objects.all()
	context = {
		'actions': actions,
	}
	return render(request, 'actions/index.html', context)

def check(request):

	bacumon.check_all()

	return redirect("index")

def storages(request):

	storages = Storage.objects.all()
	return render(request, 'storages/index.html',{'storages':storages})

def storages_check(request):

	bacumon.check_storages()

	return  HttpResponse("You're looking at check")