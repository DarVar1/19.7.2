from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_create_pet_simple_with_valid_data(name='Юрий', animal_type='пикинес',
                                     age='2'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    if name.isalpha() and animal_type.isalpha() and age.isdigit():
        # Добавляем питомца
        status, result = pf.create_pet_simple(auth_key, name, animal_type, age)

        # Сверяем полученный ответ с ожидаемым результатом
        assert status == 200
        assert result['name'] == name
    else:
        # выкидываем исключение с текстом онеправильности ввода данных
        raise Exception("Неверный формат вводимых данных")

def test_create_pet_simple_with_empty_data_name(name='',animal_type='собака',age='1'):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if name == '':
        print("Пустое поле. Введите 'Имя'")

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_empty_data_animal_type(name='Мурзик',animal_type='',age='1'):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if animal_type == '':
        print("Пустое поле. Введите 'Порода'")

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['animal_type'] == animal_type

def test_create_pet_simple_with_empty_data_age(name='Мурзик',animal_type='кот',age=''):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if age == '':
        print("Пустое поле. Введите 'Возраст'")

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age

def test_create_pet_simple_with_invalid_data_name(name='150',animal_type='собака',age='1'):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if name.isdigit():
        print("Неверный формат ввода поля 'Имя'")
        #name = 'error'

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple_with_invalid_data_animal_type(name='Денис',animal_type='999',age='8'):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if animal_type.isdigit():
        print("Неверный формат ввода поля 'Порода'")
        #animal_type = 'error'

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['animal_type'] == animal_type

def test_create_pet_simple_with_invalid_data_age(name='Володя',animal_type='кот',age='привет'):
    """Проверяем что можно добавить питомца с некорректными данными"""
    if age.isalpha():
        print("Неверный формат ввода поля 'Возраст'")
        #age = 'error'

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['age'] == age

def test_successful_set_photo_pet_jpg(pet_photo = 'images/P1040103.jpg'):
    """Проверяем что можно добавить картинку питомца в формате JPG"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_set_photo_pet(auth_key, my_pets['pets'][2]['id'], pet_photo)

        # Проверяем что статус ответа = 200
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_set_photo_pet_png(pet_photo = 'images/dachshund_PNG43.png'):
    """Баг при попытке добавления картинки питомца с расширением PNG. Статус код 500."""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_set_photo_pet(auth_key, my_pets['pets'][1]['id'], pet_photo)
        print("Status code 500")

        # Проверяем что статус ответа = 500
        assert status == 500
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_set_photo_pet_jpeg(pet_photo = 'images/8335.jpeg'):
    """Проверяем что можно добавить картинку питомца в формате JPEG"""
    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.add_set_photo_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

        # Проверяем что статус ответа = 200 и картинка добавлена
        assert status == 200
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")