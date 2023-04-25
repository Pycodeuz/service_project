from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    def tests_number_of_queries(self):
        User.objects.create(username='testuser1', first_name='Test', last_name='user1')
        # Above ORM create will run only one query.
        self.assertNumQueries(1)
        User.objects.filter(username='testuser').update(username='test1user')
        # One more query added.
        self.assertNumQueries(2)
        User.objects.all()
        self.assertNumQueries(3)


'''
user<-car

'''