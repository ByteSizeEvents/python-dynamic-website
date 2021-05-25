# python-dynamic-website
A Python Flask dynamic website - User registration, login and dynamic, unique content per user.

## Running this website
If you are running locally, make sure you have installed all Python requirements by: `pip install -f requirements.txt` then `flask run`.

## Using this website
Endpoints available when running:

`/ or /index` - Home page. Uses fixed user data to print out a username. Also prints out the render time.
`/user` - User page. Uses fixed user data to print out a username and a link.
`/user/create` - Short URL create page, contains a form expecting two elements. Will create an entry in the database.
`/user/created/<guid>` - Short URL creation confirmation page, redirected to this page on the submission of `/user/create` form.
`/<guid>` - Short URL redirection page. Searches the database for the GUID (short URL), returns the long URL and redirects.
