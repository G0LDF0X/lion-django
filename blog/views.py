from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView, TemplateView, FormView
from django.conf import settings
from blog.forms import PostSearchForm
from django.db.models import Q
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    # paginate_by = 3

    # def get_queryset(self):
    #     return Post.objects.all()

# 위의 class PostLV와 동일    
def dummy_post(request):
    objects = Post.objects.all()
    context = {
        'posts': objects
    }
    return render(request, "blog/post_all.html", context)

class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    # get_queryset -> get_object
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

# --ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_dt"
    template_name = "blog/post_archive.html"

class PostYAV(YearArchiveView):
    model = Post
    date_field = "modify_dt"
    make_object_list = True
    template_name = "blog/post_archive_year.html"

class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_dt"
    template_name = "blog/post_archive_month.html"

class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_dt"
    template_name = "blog/post_archive_day.html"

class PostTAV(TodayArchiveView):
    model = Post
    date_field = "modify_dt"
    template_name = "blog/post_archive_day.html"

class TagCloudTV(TemplateView):
    template_name = "taggit/taggit_cloud.html"

class TaggedObjectLV(ListView):
    template_name = "taggit/taggit_post_list.html"
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    
class SearchFormView(FormView):
    form_class = PostSearchForm

    # GET 요청 오면 화면 띄워줌
    template_name = "blog/post_search.html"

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)