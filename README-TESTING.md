# Testing

## User Tests

- All active buttons / links change color or tone when hovering over or clicking.
- All text is differentiated from the backgroung making it easier to read for the user.
CHANGE TEXT SIZES!

- From navigating the whole website, I found
    - All various sections, buttons, are separated where needed, through different backgrounds, colors and borders.
    - All pages have a nav bar and footer which are constantly available and provide links to all the main sections of the site. I know I can scroll to the bottom or top to navigate the website.
    - navbar and footer always contains links for charts, blog, bugs, features and cart pages. For logged in users, they also contain profile and logout links.
    - For logged out users, they also contain login and register links.
    - Having these differences, helps tell me if I am logged in or logged out.
    - On mobile width, the navbar links are located in a drop down box which is accessable from clicking the drop box icon. 
    - All active links/buttons are working and change color upon hovering and clicking, telling me they are working. 
    - Each button associated with a specific page, brings me to the page upon clicking.
    - I am always greeted with the correct header for the website.
    
- Upon first loading the site, as a logged out user, I am located to the home page, which shows the following,
    - The website masthead / header with Login and Register links/buttons and message telling me what I can do as a logged in user.
    - A welcome message, introducing the website, which suggests me to look at the Charts page for further details.
    - Examples of recent bug reports and feature requests in a side nav, which gives me an idea of how what is done on the website and tells what was recently posted. 
    - Recent news on the website, and refers me to the full news blog page for further news.
    - I get a good strong introduction to the site for this page.
    
- Upon revisiting the home page as a logged in user, the following changes to the page can be seen
    - A message welcome me (my user name) back, plus Create Bug Report and Create Feature Request buttons on the masthead, instead of the Login and Register buttons.

- On loading registration page..
    - I am first suggested to Login instead, if I already have an account, followed by a login link/button.
    - I can see the registration form, requiring an email, username, password and password confirmation.
- Upon going into the login page, 
    - I am first suggested to Register first if I haven't done so, followed by a registration link/button.
    - I can see the login form, requiring my username and password.
- Upon confirming registration..
    - If succesful, I am brought to the login page, with a message telling me I succesfully logged in.
- Upon confirming login..
        If succesful, I am brought to the Profile page, and greeted with a message.
- Upon attempting to register OR login,
    - If required inputs are missing, It alerts me without reloading the page.
    - If its a failed attempt, the page reloads with a message telling me what happened.
    
- If logged in, 
    - but login and register links/buttons are available on an already loaded page
        - clicking the login and register buttons will redirect me to the profile page, telling me to logout first.
    
- If logged out, 
    - but profile links/buttons are available on an already loaded page
        - clicking the profile button will redirect me to the login page, telling me to login first. 
    - and bug report detail page is already open with links to vote, delete, comment
        - activating these links redirects me to the login page, telling me to login.
    - and feature request detail page is already open with a link to comment, modal pop up to vote (with money in input)
        - activating these links redirects me to the login page, telling me to login.
    - and bug report/feature request edit or new form is open,
        - upon posting I am redirected to the login page, telling me to login.
    - and cart page is open, with items and their adjust buttons available, aswell as the checkout button.
        - upon adjusting or checking out, I am redirected to login page, telling me to login first (message excluded from clicking checkout.)
    - and checkout page is open, with the form filled in correctly and the confirm checkout button available,
        - upon confirming the payment, I am redirected to the login page without a message.

- Upon opening the bug reports and feature requests pages,
    - I am provided with a search form and three drop down panels, with the first open.
    - The panels in order are are Done, Doing and To Do, splitting all posts by they current status. When each are opened they display the all the posts with the status category.
    - each panel has a number displayed next to the status category, correctly displaying the amount of posts it contains.
    - if I am logged in,
        - I am provided with a button to create a post (i.e. create bug post for the bug posts list). 
        - if any of my posts in the panels are mine, it tells me.
    - if logged out, I am provided with a button to lead me to the login page, which tells me I can create posts as a member.

- Upon opening profile page,
    - The header tells me my user name and if I had registered with my email it is displayed.
    - I am provided with two drop down panels, both containing my posts. The panels separate the categories of posts between bugs and features.
    - a create Bug Report button and create Feature Request button, both easily located above their respected panels.
    - The panels embody much of the same panel functionality of the bugs and features pages panels, keeping the website consistent.

- Upon Loading individual Bug Report or Feature Request detail pages, 
    - I am provided with the full details of the post (title, description, status, user who created it (will tell me its mine if im logged in and if its mine), status, published date, the countings of likes, views and comments).
    - the list of full comments below the details of post.
    - a set of sticky buttons (and other tools) which scroll along the screen while I read the comments.
    - a 'Back to top' button (located on the sticky buttons), in which on clicking brings the user back to the top of page through animation.
    - a back to listings button (located on the sticky buttons), which brings the user back to the listings page (bugs report or feature request listings page).
    - if logged in, 
        - a vote button is available if the post status is not 'Done'.
        - if post's status is not 'Done', a comment form (located on the sticky buttons) in which drops down on clicking a button. 
    - if logged out, 
        - if post's status is not 'Done', a login page button is seen.
        - 
