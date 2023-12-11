from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ootdapp.views import home, product, login_user, signup, search

app_name = 'ootdapp'

# urlpatterns = [
#     'static/'] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('login/', login_user, name="login"),
    path('signup/', signup, name="signup"),
    path('search/', search, name="search"),
    path('', home, name="home"),
    path('product/', product, name="product")
]
