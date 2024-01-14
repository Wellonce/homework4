import random
from faker import Faker
from bookshop.models import Author, Book, Store, Publisher
from datetime import timedelta

faker = Faker()
def fake_test():
   print(faker.first_name().lower())
   print(faker.date())


def main():
    for  _ in range(25):
        # Store.objects.create(name="faker.company().split()[0]", is_active = random.choice([True, False]))
        #  Author.objects.create_superuser(username = "faker.first_name().lower()", password = faker.ean(length = 13))
        Book.objects.create(name ="faker.first_name_male().lower()" , pages = random.randint(100, 500), 
                            price =random.uniform(4, 35),
                            rating =random.uniform(0, 5), 
                            publisher = Publisher.objects.get(id = random.randint(1, 2)),
                            pubdate = faker.date())
       
       
       
if __name__ == "__main__":
    import os
 
    from django.core.wsgi import get_wsgi_application
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_wsgi_application()
 
    
 
    # main()
    fake_test()