import requests


class HTTPMixin:
  """
  A Mixin defined for implementing HTTP-like
  functionality to classes that inheritate from it
  """

  __slots__ = ()

  @staticmethod
  def _handle_response(response):
    """
    A staticmethod for properly handling given response

    Parameters
    ----------
    response: `requests.Response`
      The response object to handle
    """
    headers = response.headers

    if "Content-Type" not in headers:
      return { "error": "Content-Type is not present in the response", "code": 400 }

    if not headers["Content-Type"].startswith("application/json"):
      return { "error": "Content-Type of the response wasn't application/json", "code": 415 }
    
    return response.json()

  def _get(self, url, headers, params = None):
    """
    A method that sends a GET request to an endpoint
    and handles it using `self._handle_response` method

    Parameters
    ----------
    url: `str`
      The full endpoint url to which request should be made

    headers: `Dict[str, Any]`
      The headers to include in the GET request

    params: `Optional[Union[Dict[str, Any], bytes]]`
      The optional params to include in the request. Defaults to None

    Returns
    -------
    Dict[str, Any]
      A JSON from the response
    """
    response = requests.get(url=url, headers=headers, params=params)
    return self._handle_response(response)
  
  def _post(self, url, headers, json_data = None, params = None):
    """
    A method that sends a POST request to an endpoint
    and handles it using `self._handle_response` method

    Parameters
    ----------
    url: `str`
      The full endpoint url to which request should be made

    headers: `Dict[str, Any]`
      The headers to include in the POST request

    json_data: `Optional[Dict[str, Any]]`
      A payload of the request. Defaults to None

    params: `Optional[Union[Dict[str, Any], bytes]]`
      The optional params to include in the request. Defaults to None

    Returns
    -------
    Dict[str, Any]
      A JSON from the response
    """
    response = requests.post(url=url, headers=headers, json=json_data, params=params)
    return self._handle_response(response)
  
  def _put(self, url, headers, json_data = None, params = None):
    """
    A method that sends a PUT request to an endpoint
    and handles it using `self._handle_response` method

    Parameters
    ----------
    url: `str`
      The full endpoint url to which request should be made

    headers: `Dict[str, Any]`
      The headers to include in the PUT request

    json_data: `Optional[Dict[str, Any]]`
      A payload of the request. Defaults to None

    params: `Optional[Union[Dict[str, Any], bytes]]`
      The optional params to include in the request. Defaults to None

    Returns
    -------
    Dict[str, Any]
      A JSON from the response
    """
    response = requests.put(url=url, headers=headers, json=json_data, params=params)
    return self._handle_response(response)
  
  def _delete(self, url, headers, params = None):
    """
    A method that sends a DELETE request to an endpoint
    and handles it using `self._handle_response` method

    Parameters
    ----------
    url: `str`
      The full endpoint url to which request should be made

    headers: `Dict[str, Any]`
      The headers to include in the DELETE request

    params: `Optional[Union[Dict[str, Any], bytes]]`
      The optional params to include in the request. Defaults to None

    Returns
    -------
    Dict[str, Any]
      A JSON from the response
    """
    response = requests.delete(url=url, headers=headers, params=params)
    return self._handle_response(response)