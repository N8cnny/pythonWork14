#!"e:/python.exe"

import os
uri = os.environ['REQUEST_URI']

import cgi
form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")
print("<!Doctype html><html><body>")
print("<form action='" + uri + "' method='post'>")
print("Enter your birth year: <input type='text' name='year'>")
print("<input type='submit' value='Submit'>")
print("</form>")

if form:
    year = form.getvalue("year","(no year)")
    year = cgi.escape(year)

    y = int(year) % 12

    print("<hr size='1' width='350' align='left'>")

    if y == 4: zodiac = "rat"; image1 = "rat.png"
    elif y == 5: zodiac = "ox"; image1 = "ox.png"
    elif y == 6: zodiac = "tiger"; image1 = "tiger.png"
    elif y == 7: zodiac = "rabbit"; image1 = "rabbit.png"
    elif y == 8: zodiac = "dragon"; image1 = "dragon.png"
    elif y == 9: zodiac = "snake"; image1 = "snake.png"
    elif y == 10: zodiac = "horse"; image1 = "horse.png"
    elif y == 11: zodiac = "goat"; image1 = "goat.png"
    elif y == 0: zodiac = "monkey"; image1 = "monkey.png"
    elif y == 1: zodiac = "rooster"; image1 = "rooster.png"
    elif y == 2: zodiac = "dog"; image1 = "dog.png"
    else: zodiac = "pig"; image1 = "pig.png"

    print("You were born in<b>", year, "</b>. ")
    print("It was the", zodiac,"year.")
    print("<p><img src='" + image1 + "'></p>")
print("</body></html>")