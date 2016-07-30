#!"e:\python.exe"

import os
uri = os.environ['REQUEST_URI']

import cgi
form = cgi.FieldStorage()

import random

image = ["0.png", "1.png", "2.png", "3.png", "4.png"]


def getimage():
    i = random.randint(0, 4)
    return image[i]

print("Content-Type: text/html\n")
print("<!Doctype html><html><body>")

if not form:
    print("<form action='" + uri + "' method='post'>")
    print("First Name: <input type='text' name='firstname'><br>")
    print("Last Name: <input type='text' name='lastname'><br>")
    print("Address: <input type='text' name='addr'><br>")
    print("Email: <input type='text' name='email'><br>")
    print("<input type='submit' value='Submit'>")
    print("</form>")
else:
    print("Thank you for submitting the following:<ul>")
    print("<li>", form["firstname"].value, "</li>")
    print("<li>", form["lastname"].value, "</li>")
    print("<li>", form["addr"].value, "</li>")
    print("<li>", form["email"].value, "</li>")
    print("</ul>")
    print("<p><img src='" + getimage() + "'></p>")
    print("</body></html>")

