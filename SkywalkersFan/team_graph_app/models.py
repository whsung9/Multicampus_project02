from pyexpat import model
from django.db import models

# Create your models here.
class score_percentage(models.Model):
    category=models.CharField(max_length=50)
    season=models.CharField(max_length=50)
    score=models.IntegerField()

class roundrank_count_05_18(models.Model):
    rank=models.IntegerField()
    round1=models.IntegerField()
    round2=models.IntegerField()
    round3=models.IntegerField()
    round4=models.IntegerField()
    round5=models.IntegerField()
    round6=models.IntegerField()
    
class roundrank_count_18_22(models.Model):
    rank=models.IntegerField()
    round1=models.IntegerField()
    round2=models.IntegerField()
    round3=models.IntegerField()
    round4=models.IntegerField()
    round5=models.IntegerField()
    round6=models.IntegerField()

class seasonrank(models.Model):
    season=models.CharField(max_length=50)
    score=models.IntegerField()

class clean_sheet(models.Model):
    opposing_team=models.CharField(max_length=50)
    set_score=models.CharField(max_length=50)
    total=models.IntegerField()

class home_away_2021(models.Model):
    opposing_team=models.CharField(max_length=50)
    home_away=models.CharField(max_length=50)
    match_result=models.CharField(max_length=50)
    match_count=models.IntegerField()

class home_away_all(models.Model):
    opposing_team=models.CharField(max_length=50)
    home_away=models.CharField(max_length=50)
    match_result=models.CharField(max_length=50)
    match_count=models.IntegerField()

class relative_record_2021(models.Model):
    opposing_team=models.CharField(max_length=50)
    match_result=models.CharField(max_length=50)
    match_count=models.IntegerField()

class relative_record_all(models.Model):
    opposing_team=models.CharField(max_length=50)
    match_result=models.CharField(max_length=50)
    match_count=models.IntegerField()

class upset(models.Model):
    opposing_team=models.CharField(max_length=50)
    set_score=models.CharField(max_length=50)
    total=models.IntegerField()