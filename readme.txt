1. Creating our API with Flask
-- create new api Blueprint
(this will look very similar to ig.routes)
-- use url_prefix instead of template_folder
(because we just need to access the backend data)
-- JSON
(Javascript Object Notation)
-- Standardized way of passing data across the web
-- Create a .to_dict() method on Post to convert post objects to JSON format
-- test api route

2. Create single_post_api dynamic route

3. Create create_post_api route
-- Use Postman Application to post data to api without a frontend
(Remember to add Header: Content-Type: 'application/json')
(On body tab, select the raw, dropdown should be JSON)
-- Test post request

4. Additonal CRUD methods for api
(Create = POST)
(Read/Retrieve = GET)
(Update = PUT/POST)
(Delete = DELETE)