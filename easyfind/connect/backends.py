from django.contrib.auth.backends import ModelBackend


class ConnectPayPalBackend(ModelBackend):
    "Authentication backend for users registered with PayPal OAuth provider."

    def authenticate(self, paypal_id=None):
        "Fetch user for a given provider by id."
        try:
            return User.objects.get(paypal_id=paypal_id)
        except User.DoesNotExist:
            return None