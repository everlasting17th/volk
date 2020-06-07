from datetime import date
import random

def get_persistent_hash(s):
    ord3 = lambda x : '%.3d' % ord(x)
    return int(''.join(map(ord3, s)))

def get_rand_seed():
    return get_persistent_hash(date.today().strftime("%Y-%m-%d"))

def setup_random():
    random.seed(get_rand_seed())


descriptions = [
    "Волк вырос на {}% относительно {} но {}",
    "Уверенный отрицательный рост волка составил {}% относительно {} но {}",
    "Волк знает свое дело на {}% особенно относительно {} но {}",
    "Волк конечно на {}% слабее {} но {}",
    "Волк уверенным маршем пробежал {}% относительно {} но {}"
]

currencies = [
    "вашей мамаши",
    "завидности",
    "варения",
    "анимедевок",
    "волка",
    "клея",
    "глютена",
    "донга",
    "цирка",
    "льва",
    "тигра",
    "молока",
    "волка",
    "денег",
    "неважно кого",
    "зубов"
]

afterwords = [
    "в цирке не выступает",
    "продолжает пятиться",
    "продолжает уверенный рос!",
    "волк.",
    "волк волку волк",
    "слишком хорош",
    "из гатчины",
    "и все тут",
    "все еще слабее льва и тигра",
    "друг познается в беде, но волк волк",
    "не враг, а так",
    "Аска лучшая девочка Европы",
    "волк все-таки бесценен",
    "любят тихо, громко только пердят",
    "узнали, согласны?",
    "кушать хочется, возьмите в цирк пожалуйта",
    "тигр не волк",
    "запомни",
    "лучше быть последним-первым чем первым-последним"
]

class currency_data:
    def __init__(self):
        self.amount = 0.0
        self.desc = ""

    def generate_random_fields(self):
        self.amount = random.uniform(-500, 500)


        self.desc = descriptions[ random.randint(0, len(descriptions) - 1)].format(
            self.amount, 
            currencies[random.randint(0, len(currencies) - 1)], 
            afterwords[random.randint(0, len(afterwords) - 1)]
        );

def get_currency_report():
    setup_random();
    data = currency_data();
    data.generate_random_fields();
    return data;