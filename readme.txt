1. Make small tweaks to feed page.
(Display most recent posts first, increase card & caption sizes)

2. Dynamic Routes for each post in the feed
-- Create a Dynamic Route on ig.routes
-- Create single_post.html on ig.templates
(Identical to the feed.html just without the for loop)
-- Create if conditional for invalid post_id route
-- Make feed cards clickable to route to the specific post

3. Add Update and Delete buttons to specific post
(Update Functionality)
-- Create update_post dynamic route on ig.route
(Identical to create_post route)
-- Create update_post.html
(Identical to create_post.html)

(Delete Functionality)
-- Implement Bootstrap Modal on single_post
(Replace Delete Button)
-- Create delete_post dynamic route on ig.route
-- Create delete_from_db method

4. Protect single post from unauthorized users & backdoor security
(if current_user.id == post.user_id)

5. Flash Messages
-- Update all print statements to be flash messages

6. Many to Many Relationships with Pokemon Assignment