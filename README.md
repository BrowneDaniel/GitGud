# GitGud - Github General User Data

<h2>SETUP/USAGE:</h2>

- Clone the repo

- Activate your virtual environment

- run: pip install -r requirements.txt

- run: python manage.py runserver

- go to http://127.0.0.1:8000/admin

- login to the administrator section of the django backend (username: admin - password: admin123)

- navigate to the "Users" section

- replace the existing user with the Github username and password of the account you'd like to see statistics for

- Save, and go to http://127.0.0.1:8000/

<h2>INFO:</h2>
This project uses Django and Python, including the PyGithub library, to gather and process the data from the logged in user.
The webpage on which the data is displayed is writted in HTML (obviously lol), and uses the Chart.js library to display the user's data.
The data is displayed in a bar chart and a pie chart.
The displayed data includes:
- Your number of followers
- The number of users you follow
- The number of repositories you have on your Github account
- The number of stars you have across all repositories on your Github account
- The number of unique languages you have used across all repositories on your Github account

These same statistics are gathered for your followers and their public repositories, and an average value is generated. These values are charted against your own.

The Pie Chart displays the frequency of each language that you use in the repositories on your account.

<h3>Bar Chart Sample</h3>

![Bar Chart Sample](https://raw.githubusercontent.com/BrowneDaniel/GitGud/master/bar.png)

<h3>Pie Chart Sample</h3>

![Pie Chart Sample](https://raw.githubusercontent.com/BrowneDaniel/GitGud/master/pie.png)

(note: some initial code I did for the first part of this project, the Github access is in a separate repo. [Here's the link.](https://github.com/BrowneDaniel/git_vis))
