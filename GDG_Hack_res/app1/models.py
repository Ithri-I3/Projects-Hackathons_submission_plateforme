from django.db import models


class Challenge(models.Model):
    chall_num=models.IntegerField()
    chall_name=models.CharField(max_length=50)
    chall_desc=models.CharField(max_length=2000)
    def __str__(self):
        return(self.chall_name)

class Submission(models.Model):
    team_name=models.CharField(max_length=50)
    repo_link=models.CharField(max_length=1000)
    design_link=models.CharField(max_length=1000)
    presentation_link=models.CharField(max_length=1000)
    challenge=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    def __str__(self):
        return(self.team_name)


class Judge (models.Model):
    Jfirst_name=models.CharField(max_length=50)
    Jlast_name=models.CharField(max_length=50)
    Jtitle=models.CharField(max_length=50)
    def __str__(self):
        return(self.Jlast_name)


class Critic(models.Model):
    cri_name=models.CharField(max_length=50)
    cri_desc=models.CharField(max_length=2000)
    cri_coef=models.IntegerField()
    cri_judge=models.ForeignKey(Judge,on_delete=models.CASCADE)
    cri_chall=models.ForeignKey(Challenge,on_delete=models.CASCADE)
    def __str__(self):
        return(self.cri_name)


class Review(models.Model):
    note=models.IntegerField()
    submission=models.ForeignKey(Submission,on_delete=models.CASCADE)
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    critic = models.ForeignKey(Critic, on_delete=models.CASCADE)
