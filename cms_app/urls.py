from django.urls import path
from . import views
from .views import (TopicListView, SinglePageDetailView, ContentUpdateView, ContentDeleteView,ContentDetailView,
                                  CreateTopic, CreateTopicEntry,TopicUpdateView, TopicDeleteView, UserTopicListView)

urlpatterns = [
    path('', views.index, name = 'home-page'),
    path('about/', views.about, name = 'about-page'),
    path('topic/', TopicListView.as_view(), name = 'all-topic'),
    path('topic/<str:username>', UserTopicListView.as_view(), name = 'user-topic'),
    path('topic/<int:pk>/update/', TopicUpdateView.as_view(), name='update-topic'),
    path('topic/<int:pk>/delete/', TopicDeleteView.as_view(), name='delete-topic'),
    path('topic/<int:pk>/', ContentDetailView.as_view(), name = 'all-content'),
    path('topic/new/', CreateTopic.as_view(), name = 'create-topic'),
    path('entry/new', CreateTopicEntry.as_view(), name = 'create-entry'),
    path('topic/<int:pk>/entry/', SinglePageDetailView.as_view(), name = 'details'),
    path('update/<int:pk>', ContentUpdateView.as_view(), name = 'update-content'),
    path('delete/<int:pk>', ContentDeleteView.as_view(), name = 'delete-content'),
    

]



