from django.core.management.base import BaseCommand, CommandError
from groups.models import Group
from students.models import Student


class Command(BaseCommand):
    help = 'list of students by group'

    def handle(self, *args, **options):
        for group in Group.objects.all():
            self.stdout.write(self.style.SUCCESS(u'Group {0}'.format(group.name)))
            if Student.objects.filter(group_id=group.id):
                for student in Student.objects.filter(group_id=group.id):
                    self.stdout.write(self.style.SUCCESS(u'  {0}'.format(student.full_name())))
            else:
                self.stdout.write(self.style.SUCCESS(u'  No student'))
