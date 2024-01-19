# import random
# from faker import Faker
# from bookshop.models import Author, Book, Store, Publisher
# from datetime import timedelta

# faker = Faker()
# def fake_test():
#    print(faker.first_name().lower())
#    print(faker.date())


# def main():
#     for  _ in range(25):
#         # Store.objects.create(name="faker.company().split()[0]", is_active = random.choice([True, False]))
#         #  Author.objects.create_superuser(username = "faker.first_name().lower()", password = faker.ean(length = 13))
#         Book.objects.create(name ="faker.first_name_male().lower()" , pages = random.randint(100, 500), 
#                             price =random.uniform(4, 35),
#                             rating =random.uniform(0, 5), 
#                             publisher = Publisher.objects.get(id = random.randint(1, 2)),
#                             pubdate = faker.date())
       
       
       
# if __name__ == "__main__":
#     import os
 
#     from django.core.wsgi import get_wsgi_application
 
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
#     application = get_wsgi_application()
 
    
 
#     # main()
#     fake_test()




# from django.core.management.base import BaseCommand

# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university.settings')
# from django.core.wsgi import get_wsgi_application

# class Command(BaseCommand):
#     help = 'Generate fake data for models'

    # def handle(self, *args, **options):



def main():
    for _ in range(100):
        teacher = Teacher.objects.create(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        degree=faker.random_element(elements=('master', 'bachelor', 'academic', 'drscience', 'phs')),
        age=faker.random_int(min=25, max=65),
        email=faker.email(),
        )

        speciality = Speciality.objects.create(
        name=faker.job(),
        code=faker.uuid4(),
        is_active=faker.boolean(),
        start_date=faker.date_between(start_date='-5y', end_date='today'),
        slug=faker.slug(),
        )

        subject = Subject.objects.create(
        name=faker.catch_phrase(),
        teacher=teacher,
        )
        subject.speciality.add(speciality)

    if __name__ == "__main__":
        import os


    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university.settings')
    from django.core.wsgi import get_wsgi_application
    
    import os
    from faker import Faker

    from courses.models import Subject, Teacher, Speciality
    faker = Faker()
    main()

