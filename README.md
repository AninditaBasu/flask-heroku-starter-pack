# Flask for Heroku


Click to see :point_right: [![App on Heroku](https://img.shields.io/badge/App%20on-Heroku-brightgreen)](https://flask-heroku-starter-app.herokuapp.com/)  ................  Click to read :point_right: [![Post on dev.to](https://img.shields.io/badge/Post%20on-dev.to-blueviolet)](https://dev.to/aninditabasu/how-to-move-your-flask-app-from-the-local-machine-to-the-heroku-cloud-egk)

## _The unofficial :slightly_smiling_face: starter pack_

This repository has everything you need to get a _basic_ web app in Python to run on Heroku. Consequently, the repo has the barest minimum files needed to build a web app with Flask.


### How to use

1. Clone or fork this repository.
2. Get yourself a Heroku account if you don't already have one.
3. Create an app on Heroku by using the user interface of your Heroku account dashboard (Dashboard > New > Create new app). Follow the on-screen instructions to name your app, and connect it to your cloned or forked repository. 

   If this is the first time you are using your Heroku account to connect to anything on your GitHub account, you'll be asked to allow inter-site authentication.
   
   While creating the app, choose the manual option for deployment.
   
4. After the app is created, deploy it manually.

### Files in this repository

- templates/first_page.html *

  _Required._ This is the app home page that's displayed when the app is launched.
  
- templates/response_page.html *

  _Required._ This page is displayed after someone enters an input on the app home page.
  
- flaskStarter.py *

  _Required._ This is your Flask app.

- LICENSE

  _Optional._ The license under which I'm making available this repo. Not required for the app to work.

- Pipfile *

  _Required._ Tells Heroku which Python packages to install in the environment before building the app.

- Procfile *

  _Required._ Tells Heroku how to launch the app (which, in this case, is as a web page).

- README.md

  _Optional._ Not needed to make your app run. Is also the file you're reading right now.

- requirements.txt *

  _Required._ Tells Heroku the versions of the Python packages needed.
