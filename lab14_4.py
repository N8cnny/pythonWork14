#!"e:/python.exe"

import os
uri = os.environ['REQUEST_URI']

import cgi
form = cgi.FieldStorage()

print("Content-Type: text/html\n\n")
print("<!Doctype html><html><body>")

if not form:
    print("<form action='" + uri + "' method='post'>")
    print("Enter the number of rows: <input type='text' name='rows'><br>")
    print("Select two colors:")
    print("<input type='checkbox' name='ckb1' value='red'>Red")
    print("<input type='checkbox' name='ckb2' value='yellow'>Yellow")
    print("<input type='checkbox' name='ckb3' value='green'>Green")
    print("<input type='checkbox' name='ckb4' value='blue'>Blue")
    print("<input type='checkbox' name='ckb5' value='pink'>Pink")
    print("<input type='submit' value='Submit'>")
    print("</form>")
else:
    rows = form.getvalue("rows","(no entry)")

    rows = cgi.escape(rows)

    bgclr = []

    if "ckb1" in form:
        bgclr.append(form["ckb1"].value)

    if "ckb2" in form:
        bgclr.append(form["ckb2"].value)

    if "ckb3" in form:
        bgclr.append(form["ckb3"].value)

    if "ckb4" in form:
        bgclr.append(form["ckb4"].value)

    if "ckb5" in form:
        bgclr.append(form["ckb5"].value)

    print("<table width=100% border=0>")

    i = 1

    while i <= int(rows):
        if i % 2 == 0:
            print("<tr><td bgcolor='" + bgclr[0] + "'>row", i ,"</td></tr>")

        else:
            print("<tr><td bgcolor='" + bgclr[1] + "'>row", i ,"</td></tr>")

        i = i + 1

    print("</table>")
print("</body></html>")