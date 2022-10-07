from django.core.exceptions import ValidationError

def validar_cantidad(cantidad):
    if cantidad <1:
        raise ValidationError(
            '%(cantidad)s no es una cantidad válida',
            params={'cantidad': cantidad}
        )
def validar_longitudnombre(nombre):
    if len(nombre)<3:
        raise ValidationError(
            '%(nombre)s no tiene la longitud válida ',
            params={'nombre': nombre}
        )
def validar_precio(precio):
    if precio <=0:
        raise ValidationError(
            '%(precio)s no es un precio válido',
            params={'precio': precio}
        )
def validar_descuento(descuento):
    if descuento <0 or descuento>40:
        raise ValidationError(
            '%(descuento)s no es un porcentaje de descuento válido',
            params={'descuento': descuento}
        )