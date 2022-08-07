from .models import ProductCategory, ProductTag

def all_categories(request):

    categories = ProductCategory.objects.all()

    return {
        'all_categories': categories
    }

def all_tags(request):

    tags = ProductTag.objects.all()

    return {
        'all_tags': tags
    }