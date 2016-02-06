from django.core.urlresolvers import reverse
from django.test import TransactionTestCase, Client
from django.contrib.auth.models import AnonymousUser, User
from groups.models import Group
from groups.views import GroupListView
from students.models import Student

class GroupMethodTest(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")

    def test_create(self):
        response = self.client.get(reverse('groups:index'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username='test', password='test')
        response = self.client.get(reverse('groups:add'))
        self.assertEqual(response.status_code, 200)

        group_test = Group.objects.create(
            name="Group_test"
        )
        self.assertEqual(Group.objects.all().count(), 1)
        self.assertEqual(group_test.amount_person(), 0)

        student_test = Student.objects.create(
            surname='surname_test',
            first_name='first_name_test',
            patronymic='patronymic_test',
            number_card='1111111111',
            date_of_birth='2014-02-02',
            group=group_test
        )

        self.assertEqual(group_test.amount_person(), 1)





