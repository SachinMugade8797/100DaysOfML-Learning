Flask One Shot - https://youtu.be/zPUB3_AnRTQ

Notes 



---

## 1. Prerequisites and Environment Setup

### Brief Explanation

Before starting, you need basic Python knowledge, especially how to create **functions**. Flask is a **Python framework**. We use a **Virtual Environment (VENV)** to install libraries because sometimes installing them in the main system can **disturb other libraries or the system itself**. You must **activate** the VENV; otherwise, libraries will install on your main system. Finally, you install the Flask library into the VENV.

| Code Snippet (Terminal) | Description | Functionality |
| :--- | :--- | :--- |
| `python -m venv .venv` | This command creates the virtual environment folder (named `.venv`). | Isolates the project's libraries and keeps them separate from your computer's main system libraries. |
| `.venv/Scripts/activate.ps1` | This is an example path used to activate the created VENV. | Ensures that all subsequent library installations go into the isolated VENV. |
| `pip install Flask` | This command installs the necessary Flask library. | Makes the Flask framework available so you can start building the web application. |

## 2. Application Initialization and Basic Routing

### Brief Explanation

After setup, you start your application by importing the `Flask` class and creating the application instance, usually named `app`. **Routes** (which can be thought of as "paths" or "rastay") are then defined using the `@app.route()` decorator. A route links a specific URL path (like the home page `/`) to a specific Python function (like `home()`). The function runs and returns the content when that path is accessed. Finally, `app.run()` starts the server.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `from flask import Flask` | Imports the main `Flask` class from the installed library. | This is the starting point for building the app. |
| `app = Flask(__name__)` | Creates the main application instance, typically named `app`. | Initializes the core web application object. |
| `@app.route('/')` | A decorator that defines the root URL path (`/`). | Links the function immediately below it (`home()`) to the website's home address. |
| ```python def home(): return "Hello World" ``` | Defines the function that runs when the root URL is accessed. | Returns the string "Hello World" as the web page content. |
| ```python if __name__ == "__main__": app.run() ``` | Runs the application server. | Starts the web server so it can listen for user requests and process routes. |

## 3. Debugging and Multiple Pages

### Brief Explanation

During development, it saves a lot of time if the app automatically restarts after every change. This is done by setting `debug=True` when running the app. This option should usually be removed during hosting/deployment. To add more pages, you define extra routes (like `/about`). Each route must be linked to a function with a unique name. While you can return raw HTML text (like `<h1>`) directly from the function, this is inefficient for large websites.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `app.run(debug=True)` | Sets the debugging parameter to true when the app starts. | Automatically restarts the application whenever code changes are saved, speeding up development. |
| `@app.route('/about')` | Defines a new route for the "About" page. | Links the URL `/about` to the `about()` function. |
| ```python def about(): return "This is about page" ``` | Defines a function for the new route. | Provides unique content for the `/about` page. |
| `return "<h1>Hello World</h1>"` | Example of returning HTML directly within the Python function. | Displays the output formatted by the HTML tag (e.g., as a large heading). |

## 4. Templating with `render_template`

### Brief Explanation

To manage HTML efficiently, you must keep it in separate files called **templates**. To use templates: 1. You must import the `render_template` function. 2. All HTML files must be placed inside a specific folder that **must be named `templates`**. Flask automatically loads files from this folder. This process prevents the code from becoming **mashed up** (mixed together), making modification easier.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `from flask import render_template` | Imports the function needed to load HTML files. | Allows the Python function to load and display an entire HTML page. |
| `return render_template('index.html')` | Tells Flask to look for the file named `index.html`. | Renders the content of the `index.html` file from the `templates` folder. |
| `return render_template('about.html')` | Renders a separate template file for the "About" page. | Allows the creation of multiple pages using separate HTML files. |

## 5. Dynamic Content with Jinja2

### Brief Explanation

Flask uses the **Jinja2** template engine by default. Template engines allow you to write **backend logic** (like loops and conditions) inside your frontend code, making the templates **dynamic**.

*   **Variables:** To display a variable (like `name`) passed from the Python side, you use **double curly braces** `{{ variable_name }}`. If the variable is not passed from the backend, it will not show up.
*   **Logic:** To write loops or conditions, you use the format `{% logic %}`. Any logical block started must be **explicitly closed** (e.g., `{% endfor %}`, `{% endif %}`) to avoid a **Template Syntax Error**.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| **Python:** `return render_template('index.html', name='Moh')` | Passes a Python variable (`name`) and its value to the template. | Allows the template to display the dynamic data from the backend. |
| **HTML (Variable):** `<h1>Hello {{ name }}</h1>` | Displays the value of the `name` variable. | Renders the variable content using the Jinja2 syntax. |
| **HTML (Loop):** ```html {% for n in name %} <p>{{ n }}</p> {% endfor %} ``` | Runs a `for` loop over the characters of the `name` variable. | Executes Python logic within the HTML; the loop must be closed with `{% endfor %}`. |
| **HTML (Conditional):** ```html {% if n != 'l' %} <p>{{ n }}</p> {% endif %} ``` | Uses an `if` condition to check if a character (`n`) is not equal to 'l'. | Allows content to be rendered only if a specific condition is met. |

