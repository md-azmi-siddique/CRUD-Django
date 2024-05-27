from django.urls import path
from . views import *

urlpatterns = [
    path("create/", crudCreate.as_view(), name="create"),
    path("read/", crudRead.as_view(), name="Read"),
    path("update/<int:pk>/", crudUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", crudDelete.as_view(), name="read")
]
