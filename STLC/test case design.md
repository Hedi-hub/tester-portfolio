# Market Mate - Test Case Design

## **1. Product Rating System**

**Test Design Techniques:** Equivalence Partitioning (EP), Error Guessing

- **Equivalence Partitioning:**
  - **Test Case:** Verify that only registered users who have purchased a product can submit a rating.
    - **Input:** Logged-in user who has not purchased a product attempts to rate.
    - **Expected Outcome:** The rating option is disabled, and a message is displayed:  
      _"Only customers who purchased this product can submit a review."_

  - **Test Case:** Verify rating submission with valid stars (1-5).
    - **Input:** A user who has purchased the product selects 5 stars and submits.
    - **Expected Outcome:** The full 5-star rating should be recorded successfully.

- **Error Guessing:**
  - **Test Case:** Verify review submission with restricted words.
    - **Input:** Enter profanity in the review text.
    - **Expected Outcome:** Warning message: _"Inappropriate words are not allowed."_

---

## **2. Age Verification for Alcoholic Products**

**Test Design Techniques:** Equivalence Partitioning (EP), Error Guessing

- **Equivalence Partitioning:**
  - **Test Case:** Verify system correctly denies access to alcoholic products if the user's account is underage.
    - **Input:** Log in with an account where the registered user is 17 years old.
    - **Expected Outcome:** Access denied with a message:  
      _"You must be 18+ to access this section."_

  - **Test Case:** Verify system grants access to alcoholic products if the user is 18+.
    - **Input:** Log in with an account where the registered user is 20 years old.
    - **Expected Outcome:** Access granted to alcoholic products.

- **Error Guessing:**
  - **Test Case:** Verify system behavior for users with no recorded birthdate.
    - **Input:** Log in with an account that does not have birthdate information.
    - **Expected Outcome:** System prompts the user to enter a birthdate before accessing alcoholic products.

---

## **3. Shipping Cost Changes**

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

- **Boundary Value Analysis:**
  - **Test Case:** Verify free shipping applies correctly based on the defined threshold.
    - **Input:** Test orders with different values: **€19.99, €20, and €45.70**.
    - **Expected Outcome:**
      - **€19.99:** Shipping cost is displayed.
      - **€20 or above:** Free shipping is clearly indicated.

  - **Test Case:** Verify shipping fee applies correctly for orders below the threshold.
    - **Input:** Order total is **€19.99**.
    - **Expected Outcome:** Shipping cost is displayed and charged appropriately.

- **Equivalence Partitioning:**
  - **Test Case:** Verify system recalculates shipping if an item is removed.
    - **Input:** Remove an item reducing total from **€55 to €45**.
    - **Expected Outcome:** Shipping cost recalculated correctly.

- **Use Case Testing:**
  - **Test Case:** Verify the correct display of shipping costs on the checkout page.
    - **Input:** Proceed to checkout with different order totals (**€19.99, €20, and €45.70**).
    - **Expected Outcome:**
      - Orders below **€20** should show a shipping fee.
      - Orders **€20 and above** should display _"Free Shipping"_ explicitly instead of omitting the cost.