## 6. Template Inheritance and Static Files

### Brief Explanation

**Template inheritance** is used to create a consistent **basic theme** (layout, navbar, footer) for the website.

*   **`include` vs. `extends`:** You use `include` when you need to **add a component** (like a navbar) from another file. You use `extends` when a child page needs to **inherit the entire structure** of a base file (like `base.html`).
*   **Named Blocks:** When inheriting, the base file defines a `{% block name %}` placeholder. This name (e.g., `content`) acts as a variable, defining where the child page's unique content will be inserted.
*   **Static Files:** Assets like CSS, JS, images, and videos must be stored in a folder that **must be named `static`**.
*   **Linking:** You cannot use normal relative paths. You must use the `url_for` function within Jinja2 syntax to correctly link static files. This is necessary for **relative paths** (in contrast to external files like Bootstrap, which use **absolute paths** and can be copied directly).

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `{% extends 'base.html' %}` | Used in a child page to inherit the structure from `base.html`. | Allows multiple pages to share the same overall design (header, footer, etc.). |
| `{% include 'navbar.html' %}` | Used to inject a component's code from a separate file into the current template. | Enables modularity (e.g., loading a pre-written navbar code). |
| `{% block content %}` ... `{% endblock content %}` | Defines a unique, named placeholder in the base file. | Marks the specific area where unique content from the inheriting child templates will be placed. |
| ```html <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}"> ``` | Links a CSS file (`style.css`) located in the `static` folder. | Generates the correct path required for Flask to load relative static files. |

## 7. Form Handling and Request Methods

### Brief Explanation

Form handling involves receiving user data (like username and password) from the frontend (HTML) to the backend (Python).

*   **Input Naming:** Every input field in the HTML form **must have a `name` attribute** defined. This name is what the backend uses to identify the data.
*   **GET vs. POST:** By default, Flask routes use the **GET** method, where data is visible in the **URL**. For sensitive data, the HTML form should use **POST**, which prevents the data from showing up in the URL.
*   **Route Methods:** If the form uses POST, the route decorator must explicitly allow it using `methods=['GET', 'POST']`. If you skip this, you get a "Method Not Allowed" error. `GET` is usually kept so the page template loads correctly.
*   **Data Access:** The **`request` object** must be imported from Flask to access incoming data. Data fetching is typically done only if the request method is POST.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| **HTML:** `<input type="text" name="username">` | Assigns a unique name attribute to the input field. | Allows the backend to identify this specific piece of data when the form is submitted. |
| **HTML:** `<form method="POST">` | Sets the form submission method to POST. | Ensures sensitive data (like passwords) is not displayed in the URL. |
| **Python Route:** `@app.route('/register', methods=['GET', 'POST'])` | Explicitly lists the allowed request methods for this route. | Allows the route to handle form submission data (POST) without errors. |
| `from flask import request` | Imports the `request` object from the Flask library. | Necessary for accessing any data (like form submissions) sent by the user. |
| ```python if request.method == 'POST': username = request.form['username'] ``` | Checks if the submission was POST, and if so, fetches the value of the input named 'username'. | Prevents the fetching code from running when the page is first loaded (GET request). |

## 8. Database Management System (DBMS) Setup

### Brief Explanation

To store data permanently, we use a database. The tutorial prefers **Flask-SQLAlchemy** because its use is very **easy**.

*   **Configuration:** You must configure where the database file will be stored by setting the capitalized variable `SQLALCHEMY_DATABASE_URI`. This defines the path and type (e.g., SQLite) of the database file.
*   **Model Class:** A Python class (e.g., `class User(db.Model)`) acts as a **blueprint** for the data table.
*   **Primary Key:** Every database object needs a **unique key** for identification. The Primary Key (`primary_key=True`) is extremely important because **all data operations (update, delete)** are performed based on this key. A table **cannot have more than one** Primary Key.
*   **Table Creation:** The command `db.create_all()` must be executed (preferably within an application context) to automatically create the database file (e.g., `user.db`) inside the **`instance` folder** when the application runs.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `pip install Flask-SQLAlchemy` | Installs the database library. | Allows Python to interact easily with the chosen database system. |
| ```python app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db' ``` | Defines the database type (SQLite) and file name (`user.db`). | Tells Flask where to store the persistent data. |
| `db = SQLAlchemy(app)` | Initializes the database object using the application instance. | Prepares the application for database commands. |
| ```python class User(db.Model): serial_number = db.Column(db.Integer, primary_key=True) username = db.Column(db.String(200), nullable=False) ``` | Defines the table structure (columns) and assigns the primary key (`serial_number`). `nullable=False` means the field cannot be empty. | Creates the blueprint for the data table and ensures each entry is unique via the Primary Key. |
| ```python with app.app_context(): db.create_all() ``` | Executes the command to create the database file and tables. | Ensures the database file (e.g., `user.db`) is automatically generated in the `instance` folder upon application run. |

