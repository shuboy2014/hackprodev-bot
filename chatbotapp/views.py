from django.http import JsonResponse
from django.views.generic import View

try:
    from hackbot.secret import ACCESS_TOKEN, VERIFY_TOKEN
except ImportError as e:
    print(e, "Your have not Access token and verify_token")


class Index(View):
    def get(self, request):
        pass

    def post(self, request):
        pass