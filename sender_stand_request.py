import configuration
import requests
import data 

# Создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Получение токена для пользователя
def get_token(response):
    return response.json()["authToken"]

# Создание набора для пользователя
def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": "Bearer " + auth_token
    }

    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )

