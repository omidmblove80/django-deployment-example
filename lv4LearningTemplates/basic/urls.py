from django.conf.urls import url
from basic import views
#setting namespace


app_name = "basic" #name after the app to tell django to look there and find urls


urlpatterns = [
    url(r"relative/" , views.relative, name ="relative"),
    url(r"other/", views.other , name = "other"),

]
