from django.contrib import messages


def validate_password(request, password, confirm_password):
    """ validation for password """
    if password != confirm_password:
        messages.warning(request, 'password did not match')
        return False
    #elif len(password) < 8:
     #   messages.warning(request,
      #      'password must be equal to or grater tha 8 characters')
       # return False
    else:
        return True
