## intro/tutorial01

build image

```
$ docker build -t $IMAGENAME .
```

```
$ docker run --rm $IMAGENAME python -m django --version
```

create a django project

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME django-admin startproject mysite .
```

[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/41255859f7116abc0afd5cdb2f014bd29bf5f264)

run development server

```
$ docker run --rm -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py runserver 0.0.0.0:8000
```

