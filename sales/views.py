from django.http import HttpResponse

def index(request):
    return HttpResponse("売上構築アプリ（仮）")