## 9. Data Storage and Retrieval (Create/Read Operations)

### Brief Explanation

Data storage (Create) requires creating a new object from the Model, adding it to the database **session**, and then running **`commit()`** to permanently save the data. If you don't commit, the data will not be stored.

For data retrieval (Read), you use the query **`Model.query.all()`** to fetch all stored records from the table. The fetched data is then passed to the template and displayed using a Jinja2 loop. After any database operation, it is recommended to use the **`redirect`** function to send the user back to a main page.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `NewUser = User(username=username, password=password)` | Creates a new object using the data fetched from the form. | Prepares the new record to be inserted into the table. |
| ```python db.session.add(NewUser) db.session.commit() ``` | Adds the new object to the database session and confirms the change. | **Permanently stores** the user data in the database file. |
| `all_users = User.query.all()` | Queries the `User` table to retrieve every entry. | Fetches all stored data from the database (Read operation). |
| **HTML (Jinja2):** `{% for user in all_users %}` | Starts a loop in the HTML template to iterate over the list of user objects. | Displays each user's data sequentially on the web page. |
| `return redirect('/')` | Imports and uses the `redirect` function to move the user to a different URL (`/`). | Sends the user to the home page after a successful operation (like registration/creation or update). |

## 10. Updating and Deleting Data (Update/Delete Operations)

### Brief Explanation

Update and Delete operations rely entirely on the **Primary Key** to identify the specific record to modify. The Primary Key (serial number) is passed through the URL route as a **variable** to identify the user.

*   **Finding the User:** The user is found using `Model.query.filter_by(primary_key=variable).first()`.
*   **Update:** You change the attributes of the found user object (e.g., `user.username = new_username`) and then **add it to the session and commit**.
*   **Delete:** You find the user, use `db.session.delete(User)`, and then **commit** the session.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| **HTML Link:** `href="/update/{{ user.serial_number }}"` | Passes the user's unique primary key (`serial_number`) through the URL. | Allows the backend to know exactly which user needs to be modified. |
| **Python Route:** `@app.route('/update/<serial_number>', methods=['GET', 'POST'])` | Defines a route that accepts a variable (`serial_number`) in the URL path. | Captures the unique ID needed for the update operation. |
| `user = User.query.filter_by(serial_number=serial_number).first()` | Finds the single user object whose primary key matches the ID captured from the URL. | Locates the specific database record for modification or deletion. |
| `user.username = new_username` | Assigns the newly fetched username (from the form) to the old user object. | Modifies the data held by the record in preparation for storage. |
| ```python db.session.delete(User) db.session.commit() ``` | Deletes the found user object from the session and confirms the change. | Permanently removes the record from the database. |




















---

## 1. Database Model Definition and Table Creation

### Brief Explanation

After configuring the basic database connection, we need to define the structure of the data we want to store. This is done by creating a Python **class** which acts as a **blueprint** (or Model) for our database table. Every object we store will follow this blueprint.

It is critical to define a **Primary Key (PK)**, as this key provides **uniqueness** to each entry, and all operations (Update, Delete) depend on it. A table can only have one PK. We also define columns with their data types (`db.Integer`, `db.String`) and constraints, such as `nullable=False`, meaning the field cannot be left empty.

Finally, we run a command to ensure the database file (`user.db`) and its tables are **automatically created** inside the **`instance` folder** when the code runs, preventing manual setup.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| ```python class User(db.Model): serial_number = db.Column(db.Integer, primary_key=True) ``` | Defines the `User` class which acts as the table blueprint, inheriting from `db.Model`. The column `serial_number` is set as the Primary Key. | Creates the foundation for the `User` table and ensures each entry has a unique identifier for operations. |
| ```python username = db.Column(db.String(200), nullable=False) ``` | Defines a column named `username` as a string type with a maximum length of 200 characters. `nullable=False` is set. | Ensures the username field cannot be left empty (null) when data is stored. |
| ```python date_time = db.Column(db.DateTime, default=datetime.utcnow) ``` | Defines a column for storing the time the record was created. `datetime.utcnow` provides a default timestamp. | Automatically records the creation time of the user entry. |
| ```python with app.app_context(): db.create_all() ``` | Executes the command to create all defined tables within the application context. | Automatically generates the database file (e.g., `user.db`) inside the `instance` folder. |

