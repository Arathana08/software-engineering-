# Architecture and Component Design

## Three-Layer Architecture

### Presentation Layer
- Login page
- Dashboard
- Forms
- Tables
- CSS styling

### Application Layer
- Flask routes
- Authentication logic
- Request management
- Resource management
- Status management
- API endpoint

### Data Layer
- SQLite database
- Users table
- Resources table
- Requests table

## Component Interaction

Frontend
  -> Flask Routes
  -> Business Logic
  -> SQLite
  -> Response
  -> Frontend

## Quality Attributes

- Usability: simple forms and dashboard
- Maintainability: separate templates, static files and backend
- Portability: Docker container
- Security: hashed passwords and session authentication
