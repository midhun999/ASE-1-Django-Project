from django.conf.urls import url

from basic_app import views

# TEMPLATE URLS!
app_name = 'basic_app'

urlpatterns = [
    #url(r'^$',views.index,name="index"),
    url(r'^register/$',views.register,name='register'),
    url(r'^ShopKeeper_login/$',views.ShopKeeper_login,name='ShopKeeper_login'),
    url(r'^UserFeedback/$',views.UserFeedback,name='UserFeedback'),
     
]