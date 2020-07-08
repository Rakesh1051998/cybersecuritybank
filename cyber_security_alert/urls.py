"""cyber_security_alert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from cyber_alert import views as alert_view
from admins import views as admin_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', alert_view.admin_login, name="admin_login"),
    url(r'^admin_register/$', alert_view.admin_register, name="admin_registe"),
    url(r'^giver_transaction/$', alert_view.giver_transaction, name="giver_transaction"),
    url(r'^analyze_page/$', alert_view.analyze_page, name="analyze_page"),
    url(r'^viewer/(?P<chart_type>\w+)', alert_view.viewer, name="viewer"),
    url(r'^update/$', alert_view.update, name="update"),
    url(r'^logout_page/$', alert_view.logout_page, name="logout_page"),
    url(r'^mydetails/$', alert_view.mydetails, name="mydetails"),
    url(r'^show/$', alert_view.show, name="show"),
    url(r'^receivealert/$', alert_view.receivealert, name="receivealert"),


    url(r'^admins/admin_page/$', admin_view.admin_page, name="admin_page"),
    url(r'^admins/analyze/$', admin_view.analyze, name="analyze"),
    url(r'^admins/adlogout/$', admin_view.adlogout, name="adlogout"),
    url(r'^admins/charts/(?P<chart_type>\w+)', admin_view.charts,name="charts"),
    url(r'^admins/riskuser/$',admin_view.riskuser, name="riskuser"),
    url(r'^admins/riskalert/(?P<tuser>\d+)$',admin_view.riskalert, name="riskalert"),


]
