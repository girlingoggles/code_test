from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from .models import FilledQuestionnaire
from .forms import Dropdown
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.db.models import Count, When
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

FilledQuestionnaire.objects

class CreateDropdownView(CreateView):
    model = FilledQuestionnaire
    form_class = Dropdown
    index_page = 'templates/questionnaire/index.html'
    quesionnaire_page = 'templates/questionnaire/questionnaire.html'
    results_page = 'templates/questionnaire/results.html'


def index(request):
    #TODO: make this a real number:
    num_answers = 0
    
    #    num_answers += 1
    
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)


def questionnaire(request):
    if request.method =='POST':
        form = Dropdown(request.POST)
        print("in POST")
        print("month" + request.POST['month'])
        print("day" + request.POST['day'])
        #print(form)
        Q = FilledQuestionnaire(month=request.POST['month'], day=request.POST['day'])
        Q.save()
        if form.is_valid():
            return redirect('results.html')
    else:
        form = Dropdown()

        args = {'form': form}
        return render(request, 'questionnaire/questionnaire.html', args)

def results(request):
    entries = FilledQuestionnaire.objects.all()
    
    months = FilledQuestionnaire.objects.values("month").annotate(count = Count('month'))
    print(months)
    days = FilledQuestionnaire.objects.values("day").annotate(count = Count('day'))
    print(days)

    #queryset = entries.annotate(count = Count('month'))
    #for each in queryset:
    #    print("%s: %s" % (each.month, each.count))
    #queryset = entries.annotate(count = Count('day'))
    #for each in queryset:
    #    print("%s: %s" % (each.day, each.count))        
    return render(request, 'questionnaire/results.html')


