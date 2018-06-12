from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
from polls.models import Candidate, Rate, RatingList


def HomeView(request):
    candidates = Candidate.objects.all()

    template = loader.get_template('polls/home.html')
    context = {
        'candidates': candidates,
    }

    return HttpResponse(template.render(context, request))



def HighscoreView(request):
    ratingList = None

    averages = dict()
    candiates = Candidate.objects.all()

    for candiate in candiates:
        try:
            rate = Rate.objects.get(candidate=candiate)
            ratingList = RatingList.objects.filter(rate=rate)

            average = 0
            for rating in ratingList:
                average = average + rating.votes

            average = average / len(ratingList)

            averages[candiate.id] = average
        except:
            averages[candiate.id] = 0


    template = loader.get_template('polls/highscore.html')
    context = {
        'candiates': candiates,
        'averages': averages
    }

    return HttpResponse(template.render(context, request))


def rate(request, candidate_id, rating):
    candiate = Candidate.objects.get(id=candidate_id)

    try:
        rate = Rate.objects.get(candidate=candiate)
    except:
        rate = Rate()
        rate.candidate = candiate
        rate.save()

    ratingList = RatingList()
    ratingList.rate = rate
    ratingList.votes = rating
    ratingList.save()

    return redirect('/polls/home')

def quote(request):
    candidates = Candidate.objects.all()

    template = loader.get_template('polls/home.html')
    context = {
        'quote': quote,}

    return HttpResponse(template.render(context, request))