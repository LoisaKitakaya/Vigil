def current_user(request):

    user = request.user

    return {
        'current_user': user
    }