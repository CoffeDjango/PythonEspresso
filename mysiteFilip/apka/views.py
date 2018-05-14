from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.shortcuts import render ,get_object_or_404



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):

    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'apka/detail.html', {'question': question})