## 2. CRUD Operations: Create (Store) and Read (Fetch)

### Brief Explanation

The **Create** operation involves taking the fetched form data and permanently saving it. This requires three steps: 1. Create a new object of the `User` Model. 2. **Add it to the database session** (`db.session.add`). 3. **Commit the session** (`db.session.commit`) to confirm and save the changes. If you don't commit, the data will not be saved.

The **Read** operation retrieves data. We use **`User.query.all()`** to fetch all entries. This fetched data is then passed to the template and displayed using a Jinja2 `for` loop, iterating over the records. While displaying data like passwords is okay for testing, in a real application, passwords should be converted to hashes (e.g., using the **Bycrypt** library) for security.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| `NewUser = User(username=username, password=password)` | Creates a new object instance of the `User` model, using variables fetched from the form. | Prepares the data object for insertion into the table. |
| ```python db.session.add(NewUser) db.session.commit() ``` | Adds the new object to the database session and confirms the permanent storage of the data. | Completes the **Create** operation, saving the data to the database file. |
| `all_users = User.query.all()` | Queries the `User` model to fetch every single record stored in the table. | Performs the **Read** operation, retrieving all data objects. |
| **Python:** `return render_template('index.html', all_users=all_users)` | Passes the retrieved list of all user objects to the template. | Makes the database results available for display on the frontend. |
| **HTML (Jinja2):** `{% for user in all_users %}` | Starts a loop in the HTML to iterate through the list of user objects. | Dynamically displays each user record on the web page. |
| **HTML (Jinja2):** `{{ loop.index }}` | A special Jinja2 variable used inside a loop. | Displays the current sequential index (number of times the loop has run), providing row numbering. |

## 3. CRUD Operations: Update and Delete Setup

### Brief Explanation

Update and Delete operations rely entirely on knowing the **Primary Key** of the record to be modified. We pass this Primary Key (serial number) through the URL. This requires defining a variable within the route path, which is captured by the corresponding Python function.

We find the specific user using **`filter_by()`** based on the captured Primary Key. Using `.first()` ensures that the search stops immediately once the unique user is found, saving time.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| **HTML:** `href="/update/{{ user.serial_number }}"` | Generates a link that embeds the user's unique serial number (Primary Key) into the URL path. | Ensures that when the update button is clicked, the specific record ID is sent to the backend. |
| **Python Route:** `@app.route('/update/<serial_number>', methods=['GET', 'POST'])` | Defines the route to capture the unique Primary Key from the URL path as a variable named `serial_number`. | Makes the specific record ID available as an argument in the Python function. |
| ```python user = User.query.filter_by(serial_number=serial_number).first() ``` | Finds the single user object whose serial number matches the one captured from the URL. | Locates the exact database record that needs to be updated or deleted. |
| **HTML (Form Field):** `value="{{ user.username }}"` | Used inside the update form's input field to display the existing data. | Pre-fills the form with the user's current data, allowing them to easily update it. |

## 4. Executing Update, Delete, and Redirection

### Brief Explanation

To complete the **Update** operation, we simply change the attributes of the found user object (e.g., `user.username = new_username`). We then **add the object to the session and commit** the change. The same technique of finding the user is used for **Delete**, but we use `db.session.delete(user)` before committing.

After any successful operation (Create, Update, or Delete), the user should be redirected to a different page (like the home page) for better user experience. The **`redirect`** function (which must be imported from Flask) is used for this purpose. It is crucial to place the `redirect` command **after** the `db.session.commit()` to ensure the database change is finalized before the user is moved.

| Code Snippet | Description | Functionality |
| :--- | :--- | :--- |
| ```python user.username = new_username user.password = new_password ``` | Assigns the new data fetched from the update form to the attributes of the located user object. | Modifies the record data in memory before saving it back to the database. |
| ```python db.session.add(user) db.session.commit() ``` | Adds the modified user object to the session and permanently saves the changes. | Completes the **Update** operation. |
| `from flask import redirect` | Imports the necessary function for moving users between pages. | Enables fluid navigation after operations. |
| `return redirect('/')` | Tells the application to send the user to the root URL (`/`). | Redirects the user to the home page after an operation (Create, Update, or Delete). |
| ```python db.session.delete(user) db.session.commit() return redirect('/') ``` | Deletes the user object from the database session, commits the deletion, and redirects the user. | Completes the **Delete** operation, removing the record permanently. |





