# Machine_learning_project
This is first Machine Learning Project

### Software and account requirement.

1.[Github Account](https://github.com)
2.[Heroku Account](https://dashboard.heroku.com/login)
3.[VS Code IDE] (https://code/visualstudio.com/download)
4.[Git Cli] (https://git-scm.com/downloads) 


creating conda environment
....
conda create -p venv python==3.7 -y
....

'''
conda activate venv/
'''
or
'''
conda activate venv
'''
'''
pip install -r requirements.txt

To add files to git
'''
git add .
'''

OR
'''
git add <file_name>
'''

Note :To ignore file or folder from git we can write name of file /folder in .gitignore file

To check the git status 
'''
git status
'''
To check all version maintained by git
'''
git log
'''
To create version/commit all changes by git
'''
git commit -m "message"
'''
To send version/changes to  github

'''
git push origin main

'''
To check remote url
'''
git remote -v
'''


'''
To setup CI/CD pipeline in heroku we need 3 information

1.HEROKU_EMAIL=rosy.prabu@gmail.com

2.HEROKU-API-KEY=9171dfbc-ce5c-42d5-a04c-a607b9238ca2

3.HEROKU_APP_NAME=ml-flask-app-git