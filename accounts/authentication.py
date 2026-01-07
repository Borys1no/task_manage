from rest_framework.authentication import SessionAuthentication

class CsrfExempSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return    