from django.db import models


class Chain(models.Model):
    title = models.CharField(max_length=200)
    starting_date = models.DateField()
    owner = models.ForeignKey('auth.user')

    @property
    def links(self):
        return Link.objects.filter(chain__id=self.id)

    @property
    def current_streak(self):
        # TODO
        pass

    @property
    def record_streak(self):
        # TODO
        pass


class Link(models.Model):
    date = models.DateField()
    chain = models.ForeignKey(Chain)
