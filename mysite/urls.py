
from django.conf.urls import include, url
from django.contrib import admin
from BookDB.views import show, book_details,delete, seach_form
urlpatterns = [
    url(r'^s/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': \
                   'BookDB' }),
    url(r'^booknum/$',show),
    url(r'^book_details/$',book_details),
    url(r'^delete/$',delete),
    url(r'^seach/$',seach),
    url(r'^seach-form/$',seach_form),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^addAuthor/$',addAuthor),
]
