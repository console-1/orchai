# OrchAI API Reference

Welcome to the OrchAI API Reference! This section provides detailed documentation of the API endpoints and their usage, including code snippets and examples for each endpoint.

## Table of Contents

1. [Introduction](#introduction)
2. [Authentication](#authentication)
3. [Endpoints](#endpoints)
   - [Create Task](#create-task)
   - [Get Task Status](#get-task-status)
   - [Cancel Task](#cancel-task)
4. [Error Handling](#error-handling)

## Introduction

The OrchAI API allows you to interact with the OrchAI framework programmatically. You can create tasks, check their status, and cancel them using the provided endpoints.

## Authentication

To authenticate with the OrchAI API, you need to include your API key in the request headers. You can obtain your API key from the OrchAI dashboard.

Example:

```http
GET /api/v1/tasks HTTP/1.1
Host: api.orchai.com
Authorization: Bearer YOUR_API_KEY
```

## Endpoints

### Create Task

Create a new task for the orchestrator to execute.

- **URL:** `/api/v1/tasks`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer YOUR_API_KEY`
  - `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "task_name": "example_task",
    "parameters": {
      "param1": "value1",
      "param2": "value2"
    }
  }
  ```
- **Response:**
  - `201 Created`
  - `Content-Type: application/json`
  ```json
  {
    "task_id": "12345",
    "status": "created"
  }
  ```

### Get Task Status

Retrieve the status of a specific task.

- **URL:** `/api/v1/tasks/{task_id}`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer YOUR_API_KEY`
- **Response:**
  - `200 OK`
  - `Content-Type: application/json`
  ```json
  {
    "task_id": "12345",
    "status": "in_progress",
    "result": null
  }
  ```

### Cancel Task

Cancel a specific task.

- **URL:** `/api/v1/tasks/{task_id}/cancel`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer YOUR_API_KEY`
- **Response:**
  - `200 OK`
  - `Content-Type: application/json`
  ```json
  {
    "task_id": "12345",
    "status": "cancelled"
  }
  ```

## Error Handling

The OrchAI API uses standard HTTP status codes to indicate the success or failure of a request. In case of an error, the response body will contain a JSON object with an `error` field describing the issue.

Example:

```json
{
  "error": "Invalid API key"
}
```

We hope this API reference helps you integrate with the OrchAI framework. If you have any questions or need further assistance, please refer to the [Support](../README.md#support) section in the README.
