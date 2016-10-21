from django.conf import settings
import requests
import json
APP_ID = settings.FACEBOOK_APP_ID
SECRET_CODE = settings.FACEBOOK_SECRET_CODE

# access_token과 app_access_token은 다릅니다
APP_ACCESS_TOKEN = '{app_id}|{secret_code}'.format(
    app_id=APP_ID,
    secret_code=SECRET_CODE
)


def login(code, request_url):

print('code : %s' % code)

# 받은 'code'값과 client_id, client_secret값을 사용해서 access_token을 얻는다
url_request_access_token = 'https://graph.facebook.com/v2.8/oauth/access_token?' \
                           'client_id={client_id}&' \
                           'redirect_uri={redirect_uri}&' \
                           'client_secret={client_secret}&' \
                           'code={code}'.format(
                                client_id=APP_ID,
                                redirect_uri=REDIRECT_URL,
                                client_secret=SECRET_CODE,
                                code=code
                            )
r = requests.get(url_request_access_token)
dict_access_token = r.json()
# print(json.dumps(dict_access_token, indent=2))
ACCESS_TOKEN = dict_access_token['access_token']
print('ACCESS_TOKEN : %s' % ACCESS_TOKEN)

# 얻어낸 'access_token'의 유효성을 검사하며, 또한 user_id값을 얻어낸다
# 이때, input_token에는 위에서 얻은 'access_token'을 사용하며,
# access_token에는 {app_id}|{secret_code} 형태의 APP_ACCESS_TOKEN을 사용한다
url_debug_token = 'https://graph.facebook.com/debug_token?' \
                  'input_token={it}&' \
                  'access_token={at}'.format(
                        it=ACCESS_TOKEN,
                        at=APP_ACCESS_TOKEN
                    )
r = requests.get(url_debug_token)
dict_debug = r.json()
print(json.dumps(dict_debug, indent=2))
USER_ID = dict_debug['data']['user_id']
print('USER_ID : %s' % USER_ID)

# debug에서 받아온 USER_ID를 이용해서 graph API에 유저 정보를 요청
url_request_user_info = 'https://graph.facebook.com/' \
                        '{user_id}?' \
                        'fields=id,first_name,last_name,gender,picture,email&' \
                        'access_token={access_token}'.format(
                            user_id=USER_ID,
                            access_token=ACCESS_TOKEN
                        )
r = requests.get(url_request_user_info)
dict_user_info = r.json()
print(json.dumps(dict_user_info, indent=2))
