## DEV JOURNAL

Before starting I felt the need of frontend development knowledge,
 Hence did majority of chapters of freecodecamp's frontend development stream

-[x] Make Class Diagram for Devices, Users and Household


     Started at : 20/05/2020 11:22 AM
     Estimated Time: 60 mins
     Finished at: 20/05/2020 20:24 PM
     Remarks: Took way too long. And it still may need modification
     as I move along

​    

**23/05**

Before Login and Logout feature I am working on Bootstrap. Tried Bootstrap studio, I feel it is 
not that great, so plain CSS file editing is better. Used some examples from Bootstrap site.
I also wanted to make a grid of cards. Which is what I am working on at the moment.

24/05 OK, so I need to make signup view/functionality before,  login or logout.

Problem 1: Somehow, I am able to register the same user twice, even though I have put registration_form.is_valid() condition

Problem 2: When I try to debug (For problem 1), I am getting following error 
(apparently, I can't put image in markdown, can link to local filesystem, but on GitHub, that would be a problem)

```
Error Messagedjango.core.exceptions.ImproperlyConfigured: 
Requested setting INSTALLED_APPS, but settings are not configured"
```
Solution to Problem 2: I had selected a particular view, for debugging, which does not runs the 'manage.py', which is responsible
for configuring the setting, particularly this extended line in the error message

Solution to Problem 1: I assumed that is_valid function will check for validity. It does, but not if you have have already saved the form.
I missed the .form_save() fx and hence I was able to 'register' with same username twice. 
```
'*You must either define the environment variable DJANGO_SETTINGS_MODULE...*
```

manage.py sets this env var.

problem 3 and its solution: In case, a custom registration form is required. We need to override the default
contrib form. I assumed that, the name that appears in the form has to given in meta class.
The reality is, that Django makes up the word itself. For example house_id will show up as House id.
Problem 4: I overloaded a function, instead of a class when I wanted to make a  custome form. That was silly.

Spend too much time, theming the IDE. Plus considered about switching to VS Code, in case I get used to
professional version of Pycharm, but turns out most of the features that I use are in community version as well. 
In reality, I am investing on learning the shortcuts, which are available in the community version as well.




-[x] Make Login/Logout Feature


     Started at : 20/05/2020 10:29 PM
     Estimated Time: 90
     Finished at: 26/05/2020
     Remarks: Took way too long, not because it was difficult, but because, I did not planned in between steps. Plus
     I was too slow.

​          

​     Inconvenience: The background page some times loads, and doesn't the other times. I guess it may be because the
​     source file is being protected from being used as CDN.
​     Tried to host the image on Google Drive, and then use it as CDN, but did not worked. Plus I am not too happy about the choice of image as well.
​     Currently Imgur is working fine, but I need to use S3 at later point.
​     Also, Must remember to attribute the photographer of the image [Photo by NeONBRAND on Unsplash]

-[ ] Add Device Page


```
 Started at : 2:15 PM
 Want to first format the date in DD MM YYY on the device card page.
 Looked up document at  https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
 and the the format in the tenplate |"d M, Y" Does not seems to work. It works now, was a typo.
 
 Also, I think in order to use celery, and sendgrid. I need to reopen issue, user registration feature on github.
 So I am working on that now. Removed from done to in progress.
 
 Send grid is working, but I am not sure how to set the env variables for the secret key, in such a way, that it works
 on heroku as well. I can set the envvars in .bashrc file and run the file before the project starts. But, when I will
 push the code to github, that file should NOT be included. Hence I updated the .gitignore. Trying to make it work.
 There must be a way.
```


​     
     Problem 5: Tried to solve the above problem by using pyhton decouple, as soon as I get the variable, set by .env file
     using config('SECRET_KEY') I get an exception
     
      print(config('SENDGRID_API_KEY'))
      
        File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\decouple.py", line 124, in __init__
    for line in file_:

`  File "C:\Python38\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
`
Solution to Problem 5: It was encoded as utf-16, changed it to utf-8.
OK, so this was something, I never noticed, i.e. the encoding of the file(it matters!).
I did not paid any special attention to the encoding when I created the .env file, it was in utf-16(?) format.
I referred stackoverflow, in fact the error ITSELF says that. "utf-8' codec can't decode ". 
I opened the file in notepad and save as, and then chose utf-8 encoding, and it worked! Also, here I found the discussion on
discord useful, because, I initially put the value of secret key in quotes, 
but something made me recall the conversation on discord regarding AWS key, so I avoided that mistake.
     
Moved away from is_authenticated and then redirect, to decorators, since they are more concise, and easy to understand (not the actual mechanism of decorators,
which seems a bit of mystery). But it the disadvantage is that the redirect URL is not visible in the same file.

Problem 6: Forgot to add form.save() after validation. Hence could not locate the database entry.
     
     Estimated Time: 2 hours
     Finished at: Actually took whole working day, because of intermediate steps. 
     Remarks:

<br>

-[ ] Configure Postgres


     Started at : 18:59
     Estimated Time: 30 mins
     Finished at: 21:24 PM
     Remarks: Also, migrate the data using dumpdata command

<br>
Problem 7: While switching from sqlite to postgres, I first need to apply the existing migrations(?)
While, Migrating, i.e. makemigrations, and then migrate. I get the following error.

`TypeError: __str__ returned non-string (type Address)`

In order to get a small win, I renamed a model class from value_stream to camel case, PEP 8 style. Complicated further.

Did you rename the dashboard.value_stream model to ValueStream? [y/N] y
You are trying to add a non-nullable field 'mfg' to things without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py

https://stackoverflow.com/questions/16046478/django-model-nullable-field

then new error

`    return '<%s: %s>' % (self.__class__.__name__, self)
TypeError: __str__ returned non-string (type NoneType)
`

Although all my models are returning string! 

ok, so apparently, casting using, str(), makes the problem go away, **BUT**, new error

`ValueError: Cannot serialize: <Address: None>
There are some values Django cannot serialize into migration files.
`

This error occurs, when we have a method in a model class according to

https://stackoverflow.com/questions/32016191/django-1-7-migration-cannot-serialize-a-class-method

and the solution is to add a decorator @deconstructible , I do not have a methid in this class, why does this error occurred?.

```python
class Address(models.Model):
    street = models.CharField(max_length=150, blank=True, null=True)
    zip = models.CharField(max_length=10, default="06001")

    def __str__(self):
        return str(self.street)
```

Not sure If this is right thing to do. Most probably not, because, I am not aware about the side effects.

use  python manage.py migrate --run-syncdb to check the connection is fine

Error

```
django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: No module named 'psycopg2'
```

Solution

```
pip install psycopg2
```

Another issue, 

```
TypeError: Field 'id' expected a number but got <Address: 38 Windsor>.
```

Solution: deleted all the migrations, took a backup, of course, and ran migrations again. done. Now I am running on postgres .

Well, I forgot to migrate the actual data, so the job is not done.



UTF-8 Error again-changed to UTF-8, as earlier.

loadata json command **error**:

```
django.db.utils.IntegrityError: Problem installing fixture 'W:\workspace\WebDev_DS\django\IoT_Dashboard\db.json': Could not load contenttypes.ContentType(pk=1): duplicate key value violates unique constraint "django_content_
type_app_label_model_76bd3d3b_uniq"
DETAIL:  Key (app_label, model)=(admin, logentry) already exists.
```

**solution**: use python manage.py shell

```
 >>>from django.contrib.contenttypes.models import ContentType
 >>>ContentType.objects.all().delete()
```

ITS DONE!

------

## 

-[ ] Remodeling


     Started at : 2 a hours
     Estimated Time: 6 hours
     Finished at:
     Remarks:

wanted to create a shortcut for git add ., commit and push, like in class. But found a npm package git-upload, npm install git-update.

Usage: gitu COMMIT MSG

Create User -> Using Registration Forms

## Journal entry  template

-[ ] What needs to be done


     Started at : 
     Estimated Time:
     Finished at:
     Remarks:

------


Create User -> Using Registration Forms

Create Manufacturer -> Only Admin Can Do this

Create Device Types -> Only Admin Can Do this

Add Device -> From The List of Device Types

Todo:
1. GeoDjango and maps

2. Attribute photos

