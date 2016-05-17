from django.db.utils import IntegrityError


from internet_store.models import User, Courier


def get_all_users():
    users = User.objects.all()
    modified_users = []
    for u in users:
        modified_user = {'Email': u.Email, 'UserName': u.UserName}
        modified_users.append(modified_user)
    return modified_users


def safe_add_new_user(email, user_name):
    user = User(Email=email, UserName=user_name)
    try:
        user.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate user email address: ' + email}
    return result


def delete_user(email):
    user = User.objects.get(Email=email)
    user.delete()
    result = {'Success': True}
    return result


def get_all_couriers():
    couriers = Courier.objects.all()
    modified_couriers = []
    for c in couriers:
        modified_courier = {'CourierName': c.CourierName}
        modified_couriers.append(modified_courier)
    return modified_couriers


def safe_add_new_courier(courier_name, user_email):
    user_id = User.objects.get(Email=user_email)
    courier = Courier(CourierName=courier_name, UserId=user_id)
    try:
        courier.save()
        result = {'Success': True}
    except IntegrityError:
        result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    return result


def delete_courier(courier_name):
    courier = Courier.objects.get(CourierName=courier_name)
    courier.delete()
    result = {'Success': True}
    return result


def get_all_product_types():
    # couriers = Courier.objects.all()
    # modified_couriers = []
    # for c in couriers:
    #     modified_courier = {'CourierName': c.CourierName}
    #     modified_couriers.append(modified_courier)
    # return modified_couriers
    pass


def safe_add_new_product_type(product_type):
    # user_id = User.objects.get(Email=user_email)
    # courier = Courier(CourierName=courier_name, UserId=user_id)
    # try:
    #     courier.save()
    #     result = {'Success': True}
    # except IntegrityError:
    #     result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    # return result
    pass


def delete_product_type(product_type):
    # courier = Courier.objects.get(CourierName=courier_name)
    # courier.delete()
    # result = {'Success': True}
    # return result
    pass


def get_all_products():
    # couriers = Courier.objects.all()
    # modified_couriers = []
    # for c in couriers:
    #     modified_courier = {'CourierName': c.CourierName}
    #     modified_couriers.append(modified_courier)
    # return modified_couriers
    pass


def safe_add_new_product(product, product_type):
    # user_id = User.objects.get(Email=user_email)
    # courier = Courier(CourierName=courier_name, UserId=user_id)
    # try:
    #     courier.save()
    #     result = {'Success': True}
    # except IntegrityError:
    #     result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    # return result
    pass


def delete_product(product):
    # courier = Courier.objects.get(CourierName=courier_name)
    # courier.delete()
    # result = {'Success': True}
    # return result
    pass


def get_all_marketing_sources():
    # couriers = Courier.objects.all()
    # modified_couriers = []
    # for c in couriers:
    #     modified_courier = {'CourierName': c.CourierName}
    #     modified_couriers.append(modified_courier)
    # return modified_couriers
    pass


def safe_add_new_marketing_source(marketing_source):
    # user_id = User.objects.get(Email=user_email)
    # courier = Courier(CourierName=courier_name, UserId=user_id)
    # try:
    #     courier.save()
    #     result = {'Success': True}
    # except IntegrityError:
    #     result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    # return result
    pass


def delete_marketing_source(marketing_source):
    # courier = Courier.objects.get(CourierName=courier_name)
    # courier.delete()
    # result = {'Success': True}
    # return result
    pass


def get_all_regions():
    # couriers = Courier.objects.all()
    # modified_couriers = []
    # for c in couriers:
    #     modified_courier = {'CourierName': c.CourierName}
    #     modified_couriers.append(modified_courier)
    # return modified_couriers
    pass


def safe_add_new_region(region):
    # user_id = User.objects.get(Email=user_email)
    # courier = Courier(CourierName=courier_name, UserId=user_id)
    # try:
    #     courier.save()
    #     result = {'Success': True}
    # except IntegrityError:
    #     result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    # return result
    pass


def delete_region(region):
    # courier = Courier.objects.get(CourierName=courier_name)
    # courier.delete()
    # result = {'Success': True}
    # return result
    pass


def get_all_streets():
    # couriers = Courier.objects.all()
    # modified_couriers = []
    # for c in couriers:
    #     modified_courier = {'CourierName': c.CourierName}
    #     modified_couriers.append(modified_courier)
    # return modified_couriers
    pass


def safe_add_new_street(street, region):
    # user_id = User.objects.get(Email=user_email)
    # courier = Courier(CourierName=courier_name, UserId=user_id)
    # try:
    #     courier.save()
    #     result = {'Success': True}
    # except IntegrityError:
    #     result = {'Success': False, 'Message': 'Duplicate courier name: ' + courier_name}
    # return result
    pass


def delete_street(street):
    # courier = Courier.objects.get(CourierName=courier_name)
    # courier.delete()
    # result = {'Success': True}
    # return result
    pass