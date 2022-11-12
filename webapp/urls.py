from django.urls import path

from webapp.views import index, game_reviews_api, game_review_api


urlpatterns = [
    path('', index),
    path('api/game_reviews/', game_reviews_api),
    path('api/game_reviews/<int:game_review_id>/', game_review_api),
]

