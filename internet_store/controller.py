from django.db.utils import IntegrityError


from internet_store.models import User


def safe_add_new_user(email, user_name):
    user = User(Email=email, UserName=user_name)
    try:
        user.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate user email address' + email}
    return result


def get_all_users():

    return User.objects.all()


def delete_all_users():

    users = User.objects.all()
    users.delete()
