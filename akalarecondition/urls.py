"""akalarecondition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from product.views import home, view_dashboard, view_product, add_incoming, sale_outgoing, ProductDetailView, update_view, add_expenditure, search_product, search_home




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('dashboard/', view_dashboard, name='dashboard'),
    path('product/', view_product, name='product'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug>/update', update_view, name='update'),
    path('add_new/', add_incoming, name='incoming'),
    path('outgoing/', sale_outgoing, name='outgoing'),
    path('addexpenditure/', add_expenditure, name='expenditure'),
    path('dashboard/search/', search_product, name='query_search'),
    path('search/', search_home, name='home_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)