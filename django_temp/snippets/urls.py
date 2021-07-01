from django.urls import path
from snippets import views

# path('groups/update/<int:pk>', views.GroupsUpdateAPIView.as_view(), name='api_groups_update'),

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    # path('users/', views user_list),
]
