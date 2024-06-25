The API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on contacts. Each contact is represented by a name, mobile number, and city.

Navigations:-

View Contacts:-
Endpoint: /view/
HTTP Method: GET
Description: Retrieves a list of all contacts stored in the database.

Save Contact:-
Endpoint: /save/
HTTP Method: POST
Description: Creates a new contact with data provided in the request body. Returns the saved contact details upon success.

View Specific Contact:-
Endpoint: /view/<int:id>/
HTTP Method: GET
Description: Retrieves details of a specific contact identified by its id.

Delete Contact:-
Endpoint: /delete/<int:id>/
HTTP Method: DELETE
Description: Deletes a specific contact from the database based on its id.

Update Contact:-
Endpoint: /edit/<int:id>/
HTTP Method: PUT
Description: Updates details of a specific contact identified by its id. Requires data in the request body with updated information.


Technologies Used
Python 3.12
Django Framework
PostgreSQL Database
Django REST Framework
