from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Topic, Entries, Comment
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic.list import MultipleObjectMixin
from cms_app.forms import NewCommentForm



# Create your views here.

def index(request):
    return render(request, 'cms_app/index.html')

def about(request):
    return render(request, 'cms_app/about.html')

class TopicListView(ListView):
    model = Topic
    template_name = 'cms_app/topic_list.html'
    context_object_name = 'topic'
    paginate_by = 6

    def get_queryset(self):        
        search = self.request.GET.get('search', '') 
        topic = Topic.objects.filter(title__icontains=search)
        if not topic:
            messages.info(self.request, f'Topic {search} does not exist.')
        return topic[::-1]
     
class UserTopicListView(ListView):
    model = Topic
    template_name = 'cms_app/user_topic.html'
    context_object_name = 'topic'
    paginate_by = 4

    def get_queryset(self): 
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Topic.objects.filter(author=user)[::-1]
    

class ContentDetailView(DetailView, MultipleObjectMixin):
    model = Topic
    paginate_by = 5
    

    def get_context_data(self, **kwargs):           
        c_id = get_object_or_404(Topic, pk = self.kwargs['pk'])
        content  =  c_id.entries_set.all().order_by('-date_added')
        context = super(ContentDetailView, self).get_context_data(object_list=content, **kwargs)
        return context
    
                              
class SinglePageDetailView(DetailView):
    model = Entries
    template_name = 'cms_app/single_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Comment.objects.filter(
            entries=self.get_object()).order_by('-date_added')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance=self.request.user)
        return data
    
    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                                  author=self.request.user,
                                  entries=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

 

class CreateTopic(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)  
    
    '''def clean(self):
        if Topic.objects.filter(title=self.cleaned_data['title'].lower()).exists():   
            raise self.forms.ValidationError('Label exists!')
        return self.cleaned_data'''

          
class CreateTopicEntry(LoginRequiredMixin, CreateView):
    model = Entries
    fields = ['topic', 'name','text','entries_image']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # Filter the queryset to include only topics by current user
        form.fields['topic'].queryset = Topic.objects.filter(author=self.request.user)
        return form
    
   
class ContentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entries
    fields = ['name', 'text', 'entries_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        content = self.get_object()
        if self.request.user == content.author:
            return True
        return False

class ContentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entries
    success_url = '/'

    def test_func(self):
        content = self.get_object()    
        if self.request.user == content.author:
            return True
        return  False
        
class TopicUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topic
    fields = ['title']
    success_url = '/topic/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.author:
            return True
        return False

class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    success_url = '/'

    def test_func(self):
        topic = self.get_object()
        if self.request.user == topic.author:
            return True
        return False








   
    






        







    
 
  







        



  


        



    


 




        

   













