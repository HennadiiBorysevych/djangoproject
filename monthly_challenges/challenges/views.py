from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december"
}

def index(req):
    months = list(monthly_challenges.keys())

    return render(req, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()

    #     redirect_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href='{redirect_path}'>{
    #         capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)





def montly_challenge_by_number(req, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('invalid month')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(req, month):

    # if month == 'january':
    #     challenge_text = 'january'
    # elif month == 'february':
    #     challenge_text = 'february'
    # elif month == 'march':
    #     challenge_text = 'march'
    # elif month == 'april':
    #     challenge_text = 'april'
    # else:
    #     return HttpResponseNotFound('oopp no exist')

    try:
        challenge_text = monthly_challenges[month]

        return render(req, 'challenges/challenge.html', {"text": challenge_text, "title": month})

        # return HttpResponse(response)
    except:
        return HttpResponseNotFound('oopp no exist')
