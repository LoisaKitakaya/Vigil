from django.urls import path, include
from django.contrib import admin
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # graphql endpoint for analytics
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    # page urls
    path('', include('core.urls')),
]

admin.site.site_header = 'Vigil Admin Panel'
admin.site.site_title = 'Vigil Surveillance company website, API Backend & Headless CMS'
