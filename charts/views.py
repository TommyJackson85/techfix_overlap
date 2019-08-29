from django.db.models import Q
from django.shortcuts import render
from bugs.models import BugPost
from features.models import FeaturePost

from django.utils import timezone
import pprint, json

import time, datetime

# Create your views here.
"""
gaphs showing how many bugs or features are tended to on a daily, weekly and monthly basis
"""

"""
chunks function
taken from:
https://chrisalbon.com/python/data_wrangling/break_list_into_chunks_of_equal_size/
originally from:
https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
"""
def chunks(l, n):
    """ used to split list of individual dates into sets of 7 or 30. Called from get averages."""
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
        top_five_voted_titles.append(p.title)
        top_five_voted['votes'].append(p.votes)
    top_five_voted['title'] = json.dumps(top_five_voted_titles)
    return top_five_voted

def get_averages(objects, now, all_days, user):
    dates = []
    """first collect dates over specific time periods, in this case , posts progress dates between start time and end time/now"""
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
        
    """sets variables to collect amount of posts worked on per day, week and month"""     
    amount_per_day = []
    amount_per_week = []
    amount_per_month = []
    
    """ secondly sees which dates overlaps with all days( last 3 months ), then adds them to amount per day array"""
    for a in all_days:
        num = 0
        for b in dates:
            if a in b:
                num += 1
                
        amount_per_day.append(num)
    """fourtly, gets the average per day"""
    average_per_day = sum(amount_per_day) / len(amount_per_day)
    
    """splits all days into sets of 7 and 30 to create all weeks and all months data."""
    all_weeks = list(chunks(all_days[::-1], 7))
    all_months = list(chunks(all_days[::-1], 30))
    

    #chunks is global variable above, using array in descending order
    
    """sets weekly summary array for next analysis"""
    weekly_summary = []
    
    """fiftly, calculates weekly summary using a simular process to getting daily summaries"""
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

    """sixthly, calculates monthly summary using a simular process to getting daily summaries"""   
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
    
    """gets overall overages for weekly and monthly summaries"""    
    average_per_week = sum(weekly_summary) / len(weekly_summary)
    average_per_month = sum(monthly_summary) / len(monthly_summary)
    """returns averages rounded down to 2"""    
    return [round(average_per_day, 2), round(average_per_week, 2), round(average_per_month, 2)]

        
        
def get_charts(request):
    """
    Create a view that will returns and renders 'charts.html' template, using the above functions to return the correct data.
    charts.js is used on the charts.html page to generate the charts with data.
    """
    """gets date 3 months ago"""
    three_months_past = datetime.date.today() - datetime.timedelta(3*365/12)
    
    all_days = []
    
    user = request.user
    now = timezone.now()

    d = three_months_past
    """returns all dates from 3 months ago till today"""
    while d <=  datetime.date.today():

        all_days.append(d)
        d += datetime.timedelta(days=1)
    
    #takes bugposts started or finished
    bug_posts_time = BugPost.objects.filter(Q(start_time__gte=three_months_past) | Q(end_time__gte=three_months_past))
    
    
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
        
    #takesfeatureposts started or finished
    feature_posts_time = FeaturePost.objects.filter(Q(start_time__gte=three_months_past) | Q(end_time__gte=three_months_past))
    
    if feature_posts_time:
        #calls the get averages function from above
        feature_post_averages = get_averages(feature_posts_time, now, all_days, user)
    else:
        feature_post_averages = [0, 0, 0]
        
    feature_posts_votes = FeaturePost.objects.all().order_by('-votes')[:5]      
    if feature_posts_votes:
        most_voted_features = get_most_voted(feature_posts_votes)
    else:
        most_voted_features = None
        
    # data.category: ['Bugs', 'Features']
    daily = [bug_post_averages[0], feature_post_averages[0]]
    weekly = [bug_post_averages[1], feature_post_averages[1]]
    monthly = [bug_post_averages[2], feature_post_averages[2]]

    data = {
        'daily': daily,
        'weekly': weekly,
        'monthly': monthly,
        'most_voted_bugs': most_voted_bugs,
        'most_voted_features': most_voted_features,
    }
    
    return render(request, "charts.html", {'user': user, 'data': data})
    
    