# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.template import Template, Context
from django.http import HttpResponse,Http404



def queSong(request):
    return render_to_response("song.html")