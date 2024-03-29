# Machine_learning_project
This is first Machine Learning Project

### Software and account requirement.

1.[Github Account](https://github.com)
2.[Heroku Account](https://dashboard.heroku.com/login)
3.[VS Code IDE](https://code/visualstudio.com/download)
4.[Git Cli](https://git-scm.com/downloads) 
5.[Git Documentation](https://git-scm.com/docs/gittutorial)


creating conda environment
```

conda create -p venv python==3.7 -y

```

```
conda activate venv/
```
or
```
conda activate venv
```
```
pip install -r requirements.txt
```

To add files to git
```
git add .
```

OR
```
git add <file_name>
```

Note :To ignore file or folder from git we can write name of file /folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```
To create version/commit all changes by git
```
git commit -m "message"
```
To send version/changes to  github

```
git push origin main
```

To check remote url
```
git remote -v
```
To setup CI/CD  pipeline in heroku we need 3 information


1.HEROKU_EMAIL=rosy.prabu@gmail.com
2.HEROKU_API_KEY=<>
3.HEROKU_APP_NAME=ml-flask-app-git

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .

```

Note:Image name for docker must be lowercase

To list docker image
```
docker images
```
Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 

```
To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

```
python setup.py install
```
Install ipykernel

```
pip install ipykernel

```
