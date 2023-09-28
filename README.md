# API-DJANGO
This project is a Django API for managing users, a restaurant menu, and table reservations. It offers user authentication, CRUD operations for users and menu items, and booking functionality.


# Here's a summary of what these Django URL routes do:

1. **`/api/users`**:
   - This route is created using the DefaultRouter and associates with the `UserViewSet`.
   - It provides endpoints for listing, creating, retrieving, updating, and deleting user records.
   - Accessed via HTTP methods like GET, POST, PUT, and DELETE.

2. **`/api-auth/`**:
   - This route is used for Django REST framework's built-in authentication views.
   - It allows users to log in and log out using session authentication and provides a login page.
   - Accessed via HTTP methods like GET (for login) and POST (for logout).

3. **`/menu/`**:
   - This route maps to the `MenuItemsView`, which is a generic view for menu items.
   - It provides endpoints for listing and creating menu items.
   - Accessed via HTTP methods like GET (to list items) and POST (to create an item).

4. **`/menu/<int:pk>`**:
   - This route maps to the `SingleMenuItemView`, a generic view for a single menu item.
   - It provides endpoints for retrieving, updating, and deleting a specific menu item.
   - Accessed via HTTP methods like GET (to retrieve), PUT (to update), and DELETE (to delete).

5. **`/message/`**:
   - This route maps to the `msg` function-based view.
   - It is protected by the `IsAuthenticated` permission class, allowing only authenticated users to access it.
   - Accessed via the GET method and returns a message indicating that the view is protected.

6. **`/api-token-auth/`**:
   - This route is used for obtaining authentication tokens.
   - It associates with the `obtain_auth_token` view, which allows users to obtain a token by providing their username and password.
   - Accessed via the POST method.

7. **`/create-booking/`**:
   - This route maps to the `CreateBookingView`, a generic view for table bookings.
   - It provides endpoints for listing and creating table bookings.
   - Accessed via HTTP methods like GET (to list bookings) and POST (to create a booking).

8. **`/create-booking/<int:pk>`**:
   - This route maps to the `SingleBookingView`, a generic view for a single table booking.
   - It provides endpoints for retrieving, updating, and deleting a specific table booking.
   - Accessed via HTTP methods like GET (to retrieve), PUT (to update), and DELETE (to delete).

These URL routes define the API endpoints and their associated views, enabling various operations related to users, menu items, and table bookings in your Django application.

# To test this project after downloading it from GitHub, follow these steps:

1. **Clone the Repository:**
   - Clone or download this repository from GitHub to your computer.

2. **Install Dependencies:**
   - Make sure you have Python and Django installed on your system.
   - Navigate to the project folder in your terminal.
   - Run the following command to install project dependencies:
     ```bash
      pip install -r requirements.txt
     ```

3. **Configure the Database:**
   Before proceeding with migrations, make sure you have created the correct MySQL user, assigned privileges, and configured the database.
     Create a .env file and fill it in with the credentials of your local database.
  
        DEBUG=True
        DB_NAME=reservations
        DB_USER=    
        DB_PASSWORD=
        DB_HOST=127.0.0.1
        DB_PORT=3306
   - Perform database migrations with the following commands:
     ```bash
      python manage.py makemigrations
      python manage.py migrate
     ```

5. **Create a Superuser:**
   - Create a superuser to access the admin panel:
     ```bash
     python manage.py createsuperuser
     ```

6. **Start the Development Server:**
   - Launch the development server with the following command:
     ```bash
      python manage.py runserver
     ```

7. **Explore the API:**
   - Open your web browser and navigate to `http://localhost:8000/api/` to access the API.
   - You can use tools like `curl`, `Postman`,`Insomnia` or any API client to interact with the various endpoints available in the API.

8. **Authentication:**
   - Use `/api-token-auth/` to obtain an authentication token by providing your username and password.

9. **Test Functionalities:**
   - You can utilize routes like `/menu/`, `/create-booking/`, `/menu/<int:pk>`, and `/create-booking/<int:pk>` to list, create, view details, update, and delete menu items and bookings.

10. **Access the Admin Panel:**
   - Go to `http://localhost:8000/admin/` and log in with the superuser credentials to manage users and other data.

Enjoy exploring and testing the features and functionalities of this project. Have fun!
