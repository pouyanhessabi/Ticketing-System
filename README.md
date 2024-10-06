# Ticketing System
This system is a landing page for customers to submit support tickets directly into Jira. Customers enter their phone number or ID, and the system checks a database to see if they exist. If they're not in the system, they can register and get a new ID. If they already have an open ticket, they’ll see the ticket number instead of creating a new one. If no open ticket exists, a new one is created in Jira, and the customer gets the ticket ID. The goal is to make ticket submissions quick and hassle-free.

# Overview
The Ticketing System implements a basic issue management system using **Python**, **Flask** framework, **HTML**, and **Restful API** to interact with UI and **Jira**. <br>
Purpose: The system is designed to manage tickets, which could pertain to customer support or issue tracking.

# Key Components
Here is the *flowchart* of the system: <br>
![Flowchart](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/Flow%20Chart%20Ticketing%20System.jpg)

### Technologies Used:
`Python` and `Flask`: Main programming language for backend logic. <br>
`MySQL` and `SQLAlchemy`: for Database and ORM. <br>
`HTML`: Used for creating the user interface.

### Functionality:
- Users can create, view, and manage tickets.
- Authentication for users to secure the system including sign up and log in.
- Integration capabilities with **Jira**.
### Files and Structure:
- main.py: This file serves as the main entry point for the application, orchestrating the overall functionality and routing.
- auth.py: Handles user authentication, managing login and session-related operations to secure access.
- model.py: Contains data models that define the structure and relationships of the data used in the application.
- ticket.py: Manages operations related to ticket creation, viewing, and updates, encapsulating ticket-related business logic.
- jira_actions.py: Implements integration functionalities with JIRA, allowing for interaction and management of tickets within that platform.
- exceptions.py: Defines custom exceptions to improve error handling and provide clearer feedback during application execution.
- static and templates: Directories for static files (CSS, JS) and HTML templates, respectively.
### Database:
The system may utilize a database, as indicated by the presence of a .sql file (db.sql), which suggests it configures
the database schema. The database consists of two tables, client and ticket, with this structure: <br>
![Tables](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/Tables.jpg)
# User Interface
In this section you will see the pages and HTML files purpose.
### Home
- base.html: This is the main template that provides a common structure and layout for all other HTML files, including shared navigation and styling elements.
- index.html: Acts as the homepage of the application, offering an overview and links to other sections of the ticketing system. <br><br>
![Home](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/UI/Home.jpg)
### Authentication
- signup.html: Provides a registration form for new users to create an account within the ticketing system. <br><br>
![Signup](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/UI/Sign%20Up.jpg)
- login.html: Contains the login form for user authentication, allowing users to enter their credentials to access the system.
- profile.html: Displays the user's profile information and allows for viewing and editing personal details. <br><br>
![Profile](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/UI/Profile.jpg)
### Ticketing
- ticket_form.html: Features a form for users to submit new tickets, allowing them to input necessary details and categorize their issues. <br><br>
![Ticket Form](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/UI/Ticket%20Form.jpg)
- show_all_ticket.html: Lists all tickets in the system, providing users with an overview of existing tickets and their statuses.
- show_ticket.html: Displays detailed information about a specific ticket, including its description, status, and any related comments. <br>
![Show Ticket](https://github.com/pouyanhessabi/Ticketing-System/blob/main/Report/UI/Ticket%20Created.jpg)
