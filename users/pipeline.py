import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from users.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'google-oauth2':
        return

    social = user.social_auth.get(provider='google-oauth2')
    api_url = 'https://people.googleapis.com/v1/people/me'
    params = {
        'personFields': 'genders,birthdays',
        'access_token': social.extra_data['access_token']
    }
    response = requests.get(api_url, params)

    if response.status_code != 200:
        return

    data = response.json()

    if data['genders'][0]['value']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data == 'male' else ShopUserProfile.FEMALE

    if data['birthdays'][1]['date']['year']:
        age = timezone.now().date().year - data['birthdays'][1]['date']['year']
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.google.GoogleOAuth2')

    user.save()
