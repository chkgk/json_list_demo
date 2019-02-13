from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Minimal working example of storing and retrieving a JSON string.
"""


class Constants(BaseConstants):
    name_in_url = 'json_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # TextFields can contain longer strings than CharFields.
    array_from_javascript = models.TextField()
