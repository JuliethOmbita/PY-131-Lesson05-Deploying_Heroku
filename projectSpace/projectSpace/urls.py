"""
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from IssLocation import views

urlpatterns = [
    path('', include('IssLocation.urls')),
    path('admin/', admin.site.urls),
]
