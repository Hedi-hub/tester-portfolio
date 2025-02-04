# The software

You will test a webshop, which can be found here:
https://grocerymate.masterschool.com/

The webshop has the following basic functionalities:

- Register and login functionality
- Searching for products, sorting on price, categories of products
- Add products to favorites
- Add products to basket
- Check-out process: billing and sending information in a form, choose payment
    method. Calculation of costs (calculate total price)

# New features

## 1. Product Rating System

**Vague Requirement** :

- Users should be able to rate products with a 5-star system and have the
    option to add written feedback.

**Questions** :

1. How will the system handle invalid ratings?(e.g. can user submit 0 or even 6
    stars?)
2. Can users submit a review without a star rating or vice versa?
3. Can users delete or edit their ratings?
4. Are there any restrictions on feedback text?(e.g. maximum character limit or
    inappropriate words)
5. What happens if a user submits the same review multiple times?(e.g. does it
    overwrite or duplicates or notifies user?)

**Detailed Requirement** :

- Users should rate products using a 1 to 5-star system, with no 0 or above 5
    ratings allowed. A star rating is required to submit a review, but written
    feedback is optional. Users can edit or delete their reviews. Reviews must be
    10 - 500 characters long and pass a profanity filter. Duplicate reviews should be
    detected and notified users if they would like to replace the previous review.


## 2. Age Verification for Alcoholic Products

**Vague Requirement** :

- Alcoholic products require age verification. A modal should appear when
    navigating to the alcoholic products category asking if the user is 18+. Users
    must input their age before accessing the alcoholic products.

**Questions** :

1. Does the system handle different date formats properly?(e.g. DD/MM/YYYY vs.
    MM/DD/YYYY)
2. What happens if a user enters an invalid age?(e.g. letters, negative numbers,
    or future birthdates)
3. Can a user skip the age check and see alchoholic products without
    verification?
4. Will the age information be saved in cookies or will users need to verify it
    every time?
5. Is the modal accessible on all devices(desktop, mobile, tablet)?

**Detailed Requirement** :

- Users must be able to input in a age place holder with the date format of DD/MM/YYYY. 
    Users cannot skip age verification to access alcoholic products. Users's date of 
    birth should be stored in cookies to avoid repetition. The modal must fully 
    responsive and accessible on desktop, mobile and tablet devices.

## 3. Shipping Cost Changes

**Vague Requirement** :

- Free shipping for orders above a certain amount. Orders below this amount
    will incur a shipping fee.

**Questions** :

1. How much do users need to spend to get free shipping?
2. Are there different shipping fees for different regions?
3. How does the system calculate shipping if the total amount changes?(e.g. if
    the user removes an item and the order falls below the free shipping fee)
4. How will users be informed about the shipping cost changes?(Is there a
    notification on the checkout page?)


**Detailed Requirement** :

- Users should get free shipping if the total amount of shopping card is over 50€. 
    Shipping fees should vary by region if applicable. If the
    order total changes (e.g., items removed), the shipping cost must update
    dynamically. Users must be notified of shipping cost changes on the checkout
    page.

