# encoding=utf8
from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings

from .models import Join
from .forms import CollectEmailForm

def main(request):
    form = CollectEmailForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        subject = 'norm.com сайтад бүртгүүлсэн танд баярлалаа'
        message = 'Таны и-мэйлийг бүртгэж авлаа.'
        from_email = settings.EMAIL_HOST_USER
        to_list = [new_join.email, settings.EMAIL_HOST_USER]
        send_mail(subject, message,from_email, to_list, fail_silently=True)
        return render_to_response('main.html', {'message':message}, context_instance=RequestContext(request))

    return render_to_response('main.html', locals(), context_instance=RequestContext(request))

def norm(request):
    return render_to_response('norm.html')

def features(request):
    return render_to_response('features.html')