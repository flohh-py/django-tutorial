from django.core.management.base import BaseCommand
from partner.models import Partner
import faker

class Command(BaseCommand):
    help = "Create some test partners"

    def handle(self, *args, **options):
        fake = faker.Faker()

        for _ in range(5):
            customer = {
                'name': fake.name(),
                'type': 'customer',
                'address': fake.address()

            }
            Partner.objects.create(**customer)

            supplier = {
                'name': fake.name(),
                'type': 'supplier',
                'address': fake.address()

            }
            Partner.objects.create(**supplier)
        
