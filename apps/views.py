from django.db.models import Count, Max, Sum, Min, Func, F
from django.db.models.expressions import RawSQL
from django.db.models.functions import Concat
from django.forms import CharField
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.functions import Cast
from apps import models


def view(request):
    # models.Tag.objects.raw()

    from django.db.models import Func, F

    # Hero.objects.annotate(
    #     like_zeus=Func(
    #         F('name'), 'hello', function='levenshtein', template="%(function)s(%(expressions)s, 'Zeus')"
    #     )
    # )

    # models.Tag.objects.order_by('?')
    # models.Tag.objects.update(name=Func(Concat('id', 'name', output_field=CharField()), function='md5'))
    # models.Tag.truncate()
    # models.Tag.objects.annotate(soni=Count('name'))

    return HttpResponse('123')


def levenshtein(name, word):
    pass

users = [
    {'name': 'botirjon'},
    {'name': 'botir'},
    {'name': 'tohir'},
    {'name': 'tohirjon'},
]

for user in users:
    levenshtein(user['name'], 'botir')

