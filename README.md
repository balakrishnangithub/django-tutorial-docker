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

## intro/tutorial02

- [ ] run initial migration of database for apps included in  `INSTALLED_APPS`

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py migrate
```

#### Models

- [ ] change your models


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/dfbfec7282f48082b65ae5be5db78769e8d9106a), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/dfbfec7282f48082b65ae5be5db78769e8d9106a)

- [ ] run python manage.py makemigrations to create migrations for those changes

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py makemigrations polls
```

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/f61d7b3158d459f7d599a706db042e9fead95eb5), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/f61d7b3158d459f7d599a706db042e9fead95eb5)

see what SQL that migration would run

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py sqlmigrate polls 0001
```

- [ ] run python manage.py migrate to apply those changes to the database

check for issues before running migration

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py check
```

run migration

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py migrate
```

#### Playing with the API

- [ ] invoke Python shell

```
$ docker run --rm -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python shell
```

- [ ] insert record

```
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
```

view

```
>>> q.id
1
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2016, 12, 16, 7, 46, 10, 150666, tzinfo=<UTC>)
```

- [ ] update record

```
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
<QuerySet [<Question: Question object>]>
```

