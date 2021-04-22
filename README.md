# ![An egg](media/favicon.ico)   Hire Hens

Do you dream about fetching fresch eggs, from your own hens! **Hire Hens**, is the easy way to live your dream and try out having hens in your own backyard. We will help you with the "how to" and the equipment you need.
 
## UX
### Strategy Plane
#### Site owner's goal
- Sell renting packages including hens and accessories.
- Being able to update the information of the page.

#### External user's goal
- Hire hens and accessories, as coop and dishes.
- Find information:
    - How to hire hens.
    - What a package consists of.
    - How to take care of the hens.
    - How long it is possible to hire and what happens after the hire.

**Site owners need**
- That it is easy for a user to hire hens.
- That it is easy and intuitive to update information on the page.
- Authority to manage information on the page.

**Users** needs:
- Easy and intuitive way to hire hens.
- Easy to find more information about the rental process and how to take care of a hen.

### Scope Plane
#### User stories
(this is not in priority order)
- US_001: As a user I want to be able to sign up to the site. By doing this I have the possibility to add my personal information and thus paying process will be faster.

- US_002: As a user, I want to be able to login to the site.

- US_003: As a user, I want to be able to log out.

- US_004: As a user, I want to be able to look at the site anonymously, without logging in.

- US_005: As a user, I want to build my own rental package, consisting of hens of my choice and having the possibility to add coop and/or feeder and waterer.

- US_006: As a user, I want to add my rental package to a cart.

- US_007: As a user, I want to look at my cart.

- US_008: As a user, I want to checkout my cart.

- US_009: As a user, I want to pay, for the contents in my cart, in a secure way, with a credit card.

- US_010: As a user, I want to be able to buy things even if I am not logged in.

- US_011: As a user, I want to find information about how to hire hens and how to take care of hens.

- US_0012: As an administrator of the site, I want to login with the authority to add, change and delete information on the site.

- US_0013: As an administrator of the site, I want to be able to add, change and delete the type of hens that can be hired.

- US_0014: As an administrator of the site, I want to be able to add, change and delete "hen accessories" as coop, feeder and waterer.

- US_0015: As an administrator of the site, I want to be able to add, change and delete information of renting process and how to take care of the hens.

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

### Structure Plane
- A "homepage" with a picture of hens in a backyard.
- Navbar with:
    - Brand-image that leads to homepage.
    - Link to page where user can put together rental package.
    - Link to page where user can buy eg. food and beding
    - Link to page with FAQ
    - Link to cart
    - Sign up and Login In, or Log Out
    - Profile page
- Rental package-pages:
    - Start with choosing type of hen and number of hens.
    - Then possibility to add coop and/or feeder and waterer.
    - Information of what package consists of and possibility to start subscription.
    - User with administrator authority can add, change or delete type of hens.
    - User with administrator authority can add, change or delete accessories as eg coop, feeder...
- Buy-page:
    - User can buy food, beding and other consumeables.
    - Possibility to add consumeables to cart.
    - User with administrator authority can add, change or delete consumable.
- FAQ-page:
    - Questions and answeres to frequently asked questions.
    - User with administrator authority can add, change or delete questions and answeres.
- Cart page:
    - Information what the cart consists of and possibility to change it.
    - Link to checkout page.
- Checkout page:
    - Possibility to pay with card.
    - If user is logged in,  personal information is given.
    - If anonymous user, user has to fill in information necessary to pay.
- Profile page:
    - Page where user can add and change personal information.

### Skeleton Plane
- The user browses via the navigation system.
- To hire hens, the user is led through the process:
    - first choosing hens (which is mandatory)
    - then accessories
    - add the package to a cart
    - and finally pay for the content of the cart.
- Interactive design that works on Mobile, Tablet as well as Desktop.

#### Wireframes
- [Mobile](https://github.com/Carina-P/hire-hens/blob/master/wireframes/wireframes_mobile.png)
- [Tablet](https://github.com/Carina-P/hire-hens/blob/master/wireframes/wireframes_tablet.png)
- [Desktop](https://github.com/Carina-P/hire-hens/blob/master/wireframes/wireframes_desktop.png)

##### Major changes compared to wireframes

#### Information Architecture
##### Database Choice
- Development phase: SQLight which is installed with Django
- Production phase (deployed): PostgreSQL, provided as an add-on by Heroku

##### Data modell
The data modell was visualised with [DrawSQL](https://drawsql.app/):
![Data Model](wireframes/data_model.png)

#### Design Choices
##### Fonts
For this project, **Inter** is chosen and picked from [Google Fonts](https://fonts.google.com/). Inter is crafted and designed for computer screens. I think it is a modern and roboust and fits the site. 
As the fallback font in case Inter isn't being imported into the site correctly, **Roboto** is chosen.

##### Colours
![Colours](wireframes/hire_hens_colours.png)
- Black: #000000
- White: #FFFFFF
- Honey Yellow: #F9B236
Black and white are used to get a modern apperance and to get a good contrast. 
Honey Yellow is taken from a photo of a brown hen and this colour is used on the site to draw attention.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
### Responsive

### Features Left to Implement


## Technologies Used
### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) 
    - To structure the web content
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
    - To describe the web page's appearance/presentation
- [JavaScript](https://www.javascript.com/)
    - Bringing interactivity and logic to the site.
- [Python](https://www.python.org)
    - To manage logic and information on server side

### Frameworks, Libraries and other tools
- [Django](https://www.djangoproject.com/)
    - Used as the main framework, to increase productivity.
- [GitPod](https://gitpod.io/)
    - Used for version control by utilizing the GitPod terminal to
    commit to Git and push to GitHub and Heroku.
- [Heroku](https://www.heroku.com/home)
    - To host the web app
- [GitHub](https://github.com)
    - GitHub is used to store the code.
- [Balsamiq Wireframes](https://balsamiq.com/)
    - For designing the wireframes
- [DrawSQL](https://drawsql.app/)
    - To draw database diagrams
- [Google Fonts](https://fonts.google.com/)
    - Fonts are fetched from this site.
- [Favicon](https://favicon.io/)
    - to generate Favicon


DONE THIS FAR!
----------------------------------------------------------------------------

## Testing

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

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X