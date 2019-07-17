from django.db.models import Q
from django.shortcuts import render
from bugs.models import BugPost
from django.utils import timezone
import pprint, json

import time, datetime

# Create your views here.
"""
gaphs showing how many bugs or features are tended to on a daily, weekly and monthly basis
"""
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def get_most_voted(objects):
    top_five_voted = {
        'votes': []    
    }
    top_five_voted_titles = []
    for p in objects:
        if len(p.title) > 8:
            top_five_voted_titles.append(p.title)
        else:
            top_five_voted_titles.append(p.title)
        top_five_voted['votes'].append(p.votes)
    top_five_voted['title'] = json.dumps(top_five_voted_titles)
    print('top_five_voted[titles]')
    print(top_five_voted['title'][0])
    return top_five_voted

def get_averages(objects, now, all_days, user):
    dates = []
    for p in objects:
        if p.end_time is None:
            delta = now - p.start_time
        else:
            delta = p.end_time - p.start_time
            
        object_dates=[]
        for i in range(delta.days + 1):
            each = p.start_time + datetime.timedelta(days=i)
            object_dates.append(each.date())
        dates.append(object_dates)
            
    amount_per_day = []
    amount_per_week = []
    amount_per_month = []
    
    for a in all_days:
        num = 0
        for b in dates:
            if a in b:
                num += 1
                
        amount_per_day.append(num)
    average_per_day = sum(amount_per_day) / len(amount_per_day)
            
    all_weeks = list(chunks(all_days[::-1], 7))
    all_months = list(chunks(all_days[::-1], 30))
    #chunks is global variable above, using array in descending order
    #per_week_day_averages = list(chunks(amount_per_day[::-1], 7))
    #per_month_day_averages = list(chunks(amount_per_day[::-1], 30))
    #print(all_weeks)
    #print(all_months)
        
    weekly_summary = []
    for w in all_weeks:
        if len(w) == 7:
            num = 0
            for d in dates:
                for a in w:
                    if a in d:
                        num += 1
                        break
                
            amount_per_week.append(num)
    weekly_summary.append(sum(amount_per_week) / len(amount_per_week))
        #weekly_summary.append(sum(w) / len(w))
    print('weekly_summary')
    print(weekly_summary)
   
    monthly_summary = []
    for m in all_months:
        if len(m) == 30:
            num = 0
            for d in dates:
                for a in m:
                    if a in d:
                        num += 1
                        break
                        
            amount_per_month.append(num)
    monthly_summary.append(sum(amount_per_month) / len(amount_per_month))
    #weekly_summary.append(sum(w) / len(w))
    print('monthly_summary')
    print(monthly_summary)
        
        
    average_per_week = sum(weekly_summary) / len(weekly_summary)
    average_per_month = sum(monthly_summary) / len(monthly_summary)
    
    return [round(average_per_day, 2), round(average_per_week, 2), round(average_per_month, 2)]
        
        #return "nonsense"
def get_charts(request):
    """
    Create a view that will return a list
    of Bug Posts that were published prior to 'now'
    and render them to the 'bugposts.html' template
    """

    three_months_past = datetime.date.today() - datetime.timedelta(3*365/12)
    all_days = []
    user = request.user
    now = timezone.now()

    d = three_months_past
    while d <=  datetime.date.today():

        all_days.append(d)
        d += datetime.timedelta(days=1)
    
    #takes bugposts started or finished
    bug_posts_time = BugPost.objects.filter(Q(start_time__gte=three_months_past) | Q(end_time__gte=three_months_past))
    #takes bugposts started or finished
    
    if bug_posts_time:
        #calls the get averages function from above
        bug_post_averages = get_averages(bug_posts_time, now, all_days, user)
    else:
        bug_post_averages = [0, 0, 0]
    bug_posts_votes = BugPost.objects.all().order_by('-votes')[:5]      
    if bug_posts_votes:
        most_voted_bugs = get_most_voted(bug_posts_votes)
    else:
        most_voted_bugs = None
        
    # data.category: ['Bugs', 'Features']
    daily = [bug_post_averages[0], 3]
    weekly = [bug_post_averages[1], 3]
    monthly = [bug_post_averages[2], 4]

    data = {
        'daily': daily,
        'weekly': weekly,
        'monthly': monthly,
        'most_voted_bugs': most_voted_bugs,
    }
    
    return render(request, "charts.html", {'user': user, 'data': data})
    
    