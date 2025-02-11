# Test Case Design

## 1. Product Rating System

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Error Guessing

### Test Cases:

- **Boundary Value Analysis:**
  - **Test Case:** Verify rating submission with valid stars (1-5).
    - **Input:** Select 5 stars and submit.
    - **Expected Outcome:** Rating is recorded successfully.

- **Equivalence Partitioning:**
  - **Test Case:** Verify rating submission without stars.
    - **Input:** Submit feedback without selecting a star rating.
    - **Expected Outcome:** Error message "Please select a star rating."

- **Error Guessing:**
  - **Test Case:** Verify review submission with restricted words.
    - **Input:** Enter profanity in review text.
    - **Expected Outcome:** Warning message "Inappropriate words are not allowed."

## 2. Age Verification for Alcoholic Products

**Test Design Techniques:** Equivalence Partitioning (EP), Error Guessing

### Test Cases:

- **Equivalence Partitioning:**
  - **Test Case:** Verify access restriction for underage users.
    - **Input:** Enter birthdate indicating user is 17 years old.
    - **Expected Outcome:** Access denied with a message "You must be 18+ to access this section."

  - **Test Case:** Verify access granted for users 18+.
    - **Input:** Enter birthdate indicating user is 20 years old.
    - **Expected Outcome:** Access granted to alcoholic products.

- **Error Guessing:**
  - **Test Case:** Verify system behavior when birthdate field is left empty.
    - **Input:** Leave birthdate blank.
    - **Expected Outcome:** Error message "Birthdate is required."

## 3. Shipping Cost Changes

**Test Design Techniques:** Boundary Value Analysis (BVA), Equivalence Partitioning (EP), Use Case Testing

### Test Cases:

- **Boundary Value Analysis:**
  - **Test Case:** Verify free shipping applies above the limit.
    - **Input:** Order total is €51 (assuming free shipping starts at €50).
    - **Expected Outcome:** Shipping cost = €0.

  - **Test Case:** Verify shipping fee applies below the limit.
    - **Input:** Order total is €49.
    - **Expected Outcome:** Shipping cost = applicable fee (The system should charge the correct shipping fee based on the order amount).

- **Equivalence Partitioning:**
  - **Test Case:** Verify system recalculates shipping if an item is removed.
    - **Input:** Remove an item reducing total from €55 to €45.
    - **Expected Outcome:** Shipping cost recalculated correctly.

- **Use Case Testing:**
  - **Test Case:** Verify shipping cost is displayed on checkout page.
    - **Input:** Proceed to checkout with an order total of €40.
    - **Expected Outcome:** Shipping fee is clearly displayed before payment.