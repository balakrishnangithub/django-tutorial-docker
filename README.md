## intro/tutorial01

```
$ docker build -t $IMAGENAME .
$ docker run --rm $IMAGENAME python -m django --version

$ docker run --rm -v $LOCALPATH:/app/mysite $IMAGENAME django-admin startproject mysite .
```
