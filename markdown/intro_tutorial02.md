## intro/tutorial02

#### Models

- [ ] add *Question* and *Choice* model for *polls*


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/e4831eecd188bbee0f5a175282ea3367f4ddc55b), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/e4831eecd188bbee0f5a175282ea3367f4ddc55b)

- [ ] generate migration script

```shl
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py makemigrations polls
```

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/cc503a9dbe6569d6d90aad36561ae0f61eeb470b), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/cc503a9dbe6569d6d90aad36561ae0f61eeb470b)

- [ ] apply migration to database

check for issues

```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py check
```

view SQL of the migration script

```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py sqlmigrate polls 0001
```

apply

```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py migrate
```

#### Playing with the API

- [ ] invoke Python shell

```
$ docker run --rm -u $UID -it -p 8000:8000 -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py shell
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

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/4076cf65bc6bd7e5d5bec1a69586222c9967a9b3), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/4076cf65bc6bd7e5d5bec1a69586222c9967a9b3)

```
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
```

- [ ] add `was_published_recently()` to *Question* model


[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/377abdbd830a967952fc9875ab0e3adfe6b4673c), [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/377abdbd830a967952fc9875ab0e3adfe6b4673c)

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
