#!"e:/python.exe"

import os
uri = os.environ['REQUEST_URI']

import cgi
form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")
print("<!Doctype html><html><body>")
print("<form action='" + uri + "' method='post'>")
print("Enter hourly rate: <input type='text' name='hpay'><br>")
print("Enter the number of hours: <input type='text' name='totalh'> <br>")
print("Select the tax rate:<select name='tax'>")
print("<option value='0.25' selected>25%</option>")
print("<option value='0.27'>27%</option>")
print("<option value='0.29'>29%</option>")
print("</select>")
print("<input type='submit' value='Submit'>")
print("</form>")

if form:
    hpay = form.getvalue("hpay")
    totalh = form.getvalue("totalh")
    tax = form["tax"].value
    hpay = cgi.escape(hpay)
    totalh = cgi.escape(totalh)
    tax = cgi.escape(tax)
    gross = round(float(hpay) * float(totalh), 2)
    net = round(float(hpay) * float(totalh) * (1- float(tax)), 2)
    taxAmount = round(float(hpay) * float(totalh) * float(tax), 2)
    print("<hr size='1' width='100%'>")
    print("Your weekly income report<br>")
    print("Gross Income: $", gross, "<br>")
    print("Tax: $", taxAmount, "<br>")
    print("Net Income: $", net, "<br>")
print("</body></html>")