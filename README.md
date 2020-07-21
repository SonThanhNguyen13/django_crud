# django_crud

### CRUD with Class-Based-View & rest_framework APIView, Response, serializers.ModelSerializer
### Authenticate with rest_framework.permissions import IsAuthenticated
### settings.py:
INSTALLED_APPS = [
	'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.TokenAuthentication'
    ]
}
