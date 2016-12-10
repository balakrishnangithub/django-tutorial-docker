## intro/tutorial01

- [ ] build image


```
$ docker build -t $IMAGENAME .
```

```
$ docker run --rm $IMAGENAME python -m django --version
```

- [ ] start a project named *mysite*


```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME django-admin startproject mysite .
```

[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/5d8a6d8d0ea19e77093e20969fc0c5532363b292)

- [ ] run development server


```
$ docker run --rm -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py runserver 0.0.0.0:8000
```

- [ ] start an app named *polls*


```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py startapp polls
```

[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/a3390aa5e0c13951c251dd4033f03834de8c124d)

- [ ] create a *view* for *polls*


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/dc67e8d62f2dccb86947758513570dbdd46591d8), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/dc67e8d62f2dccb86947758513570dbdd46591d8)

## intro/tutorial02/

- [ ] run initial migration of database for apps included in  `INSTALLED_APPS`

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py migrate
```

