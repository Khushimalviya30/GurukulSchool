from django.conf.urls import url
from note.views import g_overview,gallery,contact,career,g_body,amenities,n_board,br_staff,affiliation,career

urlpatterns = [
    url(r'^overview/$',g_overview,name='g_overview'),
    url(r'^g_body/$',g_body,name='body'),
    url(r'^amenities/$',amenities,name='amenities'),
    url(r'^n_board/$',n_board,name='n_board'),
    url(r'^br_staff/$',br_staff,name='br_staff'),
    url(r'^affiliation/$',affiliation,name='affiliation'),
    url(r'^career/$',career,name='career'),
    url(r'^gallery/$',gallery,name='gallery'),
    url(r'^contact/$',contact,name='contact'),
]