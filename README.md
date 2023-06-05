# restaurant_menu_API

This project was created solely for learning purposes. It demonstrates the implementation of various HTTP methods for retrieving and posting data into a database.

**To try it out, follow these steps:**

1. **Clone the repository.**
2. **Install the project dependencies** from the Pipfile.
3. **Navigate to the directory** containing the file `manage.py`.
4. **Run the command** `python manage.py runserver`.

**Note:** Ensure that you have Python and Django installed on your system before running the project.

Once the development server is up and running, you can interact with the restaurant_menu_API using different HTTP methods. This allows you to perform operations such as retrieving menu items, adding new items, updating existing items, and deleting items from the menu.

**API URL Paths:**

- `/admin/` - Django admin site.
- `/api/` - Main API endpoint.
- `/auth/` - Authentication endpoint (djoser).
- `/auth/authtoken/` - Token-based authentication endpoint (djoser).
- `/api/token/` - Obtain token for authentication.
- `/api/token/refresh/` - Refresh token endpoint.
- `/api/token/blacklist/` - Token blacklist endpoint.
- `/menu-items` - Menu items endpoint.
- `/menu-items-fn` - Function-based menu items endpoint.
- `/menu-items-djfl` - Menu items endpoint with Django filters.
- `/categories` - Categories endpoint.
- `/menu-items/<int:pk>` - Single menu item endpoint.
- `/categories/<int:pk>` - Single category endpoint.
- `/secret` - Secret endpoint.
- `/api-token-auth` - Token-based authentication endpoint.
- `/manager-view` - Manager view endpoint.
- `/throttle-check` - Throttle check endpoint.
- `/user-throttle-check` - User throttle check endpoint.
- `/groups/manager/users` - Manager group users endpoint.

Feel free to explore the code, experiment with various API requests, and learn about Django's implementation of RESTful APIs.

**Happy learning!**
