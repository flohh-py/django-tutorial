from django.core.management.base import BaseCommand
from product.models import Product
import faker
import random


PRODUCTS = [
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "Shoes",
    "Trainers",
    "Boots",
    "Dress",
    "T-shirt",
    "Clothes",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "PoloShirt",
    "Beauty",
    "Lighting",
]

class Provider(faker.providers.BaseProvider):
    def products(self):
        return self.random_element(PRODUCTS)

class Command(BaseCommand):
    help = "Create some test products"

    def handle(self, *args, **options):
        fake = faker.Faker()
        fake.add_provider(Provider)

        for _ in range(20):
            prod = {
                'code' : 'Product '+ str(fake.products()),
                'type' : 'stock',
                'descrip' : fake.text(max_nb_chars=20),
                'price': round(random.uniform(100.99, 200.99), 2),
                'cost': round(random.uniform(10.99, 50.99), 2),
                'qty': random.randint(10,40),
            }
            Product.objects.create(**prod)
        
