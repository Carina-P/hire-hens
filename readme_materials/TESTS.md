# Test plan
Back to [README]()
## Contents

The below plan for testing was followed during development of the site: The TDD, TestDriven Development, process is followed as much as possible. Test cases are developed/thought of, before the code is implemented. The test process is conducted in an iterative manner and implementation cycles are short with small parts of code constructed every time. In some cases, prototyping is used and the thorough test is done when I was satisfied with the prototype.

Before new code is committed, testing of all code developed earlier are repeated again.

When all features are implemented and tested, the following tests are performed:
* Go throught the test cases for functional testing and testing of responsiveness, as described below.
* HTML-code validated by [W3S Markup validation service](https://validator.w3.org/)
* CSS-cod validated by [W3S CSS validation service](https://jigsaw.w3.org/css-validator/)
* JavaScript-code validated by [JSHint](https://jshint.com/)
* Python code is validated by [PEP8](http://pep8online.com/)
* The site is tested on different browsers, as described below
* The deployed version in heroku is tested

## Test of functionality and responsiveness
Functionality tests and tests of responsiveness are done by following test cases below. Test of responsiveness is mainly performed with the help of Chrome Developers Tool.

### Test cases
Test cases are described below and linked to use cases. Each test case have a name beginning with TC and then a number, e.g. TC_001.

* Testing use case US_001. As a user I want to be able to register to the site. By doing this I have the possibility to add my personal information and thus paying process will be faster.:
    **TC_001** Register to the site:
    * How to test:
        * In the navbar choose My Account and then Register.
        * Fill out email, user name and password.
        * Also test to fill in email without an @.
        * Also test to give to different passwords.
    * Expected outcome:
        * A message that a mail is sent with link for verification. When you get the mail and follow the verification your should get the possibility to login.
        * If you give email without @ or two different passwords you will be informed that they are wrong and not have possibility to register.

* Testing use case US_002. As a user, I want to be able to login to the site:
    **TC_002** Log in to the site:
    * How to test:
        * In navbar choose My Account and Log in.
        * Fill in user name and password.
        * Also test to give wrong user name.
        * Also test to give wrong password.
    * Expected outcome:
        * You are logged in to site and guided to homepage.
        * If you gie wrong user name or password you get an error message and are not logged in.
* Testing use case US_003. As a user, I want to be able to log out.
    **TC_003** Log out:
    * How to test:
        * Go to navbar, choose My Account and Log out.
    * Expected outcome: 
        * You are guided to log out-page and are asked if you are sure.
        * If you click yes you get a message that you are logged out and are guided to home page.
* Testing use case US_004. As a user, I want to be able to look at the site anonymously, without logging in.
    **TC_004** Go through all the steps to add an order to the system without logging in.
    * How to test:
        * Be sure you are not logged in.
        * In navbar choose Hire.
        * Add 10 brahma hens for 4 months to the cart.
        * Add a coop for 10 hens for 4 months to the cart.
        * Go to buy consumables and add bedding to cart.
        * Go to cart.
        * Choose checkout.
        * Fill in form and checkout.
    * Expected outcome:
        * You should be able to go through all the steps and add an order without problem.
* Testing use case US_005. As a user, I want to build my own rental package, consisting of hens of my choice and having the possibility to add coop and/or feeder and waterer.
    **TC_005** Add hens, coop and waterer, with same amount of months for rental, in cart.
    * How to test:
        * Choose Hire in navbar.
        * Choose Lohman hens.
        * Add 10 hens for 5 months to cart.
        * Choose coop for 10 hens.
        * Do not change months and add 1 coop.
        * Choose waterer
        * Do not change months and add 2 waterers to cart.
        * Go to cart.
    * Expected outcome:
        * In cart you should find 10 Lohman hens, 1 coop for 10 hens and 2 waterers in the cart. And all should have 5 months as rental lenght.
        * Carefully check all the prices, subtotals and grand total.
* Testing use case US_006. As a user, I want to add products that I want to buy to the cart.
  **TC_006** Add hens, coop, waterer, feeder, food and bedding to buy in shopping cart.
    * How to test:
        * In navbar choose buy and Hens
        * Choose Brahma hen
        * Add 4 hens to cart
        * In navbar choose buy and coop
        * Choose coop for 2 hens
        * Add 2 coops to cart
        * In navbar choose buy and equipment
        * Choose feederS
        * Add 2 feeders to cart
        * Choose waterer
        * Add 1 waterer to cart
        * In navbar choose buy and consumables
        * Choose food
        * Add 5 to cart
        * Choose bedding
        * Add 1 to cart
        * Go to cart
    * Expected outcome:
        * In the cart you should see 4 Brahma hens, 2 coops for 2 hens, 2 feeders, 1 waterer, 5 pieces of food and 1 bedding.
        * Carefully check all the prices, subtotals and grand total

* Testing use case US_007. As a user, I want to look at my cart and then continue shopping.
    **TC_007** Add items to cart, go to the cart and look and then continue adding items to the cart.
    * How to test:
        * Fill a cart as in TC_005.
        * Go to cart.
        * In navbar choose hire
        * Choose Lohman hen
        * Add 2 Lohman hens for 5 months to cart.
        * Choose coop for 10 hens
        * Add 1 coop for 2 months to cart
        * Choose Buy and Consumables in navbar
        * Choose food
        * Add 2 pieces to cart
        * Go to cart
    * Expected outcome:
        * Check carefully that you have:
            * rent: 12 Lohman hens for 5 months
            * rent: 1 coop for 10 hens for 5 months
            * rent: 1 coop for 10 hens for 2 months
            * rent: 2 waterers for 5 months
            * buy: 2 pieces of food
        * Also check prices, subtotals and Grand total.

* Testing use case US_008. As a user, I want to change quantity or remove items in cart.
    **TC_008** Add items to cart according to TC_007 and do adjustments to the cart
    * How to test:
        * Follow the steps in how to test TC_007.
        * In cart add 1 more piece of food and click update.
        * Remove the 12 Lohman hens by clicking Remove and answer yes to question if you want to remove.
    * What to expect:
        * You shoud now have 3 pieces of food in your cart
        * And you should not have any hens.
        * Carefully check subtotals and grand totals.

* Testing use case US_009. As a user, I want to checkout my cart.
    **TC_009** Checkout cart from TC_007
        * How to test:
            * Log in to the site.
            * Complete the steps in how to test from TC_007
            * Go to checkout page and fill out the form.
            * Save the delivery information in the form.
        * What to expect:
            * You should have a filled out form in checkout page 
            * You should also have an order summary that consists of:
                * rent: 12 Lohman hens for 5 months
                * rent: 1 coop for 10 hens for 5 months
                * rent: 1 coop for 10 hens for 2 months
                * rent: 2 waterers for 5 months
                * buy: 2 pieces of food
            * Please carefully check subtotals and grand totals.
    **TC_010** Give wrong credit card number.
        * How to test
            * Complete all steps according to TC_009
            * Fill out form in checkout page but give wrong credit card number.
        * Expected outcome:
            * You should get an error message telling you that credit card number is wrong. And you cannot choose complete order.

*Testing use case US_010. As a user, I want to return from the checkout page to my cart and do some adjustments.
    **TC_011** 
        * How to test:
            * Log in to the site, with same credentials as in TC_009.
            * Complete the steps in how to test from TC_007
            * Go to checkout page.
            * Information in form should be given - same as you filled out in TC_009.
            * Choose adjust cart.
            * Remove 1 coop for 10 hens for 2 months.
            * Return to checkout page.
        * What to expect:
            * You should not have to fill in checkout form.
            * In your order summary you should have:
                * rent: 12 Lohman hens for 5 months
                * rent: 1 coop for 10 hens for 5 months
                * rent: 2 waterers for 5 months
                * buy: 2 pieces of food
            * Check subtotals and grand totals!
    
* Testing use case UC_011 As a user, I want to pay, for the contents in my cart, in a secure way, with a credit card.
    **TC_0012** Complete order for TC_011
    * How to test:
        * Follow step in TC_011
        * Choose Complete order
    * Expected outcome: 
        * A page with a spinner is shown for a while.
        * Then you are guided to checkout success page with order details and grand total.
        * Check that the order details are correct.
        * Log in to account at **Stripe** and check under Developer that transaction succeeded and information is correct by looking under weebhooks, events and logs.
        * Go to admin and check the Order table in the **database** and check that everything is OK.

* Testing use case US_012. As a user that is logged in I want to be able to save my delivery and contact information to be shown in checkout form every time I checkout.
    **TC_0013** This test is part of TC_011
    * How to test:
        * This is actually tested in TC_011
    * Expected outcome: 
        * As stated in TC_011 you should not have to fill in delivery and contact information again.
 
* Testing use case US_013. As a user i want confirmation when my order is processed and added to the system.
    * How to test:
    * Expected outcome: 
* Testing use case US_003.
    * How to test:
    * Expected outcome: 
* Testing use case US_003.
    * How to test:
    * Expected outcome:  
* Testing use case US_003.
    * How to test:
    * Expected outcome:  
* Testing use case US_003.
    * How to test:
    * Expected outcome:  
* Testing use case US_003.
    * How to test:
    * Expected outcome:  
* Testing use case US_003.
    * How to test:
    * Expected outcome: 
* Testing use case US_003.
    * How to test:
    * Expected outcome:  
* Testing use case US_003.
    * How to test:
    * Expected outcome: 
* Testing use case US_003.
    * How to test:
    * Expected outcome: 


### Other tests
- The navbar functionality was test by clicking on all possibilities.
- Webhooks was tested by removing form.save() to simulate that connection was lost before form is saved.
- After each order transaction I checked in Stripe under Developers tab to see that everything looks alright.
