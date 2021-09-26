"""Rest framework utils"""
from rest_framework.response import Response
from rest_framework import status

def return_not_found():
    """Rest method for 404, not found"""
    return Response(
        {
            'ok': False,
            'error': 'registo não encontrado'
        },
        status=status.HTTP_404_NOT_FOUND
    )


def error_response(error, status_=status.HTTP_400_BAD_REQUEST):
    """Rest method for 400, bad request"""
    return Response(
        {
            'ok': False,
            'error': error
        },
        status=status_ or status.HTTP_400_BAD_REQUEST
    )


def return_method_not_accepted(status_=status.HTTP_405_METHOD_NOT_ALLOWED):
    """Rest method for 405, method not accepted"""
    return Response(
        {
            'ok': False,
            'error': 'METHOD NOT ALLOWED'
        },
        status=status_ or status.HTTP_405_METHOD_NOT_ALLOWED
    )


def success_response(data={}, status_=status.HTTP_200_OK):
    """Rest method for 200, success response"""
    return Response(
        {
            'ok': True,
            'data': data
        },
        status=status_
    )
