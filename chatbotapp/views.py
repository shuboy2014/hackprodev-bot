# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import os
import json
import pprint
import requests

try:
    from chatbot.secret import ACCESS_TOKEN, VERIFY_TOKEN
except ImportError as e:
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', '')
    VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN', '')
    if not ACCESS_TOKEN or not VERIFY_TOKEN:
        print(e, "Your have not Access token and verify_token")

URL = 'https://graph.facebook.com/v2.6/me/messages?access_token=' + ACCESS_TOKEN


def send_msg(fbid, msg):
    x = requests.post(URL, json.dumps({"recipient": {"id": fbid}, "message": {"text": "hello world!"}}),
                      headers={"Content-Type": "application/json"})
    pprint.pprint(x.json())


class ChatBotView(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET.get('hub.verify_token', '') == VERIFY_TOKEN:
            print("Facebook Ping!")
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            print("Anonymous Ping!")
            return JsonResponse({"status": "Invalid Token"})

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        msg = json.loads(self.request.body.decode('utf-8'))
        for entry in msg['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    send_msg(message['sender']['id'], message['message']['text'])
        return HttpResponse()
