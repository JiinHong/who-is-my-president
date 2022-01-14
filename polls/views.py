from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
from django.template import loader


def index(request):
    question = Question.objects.all()
    context = {'question': question}
    return render(request, 'polls/index.html', context)

'''
 context는 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값입니다.
지름길: render()
템플릿에 context 를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법입니다.
따라서 Django는 이런 표현을 쉽게 표현할 수 있도록 단축 기능(shortcuts)을 제공합니다.



'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



'''

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})



get_object_or_404() 함수는 Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
만약 객체가 존재하지 않을 경우, Http404 예외가 발생합니다.


 Question.objects.get(pk=1)
<Question: 박진홍은 진보일까 보수일까>?



'''
t = []

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        tendency = selected_choice.tendency
        t.append(tendency)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        a = Question.objects.count()
        a = int(a)
        if question_id < a:
            i = question_id
            i = int(i)
            i += 1
            nextquestion = Question.objects.get(pk=i)
            context = {'question': nextquestion}
            return render(request, 'polls/detail.html', context)
            #return HttpResponseRedirect(reverse(request, 'polls/detail.html', context))




        else:
            return HttpResponseRedirect(reverse('polls:results'))


            #i = question_id
            #i = int(i)
            # i += 1
            #nextquestion = Question.object.get(pk=i)
            # context = {'question': nextquestion}
            ##  return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

''' a = Question.object.count()
        
if qustion.id < a :
			
i =question.id
i =+ 1
nextquestion = Question.object.get(pk = i)	
context = {'question' : nextquestion}
return render(requset, 'polls/detail.html', context)
'''
def results(request):
    #a = list(Choice.objects.filter(tendency="p"))
    #b = len(a)
    f = t.count("p")
    f = int(f)
    if f > 5:
        t.clear()
        return render(request, 'polls/results.html')
    elif f == 5:
        t.clear()
        return render(request, 'polls/results3.html')
    else:
        t.clear()
        return render(request, 'polls/results2.html')
    #### 여기다가 분류를 해서 창을 띄어야할듯
    ## 진보 = Choice.objects.filter(tendency="p")
    ##    진보갯수 =진보.objects.count()
    ## if 진보갯수 > 5:
    ## return(request, "이재명 창",
    ## else:
    ## return render(request, 윤석열 창
    ##question = get_object_or_404(Question, pk=question_id)




"""
request.POST 는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 객체입니다. 이 경우, request.POST['choice'] 는 선택된 설문의 ID를 문자열로 반환합니다. request.POST 의 값은 항상 문자열들입니다.

Django는 같은 방법으로 GET 자료에 접근하기 위해 request.GET 를 제공합니다 – 그러나 POST 요청을 통해서만 자료가 수정되게하기 위해서, 명시적으로 코드에 request.POST 를 사용하고 있습니다.

만약 POST 자료에 choice 가 없으면, request.POST['choice'] 는 KeyError 가 일어납니다. 위의 코드는 KeyError 를 체크하고, choice가 주어지지 않은 경우에는 에러 메시지와 함께 설문조사 폼을 다시보여줍니다.

설문지의 수가 증가한 이후에, 코드는 일반 HttpResponse 가 아닌 HttpResponseRedirect 를 반환하고, HttpResponseRedirect 는 하나의 인수를 받습니다: 그 인수는 사용자가 재전송될 URL 입니다. (이 경우에 우리가 URL을 어떻게 구성하는지 다음 항목을 보세요).

As the Python comment above points out, you should always return an HttpResponseRedirect after successfully dealing with POST data. This tip isn’t specific to Django; it’s good web development practice in general.

우리는 이 예제에서 HttpResponseRedirect 생성자 안에서 reverse() 함수를 사용하고 있습니다. 이 함수는 뷰 함수에서 URL을 하드코딩하지 않도록 도와줍니다. 제어를 전달하기 원하는 뷰의 이름을, URL패턴의 변수부분을 조합해서 해당 뷰를 가리킵니다. 여기서 우리는 튜토리얼 3장에서 설정했던 URLconf를 사용하였으며, 이 reverse() 호출은 아래와 같은 문자열을 반환할 것입니다.
"""



