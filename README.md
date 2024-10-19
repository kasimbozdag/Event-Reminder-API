# Event Reminder API

A RESTful backend service built with Django and Django REST Framework that allows users to create, manage, and be reminded of upcoming events. This service provides a robust API for event management, including features like categorization, personalized reminders, and more.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Installation without Docker](#installation-without-docker)
  - [Installation with Docker](#installation-with-docker)
- [API Endpoint Documentation](#api-endpoint-documentation)
  - [Authentication](#authentication)
  - [Event Endpoints](#event-endpoints)
    - [Create Event](#create-event)
    - [Retrieve All Events](#retrieve-all-events)
    - [Retrieve Event Details](#retrieve-event-details)
    - [Update Event](#update-event)
    - [Delete Event](#delete-event)
    - [Retrieve Upcoming Events](#retrieve-upcoming-events)
    - [Retrieve Events by Category](#retrieve-events-by-category)
- [Sample Queries](#sample-queries)
  - [Create Event](#sample-create-event)
  - [Retrieve All Events](#sample-retrieve-all-events)
  - [Retrieve Event Details](#sample-retrieve-event-details)
  - [Update Event](#sample-update-event)
  - [Delete Event](#sample-delete-event)
  - [Retrieve Upcoming Events](#sample-retrieve-upcoming-events)
  - [Retrieve Events by Category](#sample-retrieve-events-by-category)
- [Testing](#testing)
- [Additional Notes](#additional-notes)
- [License](#license)

---

## Features

- **Event Management**: Create, read, update, and delete event reminders.
- **Reminder Notifications Simulation**: Retrieve events happening in the next 24 hours.
- **Categorization**: Categorize events (e.g., Work, Personal, Health) and retrieve events by category.
- **Personalized Reminder Timings**: Set custom reminder times for events.

---

## Setup and Installation

### Prerequisites

- **Python 3.9 or higher**
- **Django 4.2 or higher**
- **PostgreSQL** (if using without Docker)
- **Docker and Docker Compose** (if using Docker)

### Installation without Docker

#### 1. Clone the Repository

```bash
git clone https://github.com/kasimbozdag/Event-Reminder-API.git
cd event-reminder-api
```

#### 2. Create a Virtual Environment

```bash
python3 -m venv env
```

#### 3. Activate the Virtual Environment

- On Unix or MacOS:

  ```bash
  source env/bin/activate
  ```

- On Windows:

  ```bash
  env\Scripts\activate
  ```

#### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 5. Configure the Database

Ensure you have PostgreSQL installed and running. Create a database for the project.

Update `event_reminder/settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'event_reminder',
        'USER': 'your_db_username',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### 6. Apply Migrations

```bash
python manage.py migrate
```

#### 7. Run the Server

```bash
python manage.py runserver
```

#### 8. Access the Application

- API Root: [http://localhost:8000/api/](http://localhost:8000/api/)
- Swagger Documentation: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

### Installation with Docker

#### 1. Clone the Repository

```bash
git clone https://github.com/kasimbozdag/Event-Reminder-API.git
cd event-reminder-api
```

#### 2. Build and Run Containers

```bash
docker-compose up --build
```

This command builds the Docker images and starts the containers.

#### 3. Apply Migrations (Inside Docker)

The `docker-entrypoint.sh` script automatically applies migrations when the container starts.

#### 4. Access the Application

- API Root: [http://localhost:8000/api/](http://localhost:8000/api/)
- Swagger Documentation: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## API Endpoint Documentation

### Authentication

Currently, the API does not require authentication for simplicity. In a production environment, you should secure the endpoints using authentication mechanisms like Token Authentication or JWT.

### Event Endpoints

#### Create Event

- **URL**: `/api/events/`
- **Method**: `POST`
- **Description**: Create a new event reminder.

**Request Payload**:

```json
{
  "title": "Team Meeting",
  "description": "Monthly team sync-up meeting.",
  "date": "2024-10-19",
  "time": "14:30",
  "category": {
    "name": "Work"
  },
  "reminder_time": "2024-10-19T14:00:00Z"
}
```

**Response**:

- **Status**: `201 Created`
- **Body**:

  ```json
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Monthly team sync-up meeting.",
    "date": "2024-10-19",
    "time": "14:30:00",
    "category": {
      "id": 1,
      "name": "Work"
    },
    "reminder_time": "2024-10-19T14:00:00Z"
  }
  ```

#### Retrieve All Events

- **URL**: `/api/events/`
- **Method**: `GET`
- **Description**: Retrieve all events.

**Response**:

- **Status**: `200 OK`
- **Body**:

  ```json
  [
    {
      "id": 1,
      "title": "Team Meeting",
      "description": "Monthly team sync-up meeting.",
      "date": "2024-10-19",
      "time": "14:30:00",
      "category": {
        "id": 1,
        "name": "Work"
      },
      "reminder_time": "2024-10-19T14:00:00Z"
    },
    {
      "id": 2,
      "title": "Doctor Appointment",
      "description": "Annual check-up.",
      "date": "2024-10-20",
      "time": "09:00:00",
      "category": {
        "id": 2,
        "name": "Health"
      },
      "reminder_time": "2024-10-20T08:30:00Z"
    }
  ]
  ```

#### Retrieve Event Details

- **URL**: `/api/events/{id}/`
- **Method**: `GET`
- **Description**: Retrieve details of a specific event.

**Response**:

- **Status**: `200 OK`
- **Body**:

  ```json
  {
    "id": 1,
    "title": "Team Meeting",
    "description": "Monthly team sync-up meeting.",
    "date": "2024-10-19",
    "time": "14:30:00",
    "category": {
      "id": 1,
      "name": "Work"
    },
    "reminder_time": "2024-10-19T14:00:00Z"
  }
  ```

#### Update Event

- **URL**: `/api/events/{id}/`
- **Method**: `PUT`
- **Description**: Update a specific event.

**Request Payload**:

```json
{
  "title": "Updated Team Meeting",
  "description": "Updated monthly team sync-up meeting.",
  "date": "2024-10-19",
  "time": "15:00",
  "category": {
    "name": "Work"
  },
  "reminder_time": "2024-10-19T14:30:00Z"
}
```

**Response**:

- **Status**: `200 OK`
- **Body**:

  ```json
  {
    "id": 1,
    "title": "Updated Team Meeting",
    "description": "Updated monthly team sync-up meeting.",
    "date": "2024-10-19",
    "time": "15:00:00",
    "category": {
      "id": 1,
      "name": "Work"
    },
    "reminder_time": "2024-10-19T14:30:00Z"
  }
  ```

#### Delete Event

- **URL**: `/api/events/{id}/`
- **Method**: `DELETE`
- **Description**: Delete a specific event.

**Response**:

- **Status**: `204 No Content`

#### Retrieve Upcoming Events

- **URL**: `/api/events/upcoming/`
- **Method**: `GET`
- **Description**: Retrieve events happening in the next 24 hours from the current time.

**Response**:

- **Status**: `200 OK`
- **Body**:

  ```json
  [
    {
      "id": 2,
      "title": "Doctor Appointment",
      "description": "Annual check-up.",
      "date": "2024-10-20",
      "time": "09:00:00",
      "category": {
        "id": 2,
        "name": "Health"
      },
      "reminder_time": "2024-10-20T08:30:00Z"
    }
  ]
  ```

#### Retrieve Events by Category

- **URL**: `/api/events/category/{categoryName}/`
- **Method**: `GET`
- **Description**: Retrieve events by category name.

**Response**:

- **Status**: `200 OK`
- **Body**:

  ```json
  [
    {
      "id": 1,
      "title": "Team Meeting",
      "description": "Monthly team sync-up meeting.",
      "date": "2024-10-19",
      "time": "14:30:00",
      "category": {
        "id": 1,
        "name": "Work"
      },
      "reminder_time": "2024-10-19T14:00:00Z"
    }
  ]
  ```

---

## Sample Queries

Below are sample `curl` commands for each endpoint to demonstrate how to interact with the API.

### Sample Create Event

```bash
curl -X POST \
  'http://localhost:8000/api/events/' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Team Meeting",
  "description": "Monthly team sync-up meeting.",
  "date": "2024-10-19",
  "time": "14:30",
  "category": {
    "name": "Work"
  },
  "reminder_time": "2024-10-19T14:00:00Z"
}'
```

### Sample Retrieve All Events

```bash
curl -X GET 'http://localhost:8000/api/events/'
```

### Sample Retrieve Event Details

```bash
curl -X GET 'http://localhost:8000/api/events/1/'
```

### Sample Update Event

```bash
curl -X PUT \
  'http://localhost:8000/api/events/1/' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Updated Team Meeting",
  "description": "Updated monthly team sync-up meeting.",
  "date": "2024-10-19",
  "time": "15:00",
  "category": {
    "name": "Work"
  },
  "reminder_time": "2024-10-19T14:30:00Z"
}'
```

### Sample Delete Event

```bash
curl -X DELETE 'http://localhost:8000/api/events/1/'
```

### Sample Retrieve Upcoming Events

```bash
curl -X GET 'http://localhost:8000/api/events/upcoming/'
```

### Sample Retrieve Events by Category

```bash
curl -X GET 'http://localhost:8000/api/events/category/Work/'
```

---

## Testing

### Running Tests

To run the test suite, execute the following command:

```bash
python manage.py test events
```

### Test Coverage

The test suite covers:

- Model tests for `Event` and `Category` models.
- Serializer tests for `EventSerializer`.
- API endpoint tests for all CRUD operations and custom actions.
- Edge case tests to ensure robust handling of invalid data.

---

## Additional Notes

- **Time Zones**: Ensure that all date and time fields are in the correct format and time zone (`UTC` is recommended).
- **Date and Time Formats**:
  - **Date**: `YYYY-MM-DD` (e.g., `2024-10-19`)
  - **Time**: `HH:MM` or `HH:MM:SS` (e.g., `14:30` or `14:30:00`)
  - **DateTime**: `YYYY-MM-DDTHH:MM:SSZ` (ISO 8601 format, e.g., `2024-10-19T14:00:00Z`)
- **Swagger Documentation**: Visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/) for interactive API documentation.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
