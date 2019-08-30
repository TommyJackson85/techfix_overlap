# Testing

## User Tests

These are done in reflection of the Readm files user stories, but observes other UX experiences.

- Website has been tested on Chrome, Firefox and Safari. The website looks very simular on all browser but there were no error.
- All active buttons / links change color or tone when hovering over or clicking.
- All text is differentiated from the backgroung making it easier to read for the user.
- text that needs to be highlighted is a different bright color to attract my attention, which is helpful.
        - For example, on a post detail page that belongs to me, it tells me, this is your post! in bright green text. 

- From navigating the whole website, I found
    - All various sections, buttons, are separated where needed, through different backgrounds, colors and borders.
    - All pages have a nav bar and footer which are constantly available and provide links most the main sections of the site. I know I can scroll to the bottom or top to navigate the website.
    - navbar and footer always contains links for charts, blog, bugs, features and cart pages. For logged in users, they also contain profile and logout links.
    - For logged out users, they also contain login and register links.
    - Having these differences, helps tell me if I am logged in or logged out.
    - On mobile width, the navbar links are located in a drop down box which is accessable from clicking the drop box icon. 
    - All active links/buttons are working and change color upon hovering and clicking, telling me they are working. 
    - Each button associated with a specific page, brings me to the page upon clicking, unless I have to be redirected. If I am redirected, most of the tell it leaves me a message telling me why. I can still access the nav bar for other links.
    - I am always greeted with the correct header for the website.
   
- Upon first loading the site, as a logged out user, I am located to the home page, which shows the following,
    - The website masthead / header with Login and Register links/buttons and message telling me what I can do as a logged in user.
    - A welcome message, introducing the website, which suggests me to look at the Charts page for further details.
    - Examples of recent bug reports and feature requests in a side nav, which gives me an idea of how what is done on the website and tells what was recently posted. 
    - Recent news on the website, which refers me to the full news blog page for further news.
    - I get a good strong introduction to the site for this page.

- If logged in,    
        - A message welcome me (my user name) back is seen though out the site on top of most pages except login and registration pages.
                - This always tells my im logged in.
                
- Upon revisiting the home page as a logged in user, the following changes to the page can be seen
    - a Create Bug Report and Create Feature Request buttons on the masthead, instead of the Login and Register buttons.

- On loading registration page.
    - I am first suggested to Login instead, if I already have an account, followed by a login link/button.
    - I can see the registration form, requiring an email, username, password and password confirmation.
- Upon going into the login page, 
    - I am first suggested to Register first if I haven't done so, followed by a registration link/button.
    - I can see the login form, requiring my username and password.
- Upon confirming registration..
    - If succesful, I am brought to the profile page, officially logging me in aswell, with a message telling me I succesfully logged in.
- Upon confirming login..
        If succesful, I am brought to the profile page, and greeted with a message.
- Upon attempting to register OR login,
    - If required inputs are missing, It alerts me without reloading the page.
    - If its a failed attempt, the page reloads with a message telling me what happened.

- If post status is Done, but from other pages I access to an editing form of page, the post page with buttons and comment form (originally from a time when it was To Do).
        - If clicking Vote on bug post, I am redirected to the post page, telling me I cant vote for a Done post.
        - If clicking edit and/or delete on both posts (delete excluded from Feature posts),  I am redirected to Post telling me I cant edit or delete posts that are in progress or finished (same result from a post that was Doing). 
        
- Upon opening the bug reports and feature requests listings pages,
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
    - The header tells me if its a Bug Report or Feature Request page. 
    - First provided with an optional search bar, which allows me search another topic bringing me back to the listings pages.
    - I am provided with the full details of the post title, description, status, user who created it (will tell me its mine if im logged in and if its mine), status, published date, the countings of likes, views and comments.
    - the list of full comments below the details of post.
    - a 'Back to top' button (located below the comments), in which on clicking brings the user back to the top of page through animation.
    - a set buttons (above comment form) related to what I am permitted to do with the post,
        - a back to listings button (for all users) , which brings the user back to the listings page (bugs report or feature request listings page).
        - if logged in, 
                - a vote button is available if the post status is not 'Done'.
                - if post's status is not 'Done', a comment form in which drops down on clicking a button. 
                - If it is my post,
                        - A edit button for 'To Do' status posts
                        - A delete button for 'To Do' status bug posts only.
        - if logged out,
                - if post's status is not 'Done', a login button link is seen.
                 
- Upon voting for 
    - bug reports, I am brought back to the bugs listings page.
    - feature requests, 
        - I am prompted with a pop up money form, telling to submit money to vote, while also telling me how it works (i.e. 10 euro equals 1 vote). Upon suggesting amount to give, in order to vote, I am brought to the checkout page.

- in cart page, Upon amending cart items' euro adding
    - to 0 or leaving the input field empty, the item is removed after clicking amend.
    - to a number greater than 0, the page is reloaded showing the changes.

