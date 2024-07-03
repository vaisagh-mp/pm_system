# Project Management System
This is a Django-based project management system that includes user management, project tracking, task management, and notifications. 
It utilizes Django REST Framework for API endpoints, JWT for authentication, Celery for task processing, and Redis for caching and messaging.

## Features
- User management with role-based access control (Admin, Manager, Member).
- Project and task management with CRUD operations.
- Notification system for user updates.
- JWT authentication for secure API access.
- Background task processing with Celery.
- Caching with Redis.

## Technologies Used
- Django
- Django REST Framework
- Django REST Framework SimpleJWT
- Celery
- Redis
- SQLite (default database, can be switched to PostgreSQL, MySQL, etc.)

##Create and Activate Virtual Environment

python -m venv venv
`venv\Scripts\activate`

##Install Dependencies
pip install -r requirements.txt

##Run the Development Server
  python manage.py runserver

##Run Celery worker:
celery -A pm_system worker --loglevel=info

##API Endpoints

	#User Management
		List and create users: GET /api/users/ and POST /api/users/
		JWT token obtain: POST /api/token/
		JWT token refresh: POST /api/token/refresh/
  
	#Project Management
		List and create projects: GET /api/projects/ and POST /api/projects/
		Retrieve, update, and delete a project: GET /api/projects/{id}/, PUT /api/projects/{id}/, DELETE /api/projects/{id}/

	#Task Management
		List and create tasks: GET /api/tasks/ and POST /api/tasks/
		Retrieve, update, and delete a task: GET /api/tasks/{id}/, PUT /api/tasks/{id}/, DELETE /api/tasks/{id}/

	#Notifications
		List notifications for a user: GET /api/notifications/
		Update notification (mark as read): PUT /api/notifications/{id}/

##Caching
This project uses Redis for caching. Cache timeout is set to 15 minutes by default. Utility functions are provided for caching operations in pm_system.utils.cache.

##Background Tasks
	Celery is used for background task processing. Ensure Celery is running with a Redis broker as described in the setup section.

##Email Configuration
	Email backend is configured to use Gmail SMTP server. Update EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in the .env file with your email credentials.
