# Future Plans

## Bugs to fix

- In creating defensive programming, 
    - in attempting various form posts, where you shouldn't have current access to, I redirect the user to another page. 
        - Some redirects are not bypassing the error where 'CSRF token is missing or incorrect', currently found when falsly trying to post from. I plan on catching the CSRF error from the code, to make it more defensive. Potentially using Try and Catch
            - login and register posts as an already logged in user.
            - Potential more situations, need to to keep testing application under various circustances.
        - Some messages dont appear on redirects such as,
            - As a logged out user 
                - When logging out again, going to checkout page, making a checkout request.
                    - I am redirect to login page without a message. For this I need to re-analyse this code of these views.
    

    

## Features to add

- Create a page to demonstrate the rules, terms and conditions of website. The Rules for Users section of this readme document (below) will be shown on it along with other terms and conditions.
