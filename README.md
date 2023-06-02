# Algobulls Todo API

## Table of Contents
- [Algobulls Todo API](#algobulls-todo-api)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
      - [Or you can run it locally](#or-you-can-run-it-locally)
  - [API Endpoints](#api-endpoints)
    - [Get a list of all the tasks](#get-a-list-of-all-the-tasks)
    - [Create a new task](#create-a-new-task)
    - [Get a task by id](#get-a-task-by-id)
    - [Update a task by id](#update-a-task-by-id)
    - [Delete a task by id](#delete-a-task-by-id)
  - [Authentication](#authentication)
    - [Register a new user](#register-a-new-user)
## Getting Started
The API is available at [https://algobulls-todo.onrender.com/](https://algobulls-todo.onrender.com/)

You can see the documentation at [https://algobulls-todo.onrender.com/](https://algobulls-todo.onrender.com/)

#### Or you can run it locally
1. Clone the repository
2. Install the dependencies
```bash
pip install -r requirements.txt
```
3. Run the server
```bash
python manage.py runserver
```
4. The API is now available at [http://localhost:8000/](http://localhost:8000/)
5. You can see the documentation at [http://localhost:8000/](http://localhost:8000/api/schema/swagger-ui/)
6. You can also see the documentation at [http://localhost:8000/](http://localhost:8000/api/schema/redoc/)

## API Endpoints

### Get a list of all the tasks
`GET /api/tasks/`
```bash
curl -X GET https://algobulls-todo.onrender.com/api/todos/ -u "username:password"
```

### Create a new task
`POST /api/tasks/`
```bash
curl -X POST https://algobulls-todo.onrender.com/api/todos/ -u "username:password" -H "Content-Type: application/json" -d '{"title": "string", "description": "string", "status": "string", "due_date": "string", "tags": ["string"]}'
```

### Get a task by id
`GET /api/tasks/{id}/`
```bash
curl -X GET https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password"
```

### Update a task by id
`PUT /api/tasks/{id}/`
```bash
curl -X PUT https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password" -H "Content-Type: application/json" -d '{"title": "string", "description": "string", "status": "string", "due_date": "string", "tags": ["string"]}'
```

### Delete a task by id
`DELETE /api/tasks/{id}/`
```bash
curl -X DELETE https://algobulls-todo.onrender.com/api/todos/{id}/ -u "username:password"
```

## Authentication

### Register a new user
`POST /api/auth/register/`
```bash
curl -X POST https://algobulls-todo.onrender.com/api/auth/register/ -H "Content-Type: application/json" -d '{"username": "string", "password": "string"}'
```
