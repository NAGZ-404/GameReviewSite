from django.db import models

"""Creates game review model that has the following fields:
    - title: the title of the game
    - gameReview: the review of the game
    - dateTime: the date and time the review was created
    - likedGame: the rating of the game

    It has the __str__ method that returns the title of the game.
    Also, it has the to_dict method that returns the fields of the game review.

"""
# Create your models here.
class GameReview(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)
    likedGame = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'post': self.post,
            'dateTime': self.dateTime,
            'likedGame': self.likedGame,
        }