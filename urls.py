from django.urls import include,path,re_path
from django.contrib.auth.views import PasswordResetConfirmView
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.DefaultRouter(trailing_slash = False)
router.register(r'rawtang', views.RawtangViewSet, basename="rawtang")
router.register(r'rawramp', views.RawrampViewSet, basename="rawramp")
router.register(r'rawkes', views.RawkesViewSet, basename="rawkes")

app_name = "app"
urlpatterns = [
	path("", views.index, name="index"),
	path("register/", views.user_register, name="register"),
	path("data_entry/", views.data_entry, name="data"),
	path("login/", views.user_login, name="login"),
	path("logout/", views.user_logout, name= "logout"),
	path("reset/", views.user_reset_pwd, name= "reset"),
	path("reset_confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="rafflesia/password_reset_confirm.html"), name= "reset_confirm"),
	re_path(r'^datatable/(?P<table_name>\w+)/$',views.render_table,name='table'),
	re_path(r'^serverside/(?P<table_name>\w+)/(?P<filtering>\w+)/$',views.ServersideView.as_view(),name='serverside'),
	re_path(r'^download/(?P<table_name>\w+)/$',views.download,name='download'),
	path("sedar/", views.get_sedar, name="sedar"),
	path("geotagging/", views.post_geotag, name="geotag"),
	path("api-token-auth/", authviews.obtain_auth_token, name="token"),
	path("api/", include(router.urls)),
	path("send-notification-email/",views.send_notification_email, name="send_notification_email"),
	path("handle-coordinates/",views.handle_coordinates, name="handle_coordinates"),
	path('chartraw/', views.ChartRawList.as_view(), name="chartrawlist"),
	path('chartraw/<int:pk>', views.ChartRawDetail.as_view(), name="chartrawdetail"),
]