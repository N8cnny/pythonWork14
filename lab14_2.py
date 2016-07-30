#!"e:/python.exe"

import random
from random import shuffle

import os
uri = os.environ['REQUEST_URI']

import cgi
form = cgi.FieldStorage()


def shownumbers(n):
    z = []
    for i in range(1, 48):
        z.insert(i, i)

    j = 0
    while j < n:
        s = ""
        shuffle(z)
        for i in range(0, 5):
            s = s + str(z[i]) + " "

        s = s + "mega: " + str(random.randint(0, 27)) + "<br>"
        print(s)
        j = j + 1

print("Content-Type: text/html\n\n")
print("<!Doctype html><html><body>")
print("<form action='" + uri + "' method='post'>")
print("How many drawing(s)? <input type='text' name='drawing'>")
print("<input type='submit' value='Submit'>")
print("</form>")
if form:
    drawing = form.getvalue("drawing","(no drawing)")

    drawing = cgi.escape(drawing)

    n = int(drawing)

    shownumbers(n)

print("</body></html>")