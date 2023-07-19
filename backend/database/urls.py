from django.conf.urls import url
from database import views

urlpatterns = [
    url(r'^add_node/', views.add_node),
    url(r'^show_nodes/', views.show_nodes),
    url(r'^login_in/', views.login_in),
]
