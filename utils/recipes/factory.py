from random import randint

from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

def make_person():
    return{
        'name': fake.first_name(),
        'icon':{
            'url': 'https://loremflickr.com/320/240',
        }
    }

def make_sector():
    return{
        'title': fake.sentence(nb_words=1),
        'description': fake.sentence(nb_words = 1),
        'image_sector':{
            'url': 'https://loremflickr.com/320/240',
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_person())