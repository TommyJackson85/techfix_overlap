# Future Plans

## Code to clean

- In creating defensive programming, 
    - in attempting various form posts, where you shouldn't have current access to, I redirect the user to another page. 
        - Some redirects are not bypassing the error where 'CSRF token is missing or incorrect', currently found when falsly trying to post from. I plan on catching the CSRF error from the code, to make it more defensive. Potentially using Try and Catch.
            - login and register posts as an already logged in user.
            - Potential more situations, need to to keep testing application under various circustances.
        - Some messages dont appear on redirects such as,
            - As a logged out user 
                - When logging out again, going to checkout page, making a checkout request.
                    - I am redirect to login page without a message. For this I need to re-analyse this code of these views.
    

- The bug and feature posts/comments models, use alot of the same values and functions. Alot of their html templates are simular too. I will ceate a User Post app, in which will contain all the code and templates that both features and bugs have incommon.
    - Any data in the models that is relevant to multiple apps will be shared, rather than duplicated.
- This new app would then be imported into the bugs and features apps, in which it might be altered.
    - Examples of differences which would still have to be implemented from the
            - the features app..
                - The votes cost variable, the modal pop up on the detail page.
            - the bugs app..
                - The delete button and functions, the vote functions.
        - To implement these differences,
            - Create html blocks from the user post apps html files, in which I would utilise template inheritance practices, by linking/referencing blocks from the features/bugposts html.
            - Make all the post apps view functions global variables, and calling them (while giving them the collect values) from the features/votes html files or view files.
            - Add new keys to the global functions.
        - For the sake of keeping my code clean, I main not keep all my code clean.
    - I was originally considering doing this first, but I thought it would be cleaner the way it is now, and I was unsure of how different the features and bugs may become while developing them.

- Setting up a Jasmine testing environment
    - I was considering testing my JavaScript through Jasmine test but decided not to do it yet
        - I was worried about running into bugs, and I needed to find a good documentation on setting it up in a Django application.
        - Manual testing has been enough so far in testing the JavaScript Frontend elements of my project.
        - I am considering using [django-jasmine](https://pypi.org/project/django-jasmine/) or just setting up a regular HTML file for testing JavaScript.


- Update Bootstrap 3.3.7 (it is currently legacy) to Bootstap 4 or a newer better framework.
- Use a more updated version of jQuery and Font Awesome.

## Features to add

- A page and/or modal popup to demonstrate the rules, terms and conditions of website.
    - Would add a requriement in the registration form for new users to agree on them and to tick a box in agreement.
    - A link to a registration page might be provided at the bottom.

- Simular to the home page's removable introduction box, I may also include other removable details boxes such as.
    - Rules of posting comments and new posts, to be located at the 
        - bottom of the home page.
        - top of the bugs and features listings/details/form pages.
    - Guide to payment processes, to be located at the
        - top of the cart and checkout pages. This will replace the guide details on the cart page.

- A more advanced [Navbar with drop down functions](https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_navbar_collapse&stacked=h).
    - To make the create bug reports or create feature requests lists constantly accessable for logged in users, I would keep them in a drop down link list underneath their respective listings pages (i.e. create bug report will be located underneath the bugs link.)
    - Maybe add links to Facebook, GitHub and other related pages for the Techfix library.

- A sticky close button within panel dropdown boxes.
    -Simular to the sticky buttons on the bugs/features detail pages, I want to have a close button constantly available in the panel dropdown boxes.
    - A simple 'X' on a red circle would do, would be faded but shows full opacity on hover.

- Changes to panel items in panel dropdown boxes.
    - Replace buttons, with associated icons instead. i.e. pen icon for edit, 'X' for delete, eye icon for view.
        - Will help reduce space on the panel items.
        
- Allow the adding of tags, to new bugs/features posts.
    - Create an input form, that would be first of front end use, in which would allow users to drop new tags into a box, in which the tags can be removed from from the box from clicking an 'x'.
    - Using jQuery and JavaScript, this process would done through building arrays of data, in which new values are popped or removed.
    - On saving the new post, the array values are sent to the backend and through a django view function to store the values in the database.
    - On an form, the values are reloaded to the frontend in new arrays, and displayed back in the box.
    
- Make a new search bar available on most pages, to create consistency.
    - It would include a toggle switch in which would toggle between bugs and features search links. I may use jQuery, JavaScript and CSS styling to do this so it doesn't reload the page.
    - Will create it, as its own app and reference/link it through html blocks from most the websites page.
    - I may include it as an attachment to the nav bar or just have it constantly available in the header.
    - I will replace this with the search bars in the features and bugs apps, to allow users to always be able to search both.
    - All page headers will be located below the search bar.
    - I may exclude it from 
        - the charts and blog pages, as these pages will be used for promoting the site only.
        - form pages, as these pages are to be more focused on the specitis.

- Allow users to upload a profile picture.
    - This will be strictly optional, and I may not include it from the registration process.
    - It will be included in the profile page and potentially from the nav bar profile link button.
        - The icon on the profile link will be replaced by the image, in which the image will have a plus sign allow image chages. 
    - All profiles would contain a default image if no image is provided.
    - To develope this, I will try
        - [Max Goodridge's tutorial](https://www.youtube.com/watch?v=tT2JOpfelSg).
        - [corey schafer's tutorial](https://www.youtube.com/watch?v=FdVuKt_iuSI).
    - I will potentially use a modal pop up for the profile changes.
    - Would require alot of defensive programming, from the front end and back end to stop and remove faulty images that create console errors.
        - Would utilise Try and Catch functions for this, and would replace faulty images with the websites default image.
        
- Use Modal popups for logins and registration forms.
    - I might replace separate login/registration pages with modal popups to allow users to register or login from the age they are in.
    - Upon proceeding with registration/login, the user's current page will be reloaded.
    - From page reloads on registration, I may also allow automatic logins, or have a login modal popped up already for the user.
    - Might also implement this for creating posts too.

- Add more charts to the charts page
    - Charts to show top users, who's posts get the most votes. On clicking each user bar would toggle another chart showing the user's top voted posts. 
    - Expanding on the chart that shows how many bugs and features are worked on a period of time, I may had include a calender chart, showing every day of the whole last year, showing many bugs and features were worked on.
        - on hovering over each day icon, it will show many was worked on, and on clicking it will pop up a detail box showing what was worked on.
        - This is very simular to a Github profiles contribution chart.

- Add more links on the footer.
    - I used the current footer to add more links and to make use of the left over space.
    - From here I may also add help and terms and conditions links, and other social media links, once these pages are created. 
    - I might remove other links if I feel is important. While initially building this site, I wanted to make all links as accesable as possible.

- From Home Page, I will add a top users section, showing who the top users on the site are, simular to [Stack Exhange's home page](https://stackexchange.com/).
    - I left this out as there isn't enough users on the site yet. 

## Github issues to fix.

- Static folder was accidently in the gitignore file, so the commits during the development of these files might not reflect on the individual commits, particularly in their messages.
    - Unsure if there is anything I can do about this.
    
- Multiple commits were made to try and solve Heroku errors, particularly during th early stages of project when setting it up, as a result my commit history is not clean.
    - Will attempt to merger smaller commits as one commit, and/or merge them with other larger commits.