- Upon voting for 
    - bug reports, I am brought back to the bugs listings page.
    - feature requests, 
        - I am prompted with a pop up money form, telling to submit money to vote, while also telling me how it works (i.e. 10 euro equals 1 vote). Upon suggesting amount to give, in order to vote, I am brought to the checkout page.

- in cart page, Upon amending cart items' euro adding
    - to 0 or leaving the input field empty, the item is removed after clicking amend.
    - to a number greater than 0, the page is reloaded showing the changes.

- For posts in all drop down panels,
    - they are further destinguished by their status cateogories through different background colors (Red for To Do, Yellow for Doing, and Green for Done), in which is particularly useful for the profile page where they are all mixed together.
    - They contain all details of the post, but a shortened title and description. 
    - a view button is included to access the detail page.
    
- from bug post panel displays and their detail pages,
    - if the post's status is 'To Do', Edit and Delete buttons are available.

- from feature post panel displays and their detail pages,
    - if the post's status is 'To Do', an Edit button is available.
    - total money donated to create amount of votes is seen.
    
- If a feature report or bug post status is 'Done', then the buttons and forms add values to the post are removed.
###################################

- Upon loading the cart page,
    - as a logged in user 
        - I am prompted with the option to adjust my current payments of my submitted features and a cost summary.
        - the checkout button is available if there are items in the cart.
        - 
    - as a logged out user
        - I view an empty cart, and I am prompted to Login or Register to use the cart.

- Upon ajusting cart item,
    - to 0 and then submitting, the cart page is reloaded showing the item removed.
    - 12 and then submitting, the cart page is reloaded showing the values changed accordingly.

- Upon clicking the checkout button from cart page,
    - with items in my cart, I am brought to the checkout page.
 
- If logging out with items in my cart, the cart items are removed.

- Upon being redirected to the checkout page,
    - I can see my the feature vote detail one last time but I can't reajust them from this page.
    - I can see a form to to add all relevent details for purchasing the votes.

- The correct input info needed for the payment details form on the checkout page, in which will return feature lisitngs page with a success message and will remove the cart times (in which now would have added votes):
    - A real or fake address and post code (usually a 5 digit number)
    - A the Stripe fake credit card number 4242424242424242, security number 111, and a date later than the current date (usually a year later).

- The wrong payment info is giving console errors. Needs to be fixed!!

- When going back to cart page from checkout page, without having submitted payment, the cart items are still there.

- When opening the charts page, 
    - I see two charts available for display with multiple buttons above each, aswell as a description at the top.
    - The first chart set shows how many bugs and features are worked on, in which the three buttons to allow me to toggle between average per day, per week, and per month. 
    - The second chart shows the current highest voted bugs and features with buttons to toggle between both. 
    - There is a clear indication of which data has been activate because, the button associated with the displayed data is deactivated, and has a different color background, and not hover color scheme. 

- When toggling chart date, the graph fades out and fades back in with the new data displayed. I get a clear understanding of how to toggle between data sets. The two main graphs are neatly separated.

- Upon opening the blog page, I can see all of the news posts separated by their dates, titles and a line below each, and with the most recently posted seen first.

FINISH HOW THE NUMBERS ARE DISPLAYED.

- After opening the news blog page, I want to be able to view all news reports, with the most recent first shown.


## Django automated tests

- With permission from the tutors, I used the other resources for to cover the testing. I used:
    - Michael Park's [django-retroplay repository's](https://github.com/mparkcode/django-retroplay) testing files, from it's Accounts, Checkout and Cart apps.
    - I consulted with tutors Michael and Nakita from May 28th until June 5th, to try and implement the tests for these Apps.
- Video tutorial material (All from the Full Stack Frameworks with Django) used for helping me test posts, views, models, etc.
    - The Testing Django tutorial from the Beginning Django section from Aaron Sinnott. 
    - Creating and testing product models video from the Ecommerce mini project tutorial from Niel McEwen.
- Stackoverflow posts used for reference.
    - For creating and testing [fake user login instances and login sessions](https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django) courtesy of SOF member andreaspelme.
    - For testing [Form posts](https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django), courtesy of SOF members Filmm and Shane.
- I set out to cover as much of the code as possible. I tried to get atleast of 90 percent of code that wasn't as easy to test manually.
- After doing initial bugs, accounts tests I started to use Coverage while testing. I noticed that resources I used did not test everything.
- I tested models of bug posts and bug comments. However, while using Coverage while testing features I noticed that I didn't need to test the models as the model calls from testing feature views was enough.
- For Blog, Bugs, Features and Profile app views, I testing the majority of the code. The counts variables (usually for post count display numbers) haven't been tested as they are not of priority and are easy to test from manual testing.
- Fully tested the rest of accounts app except for the for backends file.
- Fully tested the rest of bugs, features, blog app main files where it was needed.
- For Charts views, I initially just tested the the get charts view. I covered the other global reusued variables by calling them within the tests, and creating fake instances of bug posts and timezones. Did not use feature posts as it was not required. 
- Tested Cart completely.
- Only partially tested Checkout because it is using stripe code.
- For testing the majority of the postings.

## Occured bugs

- Stripe Post requests.
    - Received 402 error in JavaScript console. Attempted to catch this error on static/js/stripe.js through try and catch JavaScript, but it turns out its an error from Stripes end on their own JS file.


