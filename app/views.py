from django.views.generic.base import TemplateView
from django.views.generic import ListView

from django.shortcuts import render
from django.http import HttpResponse 
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings 
from chatterbot.trainers import ChatterBotCorpusTrainer


class IndexView(TemplateView):
    template_name = 'app/index.html'


def bot_response(request):

    chatbot = ChatBot(read_only=True,    
                      trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                      **settings.CHATTERBOT)

    input_data = request.POST.get('input_text')
    if not input_data:
        return HttpResponse('<h2>空のデータを受け取りました。</h2>', status=400)

    bot_response = chatbot.get_response(input_data)
    http_response = HttpResponse()
    http_response.write('{}: {}'.format(chatbot.name, bot_response))
    return http_response

