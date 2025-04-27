import os
import django


os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='santar4_pr.settings')
django.setup()

from Velmart.models import Rubrick, Goiteens, Spare, Machine
def create_records():

    r1 = Rubrick()
    r1.name = 'Vacuum'
    r1.save()
    print('Rubrick created', r1)

    r2 = Rubrick(title='Cleaner')
    r2.save()
    print('Rubrick created', r2)

    r3 = Rubrick.objects.create(title='THUG')
    print('Rubrick created', r3)


def update_records():
    ru = Rubrick.objects.first()
    if not ru:
        ru = Rubrick(name='Default')
        ru.save()
        print('Rubrick created by default', ru)
        santara, created = Goiteens.objects.get_or_create(title='Title',
                                                          default={'content': 'some content', "price": 10, "rubrick": ru}
                                                          )
        print('Updated', santara.title, santara.content, santara.price, santara.rubrick)

        santara.title = 'New Title'
        santara.content = 'New Content'
        santara.price = 1000
        santara.rubrick = ru
        santara.save()

def get_update_or_create_records():
    rubrick, created = Goiteens.objects.get_or_create(title='Unique rubrick',
    defaults={
        'content': 'default content',
        'price': 100,
        'rubrick': Rubrick.objects.first()
    }
)
    print('Rubrick = ', rubrick.title)

    rubrick_obj, created = Goiteens.objects.update_or_create(
        title='Flowers',
        defaults={
            'title': 'Plants',
            'content': 'updated content',
            'price': 200,
            'rubrick': Rubrick.objects.last()
        }
    )

    print('update_or_create: Rubrick = ', rubrick_obj)


def bulk_operations():

    rubrick, _ = Rubrick.objects.get_or_create(title='Bulk rubrick')

    new_santara = [
        Goiteens(title='Title1', content='Some content', price=10, rubrick=rubrick),
        Goiteens(title='Title2', content='Some content', price=10, rubrick=rubrick),
        Goiteens(title='Title3', content='Some content', price=10, rubrick=rubrick),
        Goiteens(title='Title4', content='Some content', price=10, rubrick=rubrick),
        Goiteens(title='Title5', content='Some content', price=10, rubrick=rubrick),
        Goiteens(title='Title6', content='Some content', price=10, rubrick=rubrick),
    ]
    Goiteens.objects.bulk_create(new_santara)

    santara_list = list(Goiteens.objects.filter(title__startswith='Bulk Title'))

    for san in santara_list:
        san.price += 10

    Goiteens.objects.bulk_update(new_santara, ['price'])
    print('bulk_operations done')

    for san in santara_list:
        print(san.title, 'New price = ', san.price)


def m2m_operations():
    spare1 = Spare.objects.create(name='Bolt')
    spare2 = Spare.objects.create(name='Crew')
    spare3 = Spare.objects.create(name='Hummer')

    machine1 = Machine.objects.create(name='Initial Machine')

    machine1.spares.add(spare1, spare2)

    print('m2m_operations add done', list(machine1.spares.all())),

    machine1.spares.set([spare3, spare2]),
    print('m2m_operations set done', list(machine1.spares.all())),

    machine1.spares.remove(spare2),
    print('m2m_operations remove done', list(machine1.spares.all())),

    machine1.spares.clear(),
    print('m2m_operations clear done', list(machine1.spares.all()))


# if __name__ == '__main__':
#         print(' create operation start'),
#         create_records(),
#
#         print('\n update_records operation start'),
#         update_records(),
#
#         print('\n get_or_create operations start'),
#         get_update_or_create_records(),
#
#         print('\n f bulk operations start'),
#         bulk_operations(),
#
#         print('\n m2m_operations start'),
#         m2m_operations()

rubricks = Rubrick.objects.all()

for rubric in rubricks:
    print(rubric.title, end='\n') 


















