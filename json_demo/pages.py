from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import json

class MyPage(Page):
    form_model = 'player'
    form_fields = ['array_from_javascript']

    def before_next_page(self):
        # let's just demonstrate how to work with the array string in python:
        decoded_array = json.loads(self.player.array_from_javascript)
        print("The complete array is:", decoded_array)
        print("The first element is:", decoded_array[0])

        # we can also change a value and store it as a json string again.
        decoded_array[0] = 'd'
        print("The first element was changed to:", decoded_array[0])
        self.player.array_from_javascript = json.dumps(decoded_array)


class Results(Page):
    pass


page_sequence = [
    MyPage,
    Results
]
