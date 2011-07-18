from django.contrib.gis.db import models
#from django.db import models

class sp0t(models.Model):
    name = models.CharField(max_length=50)
    #geometry = models.PointField(srid=4326)
    geography = models.PointField(geography=True, null=True, blank=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.name, self.geography.x, self.geography.y)
