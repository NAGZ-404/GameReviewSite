from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpRequest

from webapp.models import GameReview
# import datetime
import json

# Create your views here.

#Creates a function that returns the index.html file that displays the title and number of reviews
def index(request: HttpRequest) -> HttpResponse:
    title = "My Video Game Reviews App"

    return render(request, "webapp/index.html", {
        "title": title,
        'n': GameReview.objects.all().count(),
    })

"""Creates an api that specifically manipulates a review with that assigned id 
    and returns the review with the assigned id. 

    If the review does not exist, it returns a 404 error.

    - It has a GET method that returns the review with the assigned id.
    - It has a PUT method that updates the review with the assigned id.
    - It has a DELETE method that deletes the review with the assigned id.
"""
def game_review_api(request: HttpRequest, game_review_id: int) -> JsonResponse:
    game_review = get_object_or_404(GameReview, id=game_review_id)

    #Returns the game review with the assigned id
    if request.method == 'GET':
        return JsonResponse({
            'game_review': game_review.to_dict()
        })

    #Updates the game review's rating of 'liked' or 'disliked' with the assigned id
    if request.method == "PUT":
        request_decode = request.body.decode('utf-8')
        request_json = json.loads(request_decode)
        print(request_json)

        game_review.likedGame = request_json['likedGame']
        game_review.save()
        return JsonResponse({
            'game_review': game_review.to_dict()
        })
    
    #Deletes the game review with the assigned id
    if request.method == "DELETE":
        game_review.delete() 

        return JsonResponse({
            'game_review': game_review.to_dict() 
        })


"""Creates an api that manipulates all reviews
    and returns all the reviews in the database.

    - It has the GET method that returns all the reviews in the database.
    - It has the POST method that creates a new review and adds it to the database.
"""
def game_reviews_api(request):

    #Returns all the exisitng game reviews in the database
    if request.method == 'GET':
        return JsonResponse({
                'game_reviews': [
                    game_review.to_dict() 
                    for game_review in GameReview.objects.all() #Returns all the game reviews in the database
                ]
        })
    
    #Creates a new review with the data from the frontend and added to the database
    if request.method == 'POST':
        request_decode = request.body.decode('utf-8')
        request_json = json.loads(request_decode)
        print(request_json)

        game_review = GameReview.objects.create(
            title=request_json['title'],
            post=request_json['post'],
            likedGame=request_json['likedGame'],

        )
        game_review.save() #Saves the review to database
        return JsonResponse({
            'game_review': game_review.to_dict() #Returns the review to the frontend
        })
     
