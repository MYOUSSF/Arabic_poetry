### 1. Compile the model

 Coompile and save model in the folder arabic-poetry-meter/model as "poetry_model.h5"

### 2. Create Docker container

```bash
docker build -t arabic-poetry-meter .

docker run -p 80:80 arabic-poetry-meter
```

### 3. Create Git repo

If you clone this repo this step is not needed. Or you can delete this git repo with `rm -rf .git` and start with a new one:

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
```

### 4. Create Heroku project

```bash
heroku login
heroku create arabic-poetry-meter
heroku git:remote arabic-poetry-meter
heroku stack:set container
git push heroku main
```
