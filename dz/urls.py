"""lab6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Journal import views

urlpatterns = [
    path('', views.main),
    path('admin/', admin.site.urls),
    path('our_authors/', views.our_authors),
    path('archive/', views.archive),
    path('auth/author/<int:id>', views.newarticle, name='author_url'),
    path('auth/glvrd/', views.glvrd, name='glvrd_url'),
    path('auth/', views.auth),
    path('articles/<int:id>/', views.GetArticle, name='article_url'),
    path('our_authors/authorz/<int:id>/', views.GetAuthor, name='authorz_url'),
    path('auth/glvrd/release/<int:id>', views.relez, name='release_url'),
    path(('auth/glvrd/new/'), views.create, name='create_url'),
    path(('auth/glvrd/createnewauthor/'), views.createauthor, name='createauthor_url'),
]
