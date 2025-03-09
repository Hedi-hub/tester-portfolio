> **XPath Solutions:**
>
> 1\. XPath to locate the main \<h1\> element\
> //h1\[@id=\'mainTitle\'\]
>
> 2\. XPath to select the \"About Us\" navigational link
> //a\[text()=\'About Us\'\]
>
> 3\. XPath to select the \"Graphic Design\" dropdown link
> //a\[@href=\'#graphicdesign\'\]
>
> 4\. XPath to select the team members name \"Jane Smith\"
> //h4\[text()=\'Jane Smith\'\]
>
> 5\. XPath to select the description of \"SEO Services\"
> //h3\[text()=\'SEO Services\'\]/following-sibling::p
>
> 6\. XPath to select all service items in the \"Our Services\" section
> //div\[@class=\'service-item\'\]
>
> 7\. XPath to select the email input field in the contact form
> //input\[@type=\'email\'\]
>
> 8\. XPath to select the entire contact form
>
> //form\[@id=\'contactForm\'\]
>
> 9\. XPath to select the footer paragraph element
>
> //footer/p
>
> 10\. XPath to select the first team member\'s \<h4\> name
>
> (//h4)\[1\]
>
> 11\. XPath to select the description of the second service item
>
> (//div\[@class=\'service-item\'\]/p)\[2\]
>
> 12\. XPath to select the \"Contact Us\" section header
>
> //h2\[text()=\'Contact Us\'\]
>
> 13\. XPath to select all links within the dropdown under the
> \"Services\" navigation item
>
> //ul\[@class=\'dropdown\'\]//a
>
> 14\. XPath to select the first \<li\> under the \"Our Team\" section
>
> (//div\[@class=\'team\'\]//li)\[1\]
>
> 15\. XPath to locate the \"Send Message\" button in the contact form
>
> //input\[@type=\'submit\' and \@value=\'Send Message\'\]
