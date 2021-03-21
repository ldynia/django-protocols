import math
import random

from django.core.management.base import BaseCommand

from rest.models import Dummy

WEEKDAY = (
    'Monday', 'Tuesday',
    'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
)

MONTH = (
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
)

class Command(BaseCommand):

    help = 'Application seed'

    def add_arguments(self, parser):
        parser.add_argument('db_records', nargs='?', type=int, default=100000)

    def handle(self, *args, **options):
        LIMIT = options['db_records']
        if type(options['db_records']) == list:
            LIMIT = options['db_records'][0]

        print('Start saving data')
        data = []
        for i in range(1, LIMIT+1):
            d = random.randint(1, 31)
            w = random.choice(WEEKDAY)
            m = random.choice(MONTH)
            y = random.randint(1800, 2020)

            data.append(Dummy(pre_seeded=True, day=d, weekday=w, month=m, year=y))

            progress = math.ceil((i/LIMIT) * 100)
            print(f'\rProgress: {progress} %', end='')

        Dummy.objects.bulk_create(data)
        print('\nDone saving data')