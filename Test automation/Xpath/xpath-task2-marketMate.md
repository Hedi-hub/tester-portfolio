# XPath Solutions for Task 2 - MarketMate

## 1. XPath for the highlighted User Profile Icon
```xpath
//div[@class='headerIcon']
```

## 2. XPath for Login/Sign-Up Page Elements

### Login Page
Email address field:
```xpath
//input[@type='email']
```
Password field:
```xpath
//input[@type='password']
```
Sign In button:
```xpath
//button[text()='Sign In']
```
Create a new account link:
```xpath
//a[text()='Create a new account']
```
Go to Home link:
```xpath
//a[text()='Go to Home']
```

### Sign-Up Page
Full Name field:
```xpath
//input[@placeholder='Full Name']
```
Email address field:
```xpath
//input[@placeholder='Email address']
```
Password field:
```xpath
//input[@placeholder='password']
```
Sign Up button:
```xpath
//button[text()='Sign Up']
```

## 3. XPath for Age Verification Modal
XPath for the `Confirm` button:
```xpath
//button[text()='Confirm']
```

## 4. XPath for Shop Page Elements (Oranges Product)
XPath for the quantity input field for Oranges:
```xpath
//p[contains(text(), 'Oranges')]/following::input[@type='number'][1]
```
XPath for the `Add to Cart` button for Oranges:
```xpath
//p[contains(text(), 'Oranges')]/following-sibling::button[text()='Add to Cart'][1]
```
XPath for the `Add to Wishlist` button for Oranges:
```xpath
//p[contains(text(), 'Oranges')]/following::button[contains(@class, 'btn-outline-dark')][1]
```
