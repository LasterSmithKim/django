from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"",views.hello,name="hello"),
    url(r"^hello/",views.hello,name="hello"),
    url(r"^index/",views.index,name="index"),
    url(r"^detail/(\d+)/",views.viewsArticle,name="article"),
    url(r"^details/(\d{2})/(\d{4})",views.viewsArticles, name="articles"),
]