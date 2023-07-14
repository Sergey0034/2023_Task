from django import template

register = template.Library()

censored_words = ['редиска', 'белка', 'панель']

@register.filter()
def censor(value):
    if isinstance(value, str):
        for word in censored_words:
            value = value.replace(word[1:], '*' * (len(word) - 1))
        return value
    else:
        raise ValueError('Цензуруются только строки')
