from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView
from .models import FilledQuestionnaire
from .forms import Dropdown
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Count, IntegerField
from django.views.generic.base import RedirectView
from django.db.models.functions import Cast

FilledQuestionnaire.objects

#Should be the Dropdown menu
class CreateDropdownView(CreateView):
    model = FilledQuestionnaire
    form_class = Dropdown
    index_page = 'templates/questionnaire/index.html'
    quesionnaire_page = 'templates/questionnaire/questionnaire.html'
    results_page = 'templates/questionnaire/results.html'

#Index page, shows how many questionnaires have been filled out
def index(request):
    #TODO: make this a real number:
    entry = FilledQuestionnaire.objects.all()
    result_total = 0
    count = 1
    queryset = entry.values("id").annotate(Count = Count('id'))
    for each in queryset:
        result_total += count 
    
    #For the HTML pages
    context = {
        'title': "Basic Questions!",
        'num_answers': result_total,
    }
    return render(request, 'questionnaire/index.html', context)

#Questionnaire page, gives you 2 dropdown menus to choose month and day. Saves to db
def questionnaire(request):
    if request.method =='POST':
        form = Dropdown(request.POST)

        Q = FilledQuestionnaire(month=request.POST['month'], day=request.POST['day'])
        Q.save()
        if form.is_valid():
            return redirect('results.html')
    else:
        form = Dropdown()

        args = {'form': form}
        return render(request, 'questionnaire/questionnaire.html', args)

#Results page, shows you month and day chosen and percentages of each.
def results(request):

    entries = FilledQuestionnaire.objects.all()
    months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    months_fav = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    months_percent = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    days = [0, 0, 0, 0, 0, 0, 0]
    days_percent = [0, 0, 0, 0, 0, 0, 0]
    months_total = 0
    days_total = 0
    #Should look for how many times each month got chosen
    queryset = entries.values("month").annotate(Count = Count('month'))
    for each in queryset:
        month_num = int(each["month"])  - 1
        months[month_num] = each["Count"]
        months_total += each["Count"]
        #print(months_total) 

        #Should calculate most chosen day per month
        fav_day = entries.filter(month = each["month"]).values("day").annotate(Count = Count('day')).order_by("-Count")[0]["day"]
        if fav_day is "1":
            months_fav[month_num] = "Monday"
        elif fav_day is "2":
            months_fav[month_num] = "Tuesday"
        elif fav_day is "3":
            months_fav[month_num] = "Wednesday"
        elif fav_day is "4":
            months_fav[month_num] = "Thursday"
        elif fav_day is "5":
            months_fav[month_num] = "Friday"
        elif fav_day is "6":
            months_fav[month_num] = "Saturday"
        elif fav_day is "7":
            months_fav[month_num] = "Sunday"
        #print(str(fav_day))
  
    #Should look for how many times each day got chosen
    queryset = entries.values("day").annotate(Count = Count('day'))
    for each in queryset:
        day_num = int(each["day"]) - 1
        days[day_num] = each["Count"]
        days_total += each["Count"]

    #Percentage calculators. Something went weird here.
    for idx, m in enumerate(months):
        months_percent[idx] = round((m / months_total) * 100, 3)

    for idx, d in enumerate(days):
        days_percent[idx] = round((d / days_total) * 100, 3) 
    
    #For the HTML pages
    context = {
        'title': "Results!",
        'months': months,
        'days': days,
        'total__month_entries' : months_total,
        'total__days_entries' : days_total, 
        'months_percent' : months_percent,
        'days_percent' : days_percent,
        'fav_day' : fav_day,
        'months_fav' : months_fav,
    }
          
    return render(request, 'questionnaire/results.html', context)


