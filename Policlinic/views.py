from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Policlinic.models import Comment,CommentForm

def index(request):
    return HttpResponse("Policlinic sayfasi")


    
