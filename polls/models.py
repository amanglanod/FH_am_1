from django.db import models

# Create your models here.
class Candidate(models.Model):
    candidate_text = models.CharField(max_length=200)
    def __str__(self):
        return self.candidate_text

    photo = models.FileField(upload_to='candidate_photo')
    quote = models.CharField(max_length=200, default='Hello')
    country = models.CharField(max_length=20, default='The World')


class Rate(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    #rate_text = models.CharField(max_length=200)


class RatingList(models.Model):
    votes = models.IntegerField(default=0)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)


