from oauth2_provider.signals import app_authorized

def handle_app_authorized(sender, request, token, **kwargs):
    print('App {} was authorized'.format(token.application.name))

app_authorized.connect(handle_app_authorized)