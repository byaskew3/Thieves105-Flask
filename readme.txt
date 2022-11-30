1. Authentication
-- Handles login/logout functionality

2. CRUD Operations (SQL)
-- Create - Insert
-- Read - SELECT
-- Update - UPDATE
-- Delete - DELETE

3. CRUD Operations (HTTP)
-- Create - POST
-- Read - GET
-- Update - PUT/POST
-- Delete - DELETE

4. Update Navbar & Login Page
5. Add Custom CSS

6. (Login Functionality)
NOTE: This will look very similar to our signup route/steps
-- Create LoginForm on forms.py
-- Add LoginForm to auth.routes
-- Apply some of the same logic from our signup route to our login route
-- Validate/Match Login Data with Database (ElephantSQL)
-- pip install flask-login
-- import LoginManager on __init__.py
-- import UserMixin on models.py
-- Add current_user to navbar (This is a checker to make sure LoginManager is doing its job)
-- Import login_user, logout_user on auth.routes
-- Verify login

7 . (Logout Functionality)
-- Create logout route on auth.routes
-- Add logout link,  if current_user.is_authenticated to navbar

8. Password Hashing for database
-- import generate_password_hash on models.py
-- import check_password_hash on auth.routes
-- delete all users in our db that don't have a hashed Password
(DELETE FROM "user" where password="test1234")

9. Ig Blueprint
NOTE: This will look very similar to our auth blueprint
-- Create ig blueprint
-- Create forms, routes, ig_templates (create_post, feed)
-- Add "create post" link to navbar
-- Remember to register your blueprint on __init__.py
-- Create PostForm
-- Import PostForm on ig.routes
-- Add post to database
-- Finish create post html (Copy & Paste signup.html and adjust to our needs)
-- Try to make a POST!

10. Handle Backdoor access to specific routes using @login_required wrapper
-- On __init__.py implement functionality, if no current user, redirect to login page
(login_manager.login_view = 'auth.login')

11. Create Feed page & route
(Remember to update navbar with feed link)
-- create a card for each post from database
=======
1. Flask Forms (WTForms)
-- Used to accept user information from the frontend, pass it to our backend, and store it in Database.

2. Flask Models (SQLAlchemy)
--

3. We're primarily going to be working with only the auth section today.

(Forms Section)
-- add login route to auth blueprint (remember to remove it from main routes)
-- polish/finish signup.html
-- pip install flask-wtf (remember to pip freeze when you add new pip installs to venv)
-- create forms.py in auth, create UserCreationForm
-- on auth.routes import the form on the signup route
-- Add SECRET_KEY to .env for security (rememeber to update your config file)
-- Add form inputs on signup.html (also, add form.hidden_tag() at the top of form)
-- GET/POST requests
-- import request on auth.routes

(Models Section)
-- create models.py on root level of app
-- pip install flask-sqlalchemy
-- Create User & Post Models
-- On auth.routes instantiate/add the User

(Database Section)
-- create new instance on ElephantSQL
-- add DATABASE_URL to .env (rememeber to add 'ql' after 'postgres')
-- update config file. (The Variable name must be 'SQLALCHEMY_DATABASE_URI' when using SQLAlchemy)
-- pip install flask-migrate, psycopg2 (MAC:psycopg2-binary)
-- add migrate,db imports to __init__.py
-- initialize our database to work with our Database
-- import models
-- migrate models to database
(Terminal Commands to migrate) 
(flask db init,flask db migrate,flask db upgrade)

4. Redirect from signup to login
-- import redirect, url_for on auth.routes
