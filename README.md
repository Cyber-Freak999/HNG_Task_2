# A RESTful API with Basic CRUD Operations

This is a RESTFul API for displaying data from a SQLlite database. It supports URL parameters, for which the API will query the database and retrieve results. It's endpoints support GET, POST, PUT and DELETE requests on all database items.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Sample Requests and Responses](#sample-requests-and-responses)
- [Documentation](#documentation)

## Getting Started

### Prerequisites

- Python 3.11

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/Cyber-Freak999/HNG_Task_2.git
   cd HNG_Task_2
   ```
2. Create and setup virtual environment
   ```bash
   pip install virtualenv # in MacOS "python3 -m pip install --user virtualenv"
   virtualenv env # in MacOS "virtualenv -p python3 env"
   env\scripts\activate.bat # in macOS "source ./env/bin/activate"
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt # in MacOS "python3 -m pip install requirements.txt"
   ```
4. Run the application
   ```bash
   python app.py #in macOS "python3 app.py"
   ```

## Usage

The API is expected to be able to perform CRUD operations on a resource. It also expected to be able to handle dynamic inputs.

### API Endpoints

- Create a Person
- Get a Person by ID
- Update a Person by ID
- Delete a Person by ID
- Create a Person by Name
- Get a Person by Name
- Update a Person by Name
- Delete a Person by Name

### Sample Requests and Responses

#### Create a Person

**Request:**

```http
POST /api/
Content-Type: application/json

{
  "name": "John Doe",
}
```

**Reponse:**

```http
{
  "message": "Person created successfully",
  "user_id": 1
}
```

## Documentation

Here is the [link](./DOCUMENTATION.md) to the documentation of the API.
