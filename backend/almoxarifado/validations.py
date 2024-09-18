from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def custom_validation(data):
    login = data['login'].strip()
    senha = data['password'].strip()
    ##
    ##
    if not senha or len(senha) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not login:
        raise ValidationError('choose another username')
    return data

