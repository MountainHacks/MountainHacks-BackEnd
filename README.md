MountainHacks-BackEnd
=====================
The backend for the MountainHacks website, written in Python on the Django framework.

Installation (Unix-system assumed)
==================================
1) Make sure you have <a href="http://virtualenvwrapper.readthedocs.org/en/latest/#" target="_blank">VirtualEnvWrapper</a> and <a href="http://pip.readthedocs.org/en/latest/installing.html" target="_blank">pip</a> installed.<br/>
2) Clone down the project.<br/>
3) In your shell, 'cd' into the project folder and create a virtual environment for Python (see VirtualEnvWrapper docs).<br/>
4) Run 'pip install -r requirements.txt' to install all python dependencies.<br/>
5) Run 'python manage.py syncdb' to create your initial database.<br/>
6) Run 'python manage.py migrate api' to bring the database schema up to speed.<br/>
7) Now run 'python manage.py runserver' and open your browser to localhost:8000
