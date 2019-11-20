from rest_framework.routers import DefaultRouter
from django.conf.urls import include,url
from .views import notes_noteViewSet
router =DefaultRouter()
router.register('notes-note',notes_noteViewSet,base_name='notes_note')
urlpatterns=[
    url('',include(router.urls))
]