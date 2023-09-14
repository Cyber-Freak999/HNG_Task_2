# RESTful API DOCUMENTATION

This documentation provides information on how to use the API, including details about the available endpoints, request and response formats, and sample usage.

## Table of Contents

- [Endpoints](#endpoints)
  - [Create a Person](#create-a-person)
  - [Get a Person by ID](#get-a-person-by-id)
  - [Update a Person by ID](#update-a-person-by-id)
  - [Delete a Person by ID](#delete-a-person-by-id)
  - [Get a Person by Name](#get-a-person-by-name)
  - [Update a Person by Name](#update-a-person-by-name)
  - [Delete a Person by Name](#delete-a-person-by-name)
  - [Create a Person by Name](#create-a-person-by-name)
- [Request and Response Formats](#request-and-response-formats)
  - [Person Object](#person-object)
  - [Error Response](#error-response)
- [Sample Usage](#sample-usage)
- [Limitations and Assumptions](#limitations-and-assumptions)
- [Local Setup and Deployment](#local-setup-and-deployment)

## Endpoints

### Create a Person

- **Endpoint:** `POST /api/`
- **Description:** Create a new person record.
- **Request Format:**
  - Content-Type: application/json
  - Body:
    ```json
    {
      "name": "John Doe"
    }
    ```
- **Response Format:**
  - Status Code: 201 Created
  - Body:
    ```json
    {
      "message": "Person created successfully",
      "id": 1
    }
    ```

### Get a Person by ID

- **Endpoint:** `GET /api/{id}`
- **Description:** Retrieve a person's details by their ID.
- **Response Format:**
  - Status Code: 200 OK
  - Body (Example):
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Update a Person by ID

- **Endpoint:** `PUT /api/{id}`
- **Description:** Update a person's details by their ID.
- **Request Format:**
  - Content-Type: application/json
  - Body (Example):
    ```json
    {
      "name": "Updated Name"
    }
    ```
- **Response Format:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "message": "Person updated successfully"
    }
    ```

### Delete a Person by ID

- **Endpoint:** `DELETE /api/{id}`
- **Description:** Delete a person's record by their ID.
- **Response Format:**
  - Body:
    ```json
    {
      "message": "Person Deleted successfully"
    }
    ```

### Create a Person by Name

- **Endpoint:** `POST /api/{name}`
- **Description:** Create a new person record by specifying their name.
- **Request Format:**
  - Content-Type: application/json
  - Body (Example):
    ```json
    {
      "name": "John Doe"
    }
    ```
- **Response Format:**
  - Status Code: 201 Created
  - Body:
    ```json
    {
      "message": "Person created successfully",
      "id": "1"
    }
    ```

### Get a Person by Name

- **Endpoint:** `GET /api/{name}`
- **Description:** Retrieve a person's details by their name.
- **Response Format:**
  - Status Code: 200 OK
  - Body (Example):
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

### Update a Person by Name

- **Endpoint:** `PUT /api/{name}`
- **Description:** Update a person's details by their name.
- **Request Format:**
  - Content-Type: application/json
  - Body (Example):
    ```json
    {
      "new_name": "Updated Name"
    }
    ```
- **Response Format:**
  - Status Code: 200 OK
  - Body:
    ```json
    {
      "message": "Person updated successfully"
    }
    ```

### Delete a Person by Name

- **Endpoint:** `DELETE /api/{name}`
- **Description:** Delete a person's record by their name.
- **Response Format:**
  - Body:
  ```json
  {
    "message": "Person deleted successfully"
  }
  ```

## Request and Response Formats

### Person Object

A person object consists of the following fields:

- `id` (integer): The unique identifier for the person.
- `name` (string): The name of the person.

### Error Response

In case of an error, the API returns an error response with the following format:

- Status Code: Appropriate HTTP status code (e.g., 400 Bad Request, 404 Not Found)
- Body (Example):
  ```json
  {
    "message": "Name is required"
  }
  ```

---

This documentation provides an overview of the API's endpoints, request and response formats, and usage examples. For more detailed information, refer to the specific sections above.
