from django.conf.urls import url
from database import views

urlpatterns = [
    url(r'^add_node/', views.add_node),
    url(r'^show_nodes/', views.show_nodes),
    url(r'^login_in/', views.login_in),
    url(r'^register/', views.register),
    url(r'^add_relation/', views.add_relation),
    url(r'^read_graph/', views.read_graph),
    url(r'^del_node/', views.del_node),
    url(r'^del_line/', views.del_line),
    url(r'^get_creep_content/', views.get_creep_content),
    url(r'^download_graph/', views.download_graph),
    url(r'^upload_graph/', views.upload_graph),
]
