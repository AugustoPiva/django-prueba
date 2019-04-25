from django import template
register = template.Library()

# esto es un decorator
@register.filter

# escribir la funcion que va a hacer el filtro personalizado nuestro

# lo que te hace esta funcion es:
# del template tag que vos le das
# {{ text|cut:"hello" }}
# el texto suponete que es "hello world"
# te imprime solo world

def cutout(value, arg):
    return value.replace(arg, '')
