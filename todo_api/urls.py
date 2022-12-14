from django.urls import path,include
from .views import (
    ExampleViews,
    RegisterUserupdateAPIView,
    TodoListApiView,
    TodoDetailApiView,
    ExampleView,
    CustomAuthToken,
    RegisterAPI,
    LoginAPI,
    UserCountView,
    UserViewSet,
)
from todo_api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippet', views.SnippetViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'brand', views.BrandViewSet)

urlpatterns = [

    #path('', views.api_root),

    #login
    path('api/login/', LoginAPI.as_view()),
   
    #register
    path('register/',RegisterAPI.as_view()),
    path('register/<int:pk>/',RegisterUserupdateAPIView.as_view()),

    #token 
    path('auth', ExampleView.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),

    #userlist and detail
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    #path('users-list/', views.UserLists.as_view()),

    #snippets(class-based-view)
    path('snippetslist/', views.SnippetList.as_view()),
    path('snippetslist/<int:pk>/', views.SnippetDetail.as_view()),
    path('snippetslist/<int:pk>/highlight/', views.SnippetHighlight.as_view()),

    #snippets(function-based-view)
    path('snippets-list/', views.snippet_list, name='snippet-list'),
    path('snippets-list/<int:pk>/', views.snippet_detail, name='snippet-detail'),

    #todo
    path('Todolist/', TodoListApiView.as_view()),
    path('Todolist/<int:todo_id>/', TodoDetailApiView.as_view()),
    
    #router
    path('router/', include(router.urls)),

    #product
    path('Productlist/', views.ProductList.as_view()),
    path('Productlist/<int:pk>/', views.ProductDetail.as_view(),name='product-detail'),

    #brand
    path('Brandlist/', views.BrandList.as_view()),
    path('Brandlist/<int:pk>/', views.BrandDetail.as_view(),name='brand-detail'),

    #parser and render
    path('parser/', ExampleViews.as_view()),
    path('render/', UserCountView.as_view()),
    path('static-html-render/',views.simple_html_view),

    #path('filter/', views.CustomSearchFilter),
]

