from django.db import models


class WeightEntryManager(models.Manager):
    def latest_for_cat(self, cat):
        return self.filter(cat=cat).order_by("-date").first()
