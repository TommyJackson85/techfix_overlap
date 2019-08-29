# Your Project's Name

Techfix Overlap is an organisation dedicated to futher developing and building the Python framework Techfix.
Our website is for users to report bugs in the framework and suggest new features for it, through the user of the forums. 
Users may search for other bug reports or feature requests and may vote in favour of them.
They will only have to pay for features. Our team of developers and administrators will constantly check on new posts from users and will work on the most voted for. Users can see which are currently being worked on or which are finished.

Under certain circumstances users will be able to edit, delete or comment on posts. We will have a team of moderators to look out for users who don't obey the sites rules.
On searching and viewing post listings, all posts are split by their current status through panel dropdown boxes, i.e. posts that are finished being worked on are separated by posts in progress or waiting progress.
This allows users to open and close panels as they choose, helping them break down what they are looking for.
Our comment form is constantly accessable when reading through comments, allowing for a dynamic comment posting system.
We are always seeking new innovated ways provide the best user experience as possible to increase the reliance on our site for Techfix developers. So far, we are getting strong feedback from users on our website.

We are a new organsistion, but already have a strong active user database due to our progress in responding to user requests.
We provide constant updates from our home, charts and blog pages. These pages are also usfull in attracting new developers to use the Techfix framework.

Travis Testing Build Status:
[![Build Status](https://travis-ci.org/TommyJackson85/techfix_overlap.svg?branch=master)](https://travis-ci.org/TommyJackson85/techfix_overlap)

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.
In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

- For my main home page, I took alot of inspiration from the [Stack Exchange website](https://stackexchange.com/), particularly in its home page structure, layout and color scheme.
    - Evidence of this,
        - the structure of homepage.
        - A removable introduction which provides links to another page to "learn more".
        - Shows recent posts.
        - the header / nav bar, footer, background color.
        
- Much of the color schemes were hence brought onto the rest of the website, to keep it consistent.

- Used [StackOverFLow](https://stackoverflow.com/questions/tagged/php) for examples on how to display search results previews (i.e. the listings of forum posts which might show only a portion of the text as a preview).
    - Helpful with developing listings of bug reports and feature requests, when trying to show as much information as possible in each.
    - The sites postal listing are still different in structure, design and purpose.

- Wire Frames and Designs.

- This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.


### User stories to follow.

- As a user on all pages, 
    - I want constant access to the
        - to the nav bar when scrolling to the top of the website.
        - to the footer when scrolling to the bottom of the page.
        - links of most the main pages of the website, from both the footer and nav bar.
        
- From the nav bar and footer
    - links to home, bug reports, feature requests, blog, charts, cart are constantly accessable.
    - links to login and register pages are accessable if logged out 
    - links to profile and logout are accessable if logged in.

- As a user upon opening the homepage I want to be 
    - welcomed with a mast head and a brief 'about' section of the website, which will contain a link for further information about the site. 
    - able to have the option to be remove this about section, if I have read it already.
    - provided with links to create a bug report or feature request if logged in as a registered user. 
    - provided with links to login or register if logged out.
    - able to view recent news and be a provided with a link to the full news blog report
    - able to view links to new bug reports and feature requests and be provided with brief details of each.

- As a user upon opening the bug reports and feature requests pages, I want to be 
    - provided with a search bar which when used will help break down my search results by key words in the postings titles, and returns the most recent first.
    - provided with three drop down accordion boxes, which separate the search results by their current statuses (To Do, Doing, Done). They can be toggled between closed and opened upon clicking, and the amount of returned results is shown on each drop down bar. When opened, all posts are displayed clearly for me.
    - provided with overview details of each post, including the amount of views, comments and votes (for features, it will include amount of money provided for the votes), user who posted it (will tell me if its mine if logged in), date published and atleast the start of the title and content.
    - provided with a view button on each displayed post for all users, an edit button on all posts with status of 'To Do' if its my post, and a delete button for bug report posts with a status of To Do, if its mine.

- As a user opening profile page, I want to be
    - provided with two drop down accordion boxes, which separate the feature requests and bug posts I created. The posts of different statuses are clearly separated within the dropdown boxes.
    - provided with a 'Create Bug Report' button above bug listings, and a 'Create Feature Request' button above feature listings.

- When clicking logout, I want to be returned to the home page as a logged out user.
- When opeing the login page, I want to be provided with a login form, and two alternative links/buttons for registration and password reset, and any helpful guides.
- When opening the password reset page, I want to provided with the necessary input fields for this procdedure.
- When opening the registration page, I want to be provided with a registration form to input my name, email and password of choice. 
- Upon confirming my registration or password reset, I want to be redirected to the login page.

- As a user, upon opening individual bug report and feature request detail pages, I want to be
    - provided with a full comprehensive detailed page of each post,  including the amount of views, comments and votes (for features, it will include amount of money provided for the votes), user who posted it (will tell me if its mine if logged in), date published and the title and content.
    - provided with a vote button on each displayed post for all users if post is not 'Done', an edit button on all posts with status of 'To Do' if its my post, and a delete button for bug report posts with a status of To Do, if its mine.
    - allowed comment on a post if its not done and to be able to read all comments.
    - able to scroll back to the top of the page through the click of a button, while scrolling through the comments.
    - able to go back to the bug reports and feature requests listings from the click of a button.
    - have the three previously mentioned functions available constantly while scrolling through the comments.
    - I want to only have to pay for feature request votes, through 
- For both bug posts and feature posts,
    - I want to be able to create or edit a post through a simple form, after clicking a button.
    - when saving a comment, edit or new post, I wan't to brought to detail page of the post.
    - when deleting or voting for a post, I want to be brought back to the post listings page.
    
- The only votes I want to have to pay for are votes for feature requests.
- I want a clear description of how to pay for votes before prodeding to the cart or checkout page, as constant reminder.

- When opening up the cart page before proceeding to the checkout page,
    - I want to be able to adjust my payments of votes for each feature request and 
    - I want to be able to remove them by #####FINISH MAYBE ADJUST THIS PAGE

- After proceding to the checkout page, 
    - I want to be able to view my cart of items one last time, before purchasing.
    - I want to be told when my payment details are incorrect or missing, when attempting to pay.

- After opening the charts page,
    - I want a clear simple description of the charts displayed, where it is needed.
    - I want to be able to able to toggle between different data displays, and want to the toggle changes clearly displayed to me, wether its through messages or animation.
    - I want to able to clearly view all chart data as much as possible, with the values displayed as the main priority, and as much of the titles shown as possible.

- After opening the news blog page, I want to be able to view all news reports, with the most recent first shown.

## Features

### Pages' layout and Existing Features

- Buttons
    - Links on nav bar and footer blend in with the background but change color on hover. 
    - Most of the other buttons are green with white text.
        - Green is the primary button color, usually will lead user to another page. 
        - Blue is the secondary button color. I used it for buttons that dont render the page, but interact with the dom (charts page). Also used for panel drop downs keeping it consistent. 
        - Light Blue is the third color choice, used for form submit buttons.
        - Red is the forth, used as sticky buttons, (in which mover when user scrolls.)
        - Yellow, is to represent a disabled inactive button, like on the charts page.
    - On hover or click they change to a different tone of its color with usually yellow text. This is to show they are interactive.

- Index / home page structure
    - Designed to 
        - introduce the website to new users. Introduction alert gives overview of websites purpose, and is removable from clicking the 'x' (useful for returning users).
        - update all users on.. 
            - news. 3 of recent full blog posts on main section as a priority. Link to full news blog found below news. 
            - recently posted bugs and features (5 of each section), in the form of links (to each full post detail).
   
- Bug Reports / Feature Requests listing pages layout.
    - Having a search bar in the header allows users to break down results, returning only posts with titles containing the search term. Searching an empty string returns all results.
    - Splitting found results by their statuses (Done, Doing, To Do) into toggle drop down boxes was a priority for these pages.
        - To show how much work our team puts into delivering what the customers want (from the Done and Doing boxes).
        - To give better navigation for the user and to break down search results. i.e. returning users might prefer to find recently posted posts.

- Profile page
    - Inherits the same structure and use of panel / dropdown boxes, but splits all users posts by features and bugs.
    - Includes Create Bug Report and Feature Request buttons (abover their respective panel).

- Panel drop down boxes (found in Bug Reports / Feature Requests / Profile pages)
    - The number tags on the dropdown panels allow users to get an overview of the amount of returned results, 
        - helpful for substantial returned results or when a user searches results.
        - Each returned post in the panel drop down box is in a ticket design, showing most details but only the start of the title and description.
            - Also contains 
                - view button.
                - euro donations for votes number tag for features.
            - have associated color tags for their current status, i.e. 'Done' posts have a green status tag.

- create and edit post forms (for both bugs and feature posts).
    - both forms inherit the same structure, but the edit form inherits the post details available for edit.

- post details pages for bugs and features.
    - each are accessable from panel post view buttons, and links in the home page.
    - Intitally shows an optional search bar if user wants to find another topic (kept above page header to make it feel separate.).
    - Gives the full comprehensive details and updates (views, likes, and comment count) of posts, comments list, and comment form with some further navigation buttons.

- comment form and extra navigation buttons (from details pages).
    - These are constantly stuck to the screen when scrolling through comments, to allow users to have constant access.
    - navigation buttons included are the 
        - 'Back to top' button, scrolls user back to post details.
        - 'Back to listings' button, redirects user back to post listings to find another post.
    - as a logged out user, the comment form is replaced with a login page link, suggesting user to login to allow comments.
 
- cart page layout
    - rules are provided at the start. 
    - Checkout button available if logged in and if you have added money to items. If logged out, a loging button is available.
    - Cart items tell you how much has already been added to each item. They allow you to adjust the the money donations, and you can remove items by adjusting to 0 or adjusting from a blank input.

- checkout page layout
    - checkout times are consistent in design with the cart page items but donations cant be adjusted here.
    - the checkout form works with the fake stripe credit card number 4242424242424242 and a later expirary date.

- charts page layout
    - designed to advertise the website and provide further information on our teams progress and user involvement.
    - contains a brief description, and two base charts in which,
        - users can toggle between different data sets from pressing buttons.
    - First chart demonstrates average amount of posts worked on by developers (user toggles data between daily, weekly and monthly averages).
    - Second chart demonstrates top 5 highest voted posts (user toggles data between bugs and features).

- blog page layout
    - designed to advertise the website and show recent news on the Techfix framework.
    - shows the full news blog with the most recent from the start in a simple layout. each post is separated by their title and an underline. 

### Features Left to Implement

Please refer to the [Readme Future Plans Document](https://github.com/TommyJackson85/techfix_overlap/blob/master/README-FUTURE-PLANS.md).
It covers all future plans, code to be fixed, .

## Rules for Users

- rules for posts as a logged in user.
    - you can post comments on them, 'vote' for them, if their status is not 'Done'.
    -if post is yours and still at 'To Do' status.
        - edit button/link available
        - delete button available for bugs.
    - voting button only available from the details page to make sure the user has full knowledge of post.
    - voting for features must be done through payment. A pop up appears on clicking the vote button, telling you the rules and showing an input form for euro input.
    - After submitting suggested amount, users can still adjust payments from cart page, or remove them.

- Rules of post votes and statuses
    - if another post of 'To Do' status exceeds a post of 'Doing' status in Votes, it becomes more of a priority.
    - our developer teams may take a break from a post to focus on a more prioritised post, depending on the circumstances of their current progress.
    - because of this rule, we allow users to vote on posts constantly, as long as they are not of Done status.  


## Administrators and Developers Guide

- Each team of administrators and developers is set on regular tasks each work.
- Administrators will activate use and refer to the admin page of the site on a daily basis.
- There are teams to deal with either Bug Reports or Feature Requests, but never both.
- On choosing the next post of a user to work on, the administrator to proceed to find the most voted first. The administrator must turn a post's status to Doing, and activate the start date to 'now'.
- If another post becomes higher voted that the post they are working on, 
    - a team may decide to stop working on the post and proceed to work on the higher voted, all under certain circumstances..
        - If the post is in the early stages (less than 50% complete), and finished its current stage (i.e. planning, analysing). 
    - a team may split, with one half working on the new prioritised post,
        - If the post does not require attention from all members.
- The team leader must make these decisions themselves.
- Regular team meetings should take place, once or twice a week.

## Technologies and Code base Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Heroku Posgres](https://www.heroku.com/postgres) database system.
    - Used for storing data for user accounts and posts.
    
- [Django](https://github.com/django/django) used as the main frameword for the website. Specifically used for
    - rendering templates; creating models, urls;
    
- [Bootstrap 3.3.7](https://getbootstrap.com/docs/3.3/) was used for, 
    - the majority of the html templating, post displays, post icons.

- Bootstrap 3.4 html templates which use Bootstrap's JavaScript code.
    - [Modal pop up](https://getbootstrap.com/docs/3.4/javascript/#modals) was used for the prompting users to pay for feature posts on feature detail page.
    - [Collapsable content](https://getbootstrap.com/docs/3.4/javascript/#collapse) was used for the the panel drop downs and comment form.

- [Font-Awesome 4.7](https://fontawesome.com/v4.7.0/) libary for used for nav bar and footer icons and maybe for other features.

- [JQuery](https://jquery.com).
    - Used to simplify DOM manipulation and to add animation transitions.
        - Used for transitioning between different chart displays on charts page.
        
- [Chart js doughnut charts](https://www.chartjs.org/docs/latest/charts/doughnut.html).
    - Used as main charts to display data for charts page.

- Video tutorial material (All from the Full Stack Frameworks with Django).
    - The Testing Django tutorial from the Beginning Django section from Aaron Sinnott.
    - Deployment tutorial, by Aaron Sinnott, 
        - as a guide to set GitHub with Heroku.
    - Authentication & Authorisation tutorial from Aaron Sinnott.
        - Used the Accounts app for setting up user registraton and connecting to the backend.
        - Blog all about it tutorial, by Matt Rudge.
            - Used the structure and code base of the blog posts for my own bugs, features and blog apps.
        - Ecommerce mini project tutorial from Niel McEwen.
            - used most of the code the for the cart and checout pages.
            - Creating and testing product models reference.
            - for reference in setting up AWS buckets and for storing static files on AWS.

- Stackoverflow posts used for reference.
    - For creating and testing [fake user login instances and login sessions](https://stackoverflow.com/questions/7502116/how-to-use-session-in-testcase-in-django) courtesy of SOF member andreaspelme.
    - For testing [Form posts](https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django), courtesy of SOF members Filmm and Shane.
    - For [dispaying fields from Models in Django Adminstration pages](https://stackoverflow.com/questions/10543032/how-to-show-all-fields-of-model-in-admin-page), from SOF user Amirshk.

## Testing

Please refer to the [Readme Testing Document](https://github.com/TommyJackson85/techfix_overlap/blob/master/README-TESTING.md) for all testing.
- The document covers Manual User Tests, Automated Django Tests, and Bugs I have come across.

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

Your README describes the deployment procedure including settings files, 
environment variables, dependencies and any other differences between the dev and live versions


If you have created an automated script to help deploy the project,
you should include it (or link to it) in your write-up.

- I set up the website for deploy from.
    - GitHub repository to contain the files.
        - made an in initial commit to load files. 
        - kept a requirements file for hosting, containing all required packages.
        - [GitHub files here.](https://github.com/TommyJackson85/techfix_overlap)
    - Heroku app to deploying and hosting the website and contain the database.
        - deployed from connecting it to the github repository.
        - stored Stripe keys, AWS bucket name and keys, and the database URL into Heroku's config logs.
        - encountered issues due to false packages, had to delete some from the requirements file, re commit to GitHub. 
        - set up automatic deploy on Heroku, so that each GitHub commit re deploys the website automatically.
        - [Deployed here.](https://techfix-overlap.herokuapp.com/)
        - attached Postgres database in Heroku Resources.      

- For development version of the site, AWS C9 uses an env.py file to hold Stripe keys, and AWS bucket name and keys and the database URL.
- manage.py is used to import Django.
- From the settings.py
    - The website has the option to allow the use of sqlite if the postgress database can't be found.
    - receives the AWS bucket name and keys and Stripe keys.
    - with custom_storage file, receives the static files, during a collect collecttatic command, and hosts them to AWS. All images and style sheets and JavaScript files are hosted to AWS.

- 'Run' from the AWS C9 project folder will run the project locally.

- Had to move from the old Cloud9 website to AWS C9 when the old one seased to exist.
    - This took time to configure, and went through various tasks to fix it:
        - Had to pull changes from GitHub before pushing.
        - add 'run 'Alias to bash_alias file.
        - Installed packages that were missing.
        - Added AWS to allowed hosts variable in settings.py file.


This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

## Credits

- My mentor Moosa Hassan.
- The tutors at Code Institute.

### Content

- All text based content was written by me.

### Media

- [Computer circuit board image](https://www.istockphoto.com/ca/vector/computer-circuit-board-seamless-black-and-white-technology-background-gm181167778-27262185), by Bubaone. Further credit to istockphoto.com.

### Acknowledgements

- I received inspiration for this project from
    - [Stack Exchange website](https://stackexchange.com/)
    - [Stack OverFLow](https://stackoverflow.com/)