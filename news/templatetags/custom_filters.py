from django import template
from datetime import datetime

register = template.Library()

WORDS = ['редиска', 'дурак', 'идиот', 'придурок']


@register.filter()
def censor(text):
    for i in WORDS:
        text = text.replace(i[1:], '*' * len(i[1:]))
    return text




