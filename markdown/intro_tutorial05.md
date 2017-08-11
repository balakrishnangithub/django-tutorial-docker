## intro/tutorial05

- [ ] define and run a test for *polls* app
```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py test polls
Creating test database for alias 'default'...
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionMethodTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/app/mysite/polls/tests.py", line 17, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

 [code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/2803405bb0b70c81217a533743f5777082ab68ac),
 [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/2803405bb0b70c81217a533743f5777082ab68ac)

- [ ] fix the bug and run the same test for *polls* app
```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py test polls
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
Destroying test database for alias 'default'...
```

 [code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/4d9392da901ee688434a671dd2dae09243bc34b6),
 [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/4d9392da901ee688434a671dd2dae09243bc34b6)

- [ ] add multiple tests
```
$ docker run --rm -u $UID -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py test polls
Creating test database for alias 'default'...
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
Destroying test database for alias 'default'...
```

 [code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/adc781bcd491abe487bb71601f3796a6f43fead5),
 [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/adc781bcd491abe487bb71601f3796a6f43fead5)

- [ ] experiment with Django test client
```
$ docker run --rm -u $UID -it -v $LOCALPATH:/app/mysite $IMAGENAME python manage.py shell

>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()

>>> # get a response from '/'
>>> response = client.get('/')
>>> # we should expect a 404 from that address
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#39;s up?</a></li>\n    \n    </ul>\n\n'
>>> # If the following doesn't work, you probably omitted the call to
>>> # setup_test_environment() described above
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>
```

 - [ ] fix listing or displaying future questions

 [code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/999a31ad077a28198039648f5039dd45bcb8bea2),
 [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/999a31ad077a28198039648f5039dd45bcb8bea2)

- [ ] add tests to ensure listing or displaying published questions only

 [code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/6488094927243b1d6e10a9897856f830c29711d0),
 [repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/6488094927243b1d6e10a9897856f830c29711d0)
