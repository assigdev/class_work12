from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            message = request.GET['message']
            print(request.GET)
            message = 'Вы отправили такое сообщение %s' % message
            return JsonResponse({'message': message})
        else:
            return super().get(request, *args, **kwargs)


def ajax_user(request):
    message = request.GET['message']
    message = 'Вы отправили такое сообщение %s' % message
    return JsonResponse({'message': message})


class SendView(TemplateView):
    template_name = 'send.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            message = request.GET['message']
            print(request.GET)
            message = 'Вы отправили такое сообщение %s' % message
            return render(request, 'send_ajax.html', {'message': message})
        else:
            return super().get(request, *args, **kwargs)
