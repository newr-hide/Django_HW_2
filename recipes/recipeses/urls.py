"""recipeses URL Configuration

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

from django.urls import path

from recipes.calculator.views import recipe_view, home_page_view



urlpatterns = [
    path('',home_page_view, name='home'),
    path('omlet/', recipe_view, name='omlet'),
    path('pasta/', recipe_view, name='pasta'),
    path('buter/', recipe_view),
    # здесь зарегистрируйте вашу view-функцию
]
