# **Market Mate - Test Execution Report**


## **Scenario 1: Product Rating Submission**

**As a registered user of GroceryMate, I should be able to submit a rating only for products I have purchased.**

| Step # | Action | Expected Outcome | OK/NOK | URL | Link to Issue |
|--------|--------|-----------------|--------|-----|--------------|
| 1 | Log in with valid credentials. | User is successfully logged in. | OK | /login | |
| 2 | Purchase the product (e.g., Celery). | Purchase is completed successfully. | OK | /checkout | |
| 3 | Return to the same product page. | Rating option is enabled. | OK | /product/celery | |
| 4 | Submit a rating (e.g., 5 stars). | The rating system allows full selection of 5 stars. | NOK | /product/celery | [Issue #1](https://github.com/Hedi-hub/tester-portfolio/issues/1) |

---

## **Scenario 2: Age Verification for Alcoholic Products**

**As a user of GroceryMate, access to alcoholic products should be restricted based on age verification.**

| Step # | Action | Expected Outcome | OK/NOK | URL | Link to Issue                                                      |
|--------|--------|------------------|--------|-----|--------------------------------------------------------------------|
| 1 | Log in with an account registered as 17 years old. | User is successfully logged in. | OK | `/login` |                                                                    |
| 2 | Attempt to access an alcoholic product page. | Access is denied with a message: _"You must be 18+ to access this section."_ | NOK | `/product/wine` | [Issue #2](https://github.com/Hedi-hub/tester-portfolio/issues/2)  |
| 3 | Log in with an account registered as 20 years old. | User is successfully logged in. | OK | `/login` |                                                                    |
| 4 | Access the same alcoholic product page. | Access is granted to the alcoholic product. | OK | `/product/wine` |                                                                    |
| 5 | Log in with an account that has no birthdate recorded. | User is successfully logged in. | OK | `/login` |                                                                    |
| 6 | Attempt to access an alcoholic product page. | System prompts the user to enter their birthdate before accessing alcoholic products. | NOK | `/product/wine` | [Issue #3](https://github.com/Hedi-hub/tester-portfolio/issues/3)  |

---

## **Scenario 3: Shipping Cost Calculation**

**As a user of GroceryMate, the shipping cost should be calculated based on the order total, with free shipping applied correctly according to the defined threshold.**

| Step # | Action | Expected Outcome | OK/NOK | URL | Link to Issue |
|--------|--------|------------------|--------|-----|--------------|
| 1 | Add items totaling €19.99 to the cart. | Shipping fee is applied. | OK | `/cart` | |
| 2 | Increase the order total to €20.00. | Free shipping is applied. | OK | `/cart` | |
| 3 | Proceed to checkout with an order total of €19.99. | Shipping fee is displayed correctly before payment. | OK | `/checkout` | |
| 4 | Proceed to checkout with an order total of €20.00. | _"Free Shipping"_ is explicitly displayed before payment. | OK | `/checkout` | |
| 5 | Remove an item reducing the total from €55 to €45. | Shipping cost is recalculated correctly based on the new total. | OK | `/cart` | |

---