from django.conf.urls import url
from.import views

urlpatterns = [
    url(r'^$',views.PostPageView.as_view()),
    url(r'^about/$',views.AboutPageView.as_view() ),
   
]
