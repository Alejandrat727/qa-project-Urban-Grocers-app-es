import auth_token
import configuration
import requests

import create_kit_name_kit_test
import data

## Creación de usuario.
def post_new_user(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json = kit_body,
                        headers=data.headers)

response = post_new_user(data.user_body)
print(response.json())
print(response.status_code)

## Recibir el Token Generado.

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = create_kit_name_kit_test.post_new_user(user_body)
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""
    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = create_kit_name_kit_test.get_users_table()
    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1  # Comprueba si el usuario o usuaria existe y es único/a

## PRUEBA 1.

def test_create_user_1_letter_in_first_name_get_error_response():
    prueba_uno = {
        "name": "a"
    }

## PRUEBA 2.

def test_create_user_511_letter_in_first_name():
    pruebados = (
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
        "AbC"
    )   # Total: 511 caracteres

## PRUEBA 3.

def test_name_empty_should_return_400():
    kit_body = {
        "name": ""
    }

## PRUEBA 4.
def test_name_with_more_than_512_characters_should_return_400():
    prueba_cuatro ={
        "name": "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbc"
                "dAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAb"
                "cdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdA"
                "bcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcd"
                "AbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbc"
                "dAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAb"
                "cdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdA"
                "bcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdAbcdX"
    }

## PRUBA 5.
def test_name_with_special_characters_should_return_201():
    prueba_cinco = {"name": "№%@,."}

## PRUEBA 6.
def test_create_user_has_space_in_first_name_get_error_response( ):
    prueba_seis = {"name": "A aaa"}

## PRUEBA 7.
def test_create_user_has_number_in_first_name_get_error_response():
        prueba_siete = {"name": "123"}

## PRUEBA 8.

def negative_assert_code_400(kit_body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=data.create_kit_header
    )

    print("Código de respuesta:", response.status_code)
    print("Respuesta del servidor:", response.text)

    assert response.status_code == 400

def test_kit_creation_without_name_should_return_400():
    kit_body = {}
    negative_assert_code_400(kit_body)

## PRUEBA 9.

def test_kit_name_as_number_should_return_400():
    kit_body = {"name": 123}
