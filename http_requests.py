import requests


def perform_get_request_with_params():
    url = 'https://httpbin.org/get'
    params = {'key': 'value'}
    response = requests.get(url, params=params)
    return response



def perform_get_request_with_params():
    """Perform GET request to given URL sending any parameter and return the response"""
    # HINT: you should add the GET parameters at the end of the url
    url = 'https://httpbin.org/get'
    pass


def perform_post_request():
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.post(url, json=data)
    return response



def perform_put_request():
    """Perform PUT request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    pass


def perform_patch_request():
    """Perform PATCH request to given URL sending given data and return the response"""
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    pass


def perform_delete_request():
    url = 'https://httpbin.org/delete'
    response = requests.delete(url)
    return response



def perform_redirect_request():
    url = 'https://httpbin.org/redirect/1'
    response = requests.get(url, allow_redirects=False)
    return response.headers.get('Location')

