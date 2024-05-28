# HTTPMixin Class Documentation

## Class: HTTPMixin

A Mixin defined for implementing HTTP-like functionality to classes that inherit from it.

## Methods:

### _handle_response(response)
- A static method for properly handling a given response.
- **Parameters:**
  - `response` (`requests.Response`): The response object to handle.
- **Returns:** `Dict[str, Any]` - A JSON from the response.

### _get(url, headers, params=None)
- Sends a GET request to an endpoint and handles it using `_handle_response` method.
- **Parameters:**
  - `url` (`str`): The full endpoint URL to which request should be made.
  - `headers` (`Dict[str, Any]`): The headers to include in the GET request.
  - `params` (`Optional[Union[Dict[str, Any], bytes]]`): The optional params to include in the request. Defaults to None.
- **Returns:** `Dict[str, Any]` - A JSON from the response.

### _post(url, headers, json_data=None, params=None)
- Sends a POST request to an endpoint and handles it using `_handle_response` method.
- **Parameters:**
  - `url` (`str`): The full endpoint URL to which request should be made.
  - `headers` (`Dict[str, Any]`): The headers to include in the POST request.
  - `json_data` (`Optional[Dict[str, Any]]`): A payload of the request. Defaults to None.
  - `params` (`Optional[Union[Dict[str, Any], bytes]]`): The optional params to include in the request. Defaults to None.
- **Returns:** `Dict[str, Any]` - A JSON from the response.

### _put(url, headers, json_data=None, params=None)
- Sends a PUT request to an endpoint and handles it using `_handle_response` method.
- **Parameters:**
  - `url` (`str`): The full endpoint URL to which request should be made.
  - `headers` (`Dict[str, Any]`): The headers to include in the PUT request.
  - `json_data` (`Optional[Dict[str, Any]]`): A payload of the request. Defaults to None.
  - `params` (`Optional[Union[Dict[str, Any], bytes]]`): The optional params to include in the request. Defaults to None.
- **Returns:** `Dict[str, Any]` - A JSON from the response.

### _delete(url, headers, params=None)
- Sends a DELETE request to an endpoint and handles it using `_handle_response` method.
- **Parameters:**
  - `url` (`str`): The full endpoint URL to which request should be made.
  - `headers` (`Dict[str, Any]`): The headers to include in the DELETE request.
  - `params` (`Optional[Union[Dict[str, Any], bytes]]`): The optional params to include in the request. Defaults to None.
- **Returns:** `Dict[str, Any]` - A JSON from the response.
