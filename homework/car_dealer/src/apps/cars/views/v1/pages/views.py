from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

# from src.apps.board.forms import CommentForm
from src.apps.cars.models import Car


class CarListView(ListView):
    model = Car
    paginate_by = 10
    template_name = 'car/list.html'
    context_object_name = 'cars'  # instead of object_list (as default)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs.filter(owner=self.request.user)
        return qs.active()


class CarDetailView(DetailView):
    model = Car
    template_name = 'car/detail.html'
    context_object_name = 'car'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['resource_url'] = reverse('car:detail', kwargs={'pk': self.object.id})
        # data['books'] = list(Board.objects.filter(name__contains='cool'))
        # data['comment_form'] = CommentForm()
        return data


# class TaskCreateView(CreateView):
#     model = Task
#     fields = ['name', 'column']
#     template_name = 'task/create.html'
#
#     def get_form(self, form_class=None):
#         return self.get_form_class()(initial={'board': ''})
#
#     def form_valid(self, form):
#         # obj = form.save(commit=False)
#         # obj.board = ''
#         # obj.owner = self.request.user
#         # obj.save()
#         return super().form_valid(form)
#
#
def cars_list_api_view(requests):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(data, status=200)
