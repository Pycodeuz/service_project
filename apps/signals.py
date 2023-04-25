# from django.db.models import F
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# from apps.models import Hero, Category, Villain
#
#
# @receiver(pre_save, sender=Hero, dispatch_uid="update_hero_count")
# def update_hero_count(sender, **kwargs):
#     hero = kwargs['instance']
#     if not hero.pk:
#         Category.objects.filter(pk=hero.category_id).update(hero_count=F('hero_count') + 1)
#
#
# @receiver(pre_save, sender=Villain, dispatch_uid="update_villain_count")
# def update_villain_count(sender, **kwargs):
#     villain = kwargs['instance']
#     if not villain.pk:
#         Category.objects.filter(pk=villain.category_id).update(villain_count=F('villain_count') + 1)
