from django.db import models


# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=20)

    def __str__(self):
        return self.state_name


class District(models.Model):
    state = models.ForeignKey(State,
                              on_delete=models.CASCADE)
    dist_name = models.CharField(max_length=25)

    def __str__(self):
        # return self.dist_name+"- "+self.state.state_name
        return self.dist_name
