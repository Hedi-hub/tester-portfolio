# Test Case Design

## 1. Product Rating System

Test Design Techniques: Boundary Value Analysis (BVA), Equivalence Partitioning (EP),
Error Guessing

## Test Cases:

1. Boundary Value Analysis:
    o Test Case: Verify rating submission with valid stars (1-5).
    o Input: Select 5 stars and submit.
    o Expected Outcome: Rating is recorded successfully.
2. Equivalence Partitioning:
    o Test Case: Verify rating submission without stars.
    o Input: Submit feedback without selecting a star rating.
    o Expected Outcome: Error message "Please select a star rating."
3. Error Guessing:
    o Test Case: Verify review submission with restricted words.
    o Input: Enter profanity in review text.
    o Expected Outcome: Warning message "Inappropriate words are not allowed."

## 2. Age Verification for Alcoholic Products

Test Design Techniques: Equivalence Partitioning (EP), Error Guessing

## Test Cases:

1. Equivalence Partitioning:
    o Test Case: Verify access restriction for underage users.
    o Input: Enter birthdate indicating user is 17 years old.
    o Expected Outcome: Access denied with a message "You must be 18+ to
       access this section."
2. Equivalence Partitioning:
    o Test Case: Verify access granted for users 18+.
    o Input: Enter birthdate indicating user is 20 years old.
    o Expected Outcome: Access granted to alcoholic products.
3. Error Guessing:
    o Test Case: Verify system behavior when birthdate field is left empty.
    o Input: Leave birthdate blank.
    o Expected Outcome: Error message "Birthdate is required."

## 3. Shipping Cost Changes

Test Design Techniques: Boundary Value Analysis (BVA), Equivalence Partitioning (EP),
Use Case Testing


## Test Cases:

1. Boundary Value Analysis:
    o Test Case: Verify free shipping applies above the limit.
    o Input: Order total is €51 (assuming free shipping starts at €50).
    o Expected Outcome: Shipping cost = €0.
2. Boundary Value Analysis:
    o Test Case: Verify shipping fee applies below the limit.
    o Input: Order total is €49.
    o Expected Outcome: Shipping cost = applicable fee (The system should
       charge the correct shipping fee based on the order amount.).
3. Equivalence Partitioning:
    o Test Case: Verify system recalculates shipping if an item is removed.
    o Input: Remove an item reducing total from €55 to €45.
    o Expected Outcome: Shipping cost recalculated correctly.
4. Use Case Testing:
    o Test Case: Verify shipping cost is displayed on checkout page.
    o Input: Proceed to checkout with an order total of €40.
    o Expected Outcome: Shipping fee is clearly displayed before payment.