- For posts in all drop down panels,
    - they are further destinguished by their status cateogories through different colored status labels (Red for To Do, Yellow for Doing, and Green for Done), in which is particularly useful for the profile page where they are all mixed together.
    - They contain all details of the post, but a shortened title and description. 
    - a view button is included to access the detail page.
    
- from bug post panel displays and their detail pages,
    - if the post's status is 'To Do', Edit and Delete buttons are available.

- from feature post panel displays and their detail pages,
    - if the post's status is 'To Do', an Edit button is available.
    - total money donated to create amount of votes is seen.
    
- If a feature report or bug post status is 'Done', then buttons and the form, in which alter posts, are removed.

- Upon loading the cart page,
    - as a logged in user 
        - I am prompted with the option to adjust my current payments of my submitted features and a cost summary.
        - the checkout button is available if there are items in the cart.
        
    - as a logged out user
        - I view an empty cart, and I am prompted to Login or Register to use the cart.

- Upon ajusting cart item,
    - to 0 or emptied input, and then submitting, the cart page is reloaded showing the item removed.
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

- When going back to cart page from checkout page, without having submitted payment, the cart items are still there.

- When opening the charts page, 
    - I see two charts available for display with multiple buttons above each, aswell as a description at the top.
    - The first chart set shows how many bugs and features are worked on, in which the three buttons to allow me to toggle between average per day, per week, and per month. 
    - The second chart shows the current highest voted bugs and features with buttons to toggle between both. 
    - There is a clear indication of which data has been activate because, the button associated with the displayed data is deactivated, and has a different color background, and not hover color scheme. 
- When toggling chart date, the graph fades out and fades back in with the new data displayed. I get a clear understanding of how to toggle between data sets. The two main graphs are neatly separated.
- All charts keys and values are displayed without having to click the graphs, but clicking the graphs also shows the values and keys.

- Upon opening the blog page, I can see all of the news posts separated by their dates, titles and a line below each, and with the most recently posted seen first.

- The blog page link is located below the charts on the charts page, and a charts link is below the blog page.
        - Both pages inform me alot about the site.
 

## Code logic of average charts

- Manually tested average charts monthly averages.
    - Went 3 sets of 30 days back from current date, while going through each bug post.
        For each 30 days
            - If the dates overlapped with post start and end dates, I would add one to a whole number. 
            - Would then divide the collective number by 3 (for 3 months).
    - I didn't do the same for weeks because it follows the same logic but with 7 instead of 30.
    - Officially tested on the 29th of August, with returned results of an average of 3.33 bugs worked on per month.

## Passing code through automated testers.

