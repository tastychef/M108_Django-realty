from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Zhk


class ZhkView(View):
    '''Вывод проектов'''

    def get(self, request, *args, **kwargs):
        projects = Zhk.objects.all()
        return render(request, 'index.html', {'zhk_list': projects})

class ZhkDetail(View):
    '''Отдельная страница'''
    def get(self, request, pk):
        project = Zhk.objects.get(id=pk)
        return render(request, 'index_detail.html', {'project': project})