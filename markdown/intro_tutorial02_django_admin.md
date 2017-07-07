## Django Admin

- [ ] enable *Django Admin*
```shl
$ docker run --rm -u $UID -it -v $LOCALPATH:/app/mysite django-tutorial-docker python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password:
Password (again):
Superuser created successfully.
```

- [ ] register the *polls*'s *Question* model in the *Django Admin*

[code difference](https://github.com/bkmagnetron/django-tutorial-docker/commit/97f9e8b46992431ebf6bec270aecff305a50ce87),
[repository at this point](https://github.com/bkmagnetron/django-tutorial-docker/tree/97f9e8b46992431ebf6bec270aecff305a50ce87)
