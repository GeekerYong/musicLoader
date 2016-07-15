from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'musicLoader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','musicLoader.views.home'),
    url(r'^song/','musicLoader.views.queSongIndex'),
    url(r'^quesong/','musicLoader.views.queSong'),
    url(r'^music/','musicLoader.views.playMusic'),
    url(r'^admin/', include(admin.site.urls)),
]
