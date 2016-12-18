## intro/tutorial01

- [ ] build docker image


```
$ docker build -t $IMAGENAME .
```

```
$ docker run --rm $IMAGENAME python -m django --version
```

- [ ] start project named *mysite*


```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME django-admin startproject mysite .
```

[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/5d8a6d8d0ea19e77093e20969fc0c5532363b292)

- [ ] try running development server


```
$ docker run --rm -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py runserver 0.0.0.0:8000
```

- [ ] start app named *polls*


```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py startapp polls
```

[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/a3390aa5e0c13951c251dd4033f03834de8c124d)

- [ ] create view for *polls*


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/dc67e8d62f2dccb86947758513570dbdd46591d8), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/dc67e8d62f2dccb86947758513570dbdd46591d8)

## intro/tutorial02

#### Models

- [ ] add *Question* and *Choice* model for *polls*


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/dfbfec7282f48082b65ae5be5db78769e8d9106a), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/dfbfec7282f48082b65ae5be5db78769e8d9106a)

- [ ] generate migration script

```shl
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py makemigrations polls
```

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/f61d7b3158d459f7d599a706db042e9fead95eb5), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/f61d7b3158d459f7d599a706db042e9fead95eb5)

- [ ] apply migration to database

check for issues

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py check
```

view SQL of the migration script

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py sqlmigrate polls 0001
```

apply

```
$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py migrate
```

#### Playing with the API

- [ ] invoke Python shell

```
$ docker run --rm -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python shell
```

- [ ] try inserting record

```
>>> from polls.models import Question, Choice
>>> Question.objects.all()
<QuerySet []>
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
```

- [ ] try updating inserted record

```
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
<QuerySet [<Question: Question object>]>
```

- [ ] add `__str__()` method to *Question* and *Choice* model

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/3fbc40a184bc59b75e7c434bae25ad7b69199954), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/3fbc40a184bc59b75e7c434bae25ad7b69199954)

```
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
```

- [ ] add `was_published_recently()` to *Question* model


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/b73aef6495c53957de112f799c640af31f6b11d6), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/b73aef6495c53957de112f799c640af31f6b11d6)

```
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True
```

- [ ] try *get*, *filter*

*get*

```
>>> Question.objects.get(id=1)
<Question: What's up?>
>>> Question.objects.get(pk=1)
<Question: What's up?>
```

*filter*

```
>>> Question(question_text="Who're you?", pub_date= timezone.now()).save()
```

```
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>

>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.filter(pub_date__year=current_year)
<QuerySet [<Question: What's up?>, <Question: Who're you?>]>
```

- [ ] try insert using relation i.e. create *Choice* for *Question*

```
>>> q = Question.objects.get(pk=1)

>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> q.choice_set.create(choice_text='Just hacking again', votes=0)
<Choice: Just hacking again>
>>> q.choice_set.create(choice_text='Just hacking again and again', votes=0)
<Choice: Just hacking again and again>

>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>, <Choice: Just hacking again and again>]>
>>> q.choice_set.count()
4
```

- [ ] try relational *get*, *filter* and *delete*

```
>>> c = q.choice_set.get(choice_text='Just hacking again')
>>> c.question
<Question: What's new?>

>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c
<QuerySet [<Choice: Just hacking again>, <Choice: Just hacking again and again>]>

>>> c.delete()
(2, {'polls.Choice': 2})
```

