# Flask for Heroku

_The unofficial :slightly_smiling_face: starter pack_

This repository has everything you need to get a _basic_ web app in Python to run on Heroku. Consequently, the repo has the barest minimum files needed to build a web app with Flask.


## How to use

1. Clone or fork this repository.
1. Get yourself a Heroku account if you don't already have one.
1. Create an app on Heroku.
    1.  On your Heroku dashboard, click New > Create new app.
    1.  Follow the on-screen instructions to name your app, and connect it to your cloned or forked repository. If this is the first time you are using your Heroku account to connect to anything on your GitHub account, you're asked to allow inter-site authentication. 
    1.  Choose the manual option for deployment. 
1. After the app is created, deploy it manually.
1. After the app is deployed, test it. It should work. If it doesn't, review the files in the repository and try again.

## Files in this repository

<dl>

<dt>templates/first_page.html *</dt>
<dd><i>Required</i>. This is the app home page that's displayed when the app is launched.</dd>

<dt>templates/response_page.html *</dt>
<dd><i>Required</i>. This page is displayed after someone enters an input on the app home page.</dd>
  
<dt>flaskStarter.py *</dt>
<dd><i>Required</i>. This is your Flask app.</dd>

<dt>LICENSE</dt>
<dd><i>Optional</i>. The license under which I'm making this repo available. Not required for the app to work.</dd>

<dt>Pipfile *</dt>
<dd><i>Required</i>. Tells Heroku which Python packages to install in the environment before building the app.</dd>

<dt>Procfile *</dt>
<dd><i>Required</i>. Tells Heroku how to launch the app (which, in this case, is as a web page).</dd>

<dt>README.md</dt>
<dd><i>Optional</i>. Not needed to make your app run. Is also the file you're reading right now.</dd>

<dt>requirements.txt *</dt>
<dd><i>Required</i>. Tells Heroku the versions of the Python packages needed.</dd>

</dl>

## Why I made this template

Click to read :point_right: [![Post on dev.to](https://img.shields.io/badge/Post%20on-dev.to-blueviolet)](https://dev.to/aninditabasu/how-to-move-your-flask-app-from-the-local-machine-to-the-heroku-cloud-egk)
