from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path(r'<int:pk>/rate', login_required(DocUpdate.as_view()), name='rate-doc'),
    path(r'docs/', login_required(DocList.as_view()), name='doc-list'),
    path(r'get-next/', get_next, name='get-next'),
    path(r'export/', login_required(Export), name='export'),
]