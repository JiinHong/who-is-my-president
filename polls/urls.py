from django.contrib import admin
from django.urls import path, include

import polls
from polls import views
app_name = "polls"
urlpatterns = [
    path('pk', views.index, name='index'),   # 박진홍 투표하기 눌렸을때 나오는 화면 Question Choice
    # ex: /polls/5/

    # path('1', views.nextindex, name = 'nextindex')
    path('<int:question_id>/', views.detail, name='detail'),  ### next Question
# ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/5/results/
    path('results/', views.results, name='results'),



]