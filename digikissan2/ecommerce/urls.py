from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path("detection",views.detection,name="detection"),
    path("ecommerce",views.ecommerce,name="ecommerce"),
    path("login_user",views.login_user,name="login_user"),
    path("sign_up",views.sign_up,name='sign_up'),
    path("logout_user",views.logout_user,name="logout_user"),
    path("seller_account",views.seller_account,name="seller_account"),
    path("profile",views.profile,name="profile"),
    path("products",views.products,name="products"),
    path("product_form",views.product_forms,name='product_form'),
    path('product_details/<int:pk>/',views.product_details,name="product_details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)