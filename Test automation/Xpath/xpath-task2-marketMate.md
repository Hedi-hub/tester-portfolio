> **XPath Solutions for Task 2 - MarketMate**\
> **1. XPath for the highlighted User Profile Icon**\
> Find the \<svg\> inside the div with class \'headerIcon\':\
> //div\[@class=\'headerIcon\'\]//svg\
> XPath for Selenium automation to click the profile icon:\
> driver.find_element(By.XPATH,
> \"//div\[@class=\'headerIcon\'\]//svg\").click()
>
> **2. XPath for Login/Sign-Up Page Elements**\
> **Login Page**\
> Email address field:\
> //input\[@type=\'email\'\]\
> Password field:\
> //input\[@type=\'password\'\]\
> Sign In button:\
> //button\[text()=\'Sign In\'\]
>
> **Create a new account link:**\
> //a\[text()=\'Create a new account\'\]
>
> **Go to Home link:**\
> //a\[text()=\'Go to Home\'\]
>
> **Sign-Up Page**\
> Full Name field:\
> //input\[@placeholder=\'Full Name\'\]\
> Email address field:\
> //input\[@placeholder=\'Email address\'\]
>
> Password field:\
> //input\[@placeholder=\'password\'\]\
> Sign Up button:\
> //button\[text()=\'Sign Up\'\]
>
> **3. XPath for Age Verification Modal**\
> XPath for the \'Confirm\' button:\
> //button\[text()=\'Confirm\'\]
>
> **4. XPath for Shop Page Elements (Oranges Product)**\
> XPath for the quantity input field for Oranges:\
> //div\[contains(text(),
> \'Oranges\')\]/following-sibling::div//input\[@type=\'number\'\]
>
> XPath for the \'Add to Cart\' button for Oranges:\
> //div\[contains(text(),
> \'Oranges\')\]/following-sibling::div//button\[text()=\'Add to
> Cart\'\]
>
> XPath for the \'Add to Wishlist\' button for Oranges:\
> //div\[@class=\'col-1\'\]//button\[contains(@class,
> \'btn-outline-dark\')\]