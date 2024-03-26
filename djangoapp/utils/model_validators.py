from django.core.exceptions import ValidationError

def velidate_png(img):
    if not img.name.lower().endswith('.png'):
        raise ValidationError('Suporte somente para formato ".PNG"')