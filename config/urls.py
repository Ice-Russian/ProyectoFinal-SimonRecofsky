from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('python/', include('page_base.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('post/', include('profile_post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

