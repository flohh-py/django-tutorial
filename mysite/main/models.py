from django.db import models

NAMING_TYPE = [
    ('default', 'Default'),
    ('in', 'In'),
    ('out', 'Out'),
]

class Main(models.Model):
    title = models.CharField(max_length=140)


class NamingSeries(models.Model):
    serie = models.CharField(max_length=10)
    type = models.CharField(choices=NAMING_TYPE, default='default', null=True, max_length=10)
    number = models.IntegerField(max_length=10, default=1)
    fill = models.IntegerField(max_length=1, default=4)

    @classmethod
    def get_series(cls, serie=None, type='default'):
        get_s = cls.objects.get_or_create(serie=serie, type=type)
        s = get_s[0]
        if get_s[1]:
            return str(serie) +' - ' + str(s.number).zfill(s.fill)
        else:
            s.number = int(s.number) + 1
            s.save()
            return str(serie) +' - ' + str(s.number).zfill(s.fill)