- stripe.js, each_post_detail.js, charts.js files all pass JSHINT.
- Tested all my HTML files in the [w3 validator](https://validator.w3.org/).
        - Make relevent changes when ever I could. 

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
- For Blog, Profile Bugs and Features app views, I covered the majority of the code. The counts variables (usually for post count display numbers) haven't been tested as they are not of priority and are easy to test from manual testing.
- Fully tested the rest of accounts app except for the for backends file.
- Fully tested the blog app main files where it was needed.
- For Charts views, I initially just tested the the get charts view. I covered the other global reusued variables by calling them within the tests, and creating fake instances of bug posts and timezones. Did not use feature posts as it was not required. 
- Tested Cart completely.
- Only partially tested Checkout because it is using stripe code.
- My initial plan for Django testing was to cover all the code and anything relevent that can't be tested manually.
- As I have now also manually tested my my website, the next stage is to test, specific parts of view / model functions covered.
        - i.e. through assertEquals functions.


## Unfixed occured bugs
 
- CSRF verification failed. Request aborted, Python page error page.
    - When another user is logged in, and when attempting to post, on a different / previously logged in account, from forms:
        - login, registration, edit/create, comment, feature donations
        - each form doesn't redirect to their respective pages.
        - I am receiving "CSRF verification failed. Request aborted" on an error page.
        - Clicking back from Chrome browser, brings me to page I was supposed to be redirected to.
        
        - Quite common on the Chrome browser but for Firefox and Safari, it is more varied.
                - For example, when creating a bug report, but another user is logged in (thinking it is my own account), the post is done from the users account, and not my.
                - they get the error from attempting logins and registrations, when another user is logged in.
        - This is a very sponataneous error, it will need to be tested more.
        - Looking at ways to catch the error aswell, through defensive programming.

- Sticky css position doesn't work on Safari.
    - Originally wanted to have a sticky comment form with other buttons.
    - Looking at alternatives to position 'sticky' such as from this [Stack Overflow Post](https://stackoverflow.com/questions/51792783/safari-positionsticky-not-working-in-an-overflowauto-element).
    - However, in heinseight of other user feedback, I may not go back to it. Maybe include a modal popup instead, from a sticky button, if I decide to do it.
    - As of now, it is a regular drop down form and the other sticky buttons have been moved to other areas (scroll to the top button is now at the bottom of the details page below the comments.).
    
- Users can vote for 'Done' feature requests, if the feature donations modal is available to them or by calling the add to chart function with specific reference to the posts id.
    - From the cart and checkout page, I will add more defensive design, in detecting cart items that are already finished. 
    - This is hard to do because the add to cart and adjust cart refer to the items ids and not the whole feature and are linked to a session. 
    - Attempted to pass in the full feature on the add to cart function (instead of feature id) from the features detail page but it was bringing up page errors.
    - I will do simular defensive programming, in relation post statuses.
    
- Stripe Post requests.
    - Received 402 error in JavaScript console. Attempted to catch this error on static/js/stripe.js through try and catch JavaScript, but it turns out its an error from Stripes end on their own JS file.
    - This is not full filling the ecommerce requirements but its the fault of Stripe.

- Reset password page.
    - Due to a significant error on reseting passwords with google email account, I had to remove the reset password button from the login page.
    - When using the the reset password function on a gmail email, it returns a Django error to do with google account authentication.
    - Will consider catching the error on login, and reloading the login page with the error in an error popup.

- Timezone issues
    - My Mentor spotted this issue when attempting to create a post. The post's publishing date was in UK time only because it was stored as a string.
    - Was suggested to use the [time library](https://stackoverflow.com/questions/1111056/get-time-zone-information-of-the-system-in-python) to try and fix this.
    - On a second meeting with mentor, he said he said the issue seemed to be fixed.
    - Will retest this issue again to double check.

- User experiences.
        - I get mixed reactions from the color tone of my sight, some like it others don't.
        - I am trying to tone down the color schemes as much as possible.
        - The comments section needs better design of color schemes. When I bring in user images, it will help make user comments feel more personal, being able to see an individual picture.
        - At the moment, it is jus the user name in bright green text.
        - Panel drop down items need to be ajusted aswell. On ipad width screens, they get too big for the amount of text and information in them.
        - This is one of the downfalls of Bootstrap. Their small columns are quite big compared to their extra small columns.
        - Will pontentially allow more text to be in the panel items from, and maybe uses media queries to help fix this.
        - Add better images. The Masthead image is just a prototype to get the correct feeling of the page.

- Made more of an effor to implement HTML Semantics in my project, using Headers for hierarchy.
        - I need to fix the structure of my sections, side navs. For example, my Side Nav is located in my main section.
        - I didn't do any major changes to this, due to lack of time, and I was a afraid I would break the code.
        - I had the wrong Idea how to implement headers too. Need to fix this.

- Github repository currently has a severe Django error and pycrypto error.


## Fixed occured bugs

- unwarrented user actions.
        - I used defensive programming techniques for this. 
        - Attempting to edit (entering a link posting from a form), delete a bug post when the post status is "Doing".
                - I am brought back to the post, explainin the error. The post page is now updated correctly. 
                - Initially might of happened if the page was at To Do status recently.
                - Same errors might occur for Done statuses, in whiching commenting and voting on the post will bring the user back to the page.
        - If logged in, 
            - but login and register links/buttons are available on an already loaded page
                - clicking the login and register buttons will redirect me to the index page, telling me to logout first.
        - If logged out, 
            - but profile links/buttons are available on an already loaded page
            - but bug report detail page is already open with links to vote, delete, comment
            - but feature request detail page is already open with a link to comment, modal pop up to vote (with money in input)
            - but bug report/feature request edit or new form is open,
            - but cart page is open, with items and their adjust buttons available, aswell as the checkout button.
            - but checkout page is open, with the form filled in correctly and the confirm checkout button available,
                - activation any actions these places, where being logged in is required, redirects me ot the login page, telling me to login.
        - I have manually tested these situations in all browsers, but it would be no harm to continuously do user tests on these situations as they are complex and come from places you don't expect.


- Issues testing Bugs and Features when referencing a user id. When adding more defensive programming in relation to seeing if post belonged to user, i had trouble.
    - Trying to link foreign user key of a post to the current logged in user was difficult.
    - But I figured it out by referencing the pk value of a post, regardless if its a fake instance.

- Installed a pip3 Jasmine package in which automatically updated Django to 2.2.3 which only supports Python 3.5.
    - Created errors in running the App on AWS Clous 9 (in which only runs on Python 3.4), detecting import issues.
    - Fixed by installing Django 1.11.17 instead.
    - Removed Jasmine package.

- Running migrations after changing models.
    - After making multiple model changes, calling make migrations, didn't update them all.
    - Initally tried to reset and delete the entire database from Heroku, ran the console from Heroku to try and solve the issue.
    - Used this [migrations reset tutorial](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html).
    - This error had taken alot of time from me, but I managed to fix it once I discovered I had to keep calling make migrations for each saved change.

- Errors in running Stripes test bank number 4242424242424242 to payment form on checkout page.
    - I had to renew my Stripe keys as they were from 2016.
    - I discovered I had to include a later date as an expery date.