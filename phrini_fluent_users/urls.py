from django.urls import path
from .views import SignupView, LoginView
from .admin_views import import_words

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("import-words/", import_words, name="import-words"),
]
