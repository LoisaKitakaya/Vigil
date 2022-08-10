from django.urls import path, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # page urls
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('accounts/', include('users.urls')),
    path('checkout/', include('orders.urls')),
    path('products/', include('products.urls')),

    # graphql endpoint for analytics
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

admin.site.site_header = 'Vigil Admin Panel'
admin.site.site_title = 'Vigil Surveillance company website, API Backend & Headless CMS'
