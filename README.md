# webServer
a web server page customizable.

to make a new page, copy the file named original.html here you will design the page, you can use the script tag to implant Js or css, then go to app.py and add the @app.route('/') decorator, you can put the name of the page after the / caracter if left to only / it will be the main page of your web app. underneath the decorator create a function for example:
example():
  add the code
  then add
  return render_template('fileNameForPage.html')
  
  to make a page only accesssible when logged in add the @login_required decorator after @app.route('/')
  
  
  made in python 3.7.2, using Flask and flask_login
