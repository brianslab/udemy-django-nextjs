from rest_framework.views import exception_handler as restfw_exception_handler


def exception_handler(exc, context):

    response = restfw_exception_handler(exc, context)

    exception_class = exc.__class__.__name__

    print('Encountered exception. exception_class:', exception_class)

    if exception_class == 'AuthenticationFailed':
        response.data = {
            "error": "Invalid username or password. Please try again."
        }

    if exception_class == 'NotAuthenticated':
        response.data = {
            "error": "Login first to access this resource."
        }

    if exception_class == 'InvalidToken':
        response.data = {
            "error": "Your authentication token has expired. Please login again."
        }

    return response
