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
