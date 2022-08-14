##### Serialization
###### Creating a Serializer class
###### Using ModelSerializers
###### Writing regular Django views using our Serializer

##### Requests and Responses
###### Request objects
- Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.
`request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.`
###### Response objects
- Response object, which is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.
`return Response(data)  # Renders to content type as requested by the client.
`
###### Status codes
- REST framework provides more explicit identifiers for each status code, eg: HTTP_400_BAD_REQUEST in the status module.
###### Wrapping API views
- REST framework provides two wrappers you can use to write API views.
	- The @api_view decorator for working with function based views.
	- The APIView class for working with class-based views.
- They provide bits of functionality such as receiving `Request` and adding context to `Response`
###### Adding optional format suffixes to our URLs
- Using format suffixes gives us URLs that explicitly refer to a given format, and means our API will be able to handle URLs such as http://example.com/api/items/4.json.
##### Class-based Views
###### Rewriting our API using class-based views
###### Using mixins
###### Using generic class-based views

##### Authentication & Permissions


