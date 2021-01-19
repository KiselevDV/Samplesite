from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import BbForm
from .models import Bb, Rubric


def index(request):
    """Главная страница"""
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    """Вывод объявлений по заданной рубрике"""
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric
    }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    """Ввод новых объявлений"""
    # путь к файлу шаблона, создающего страницу с формой
    template_name = 'bboard/create.html'
    # ссылка на класс формы, связанной с моделью
    form_class = BbForm
    # интернет-адрес для перенаправления после успешного сохранения данных
    # reverse_lazy - аналог redirect
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
