__author__ = 'q'

from lolmaps.hawtsp0ts.models import sp0t

with open('data.txt') as f:
    for line in f:
        name, points = line.strip().split(':')
        y, x = points.split(', ')

        geography = 'POINT({x} {y})'.format(x=x,y=y)

        hawt, created = sp0t.objects.get_or_create(name=name, defaults={'geography':geography})

        if created:
            print "ADDED: {0}".format(hawt)
        else:
            print "found: {0}".format(hawt)


