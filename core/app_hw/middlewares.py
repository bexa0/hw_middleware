from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Class middleware')
        response = self.get_response(request)

        return response


class UserGroupsMiddleware(MiddlewareMixin):
    def process_template_response(self, request, response):
        if request.user.is_authenticated:
            response.context_data['user_groups'] = list(request.user.groups.values_list('name', flat=True))
        return response
