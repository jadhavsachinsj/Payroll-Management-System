from django.conf.urls import url


from . import views
# for image
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'index/', views.home_view, name="home"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
