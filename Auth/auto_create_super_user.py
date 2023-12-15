
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


admin_email = 'root5'
password = 'root'



try:

    user_admin = User.objects.filter(email=admin_email)

    def createUser():
        u = User(username=admin_email, email=admin_email, first_name='ROOT', last_name='ROOT')
        u.set_password(password)
        u.is_superuser = True
        u.is_staff = True
        u.save()

    if user_admin.exists():
        print('superuser already exist... ', user_admin.first())
        pass
    else:
        print('creating super user...')
        createUser()

except BaseException as e:
    print(e)
    print('failed creating default user')
