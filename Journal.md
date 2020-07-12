

## DEV JOURNAL

Before starting I felt the need of frontend development knowledge,
 Hence did majority of chapters of freecodecamp's frontend development stream

### Entry 1

-[x] Setup Project with correct repository

Start Commit: b6f036455dc56705f02d40e9b904068ab09367c4 [b6f0364]
End Commit: Commit: f36ab2d86718d6e2ffbc1208c268cdd993464911 [f36ab2d]

     Started at : 19/03/2020 11:22 AM
     Estimated Time: 60 mins
     Finished at: 11/04/2020 20:24 PM


​    

### Entry 2

-[x] Learn to execute merge and pull request


     Started at : 11/04/2020 20:00
     Estimated Time: 
     Finished at: 12/04/2020 15:37

​    

### Entry 3

-[x] Make Class Diagram for Devices, Users and Household


     Started at : 20/05/2020 11:22 AM
     Estimated Time: 60 mins
     Finished at: 20/05/2020 20:24 PM
     Remarks: Took way too long. And it still may need modification
     as I move along

​    

### Entry 4 

-[x] Familiarize with UI development


     Started at : 23/05/2020 11:22 AM
     Estimated Time: 60 mins
     Finished at: 23/05/2020 20:24 PM

Before Login and Logout feature I am working on Bootstrap. Tried Bootstrap studio, I feel it is 
not that great, so plain CSS file editing is better. Used some examples from Bootstrap site.
I also wanted to make a grid of cards. Which is what I am working on at the moment.

### Entry 5

     Started at : 24/05/2020 
     Estimated Time: 60 mins
     Finished at: 23/05/2020 

Realized that I need to make signup view/functionality before,  login or logout.

*Problem 1*: Somehow, I am able to register the same user twice, even though I have put registration_form.is_valid() condition

### Entry 6 

-[x] Problem 2: When I try to debug (For problem 1),
 I am getting following error 
(apparently, I can't put image in markdown, can link to local filesystem, but on GitHub, that would be a problem)

```
Error Messagedjango.core.exceptions.ImproperlyConfigured: 
Requested setting INSTALLED_APPS, but settings are not configured"
```
Solution to Problem 2: I had selected a particular view, for debugging, which does not runs the 'manage.py', which is responsible
for configuring the setting, particularly this extended line in the error message

### Entry 7 : 22/05/2020

Added/downloaded Icons and styling css and added them to correct path for reference within the pages
Also, worked on base and derived templates

### Entry 8 : 23/05/2020

Worked on creating the first model of the 'thing' i.e.  a smart device

Entry 9 : 23/05/2020

Worked on creating the sidebar and learned about styling using css and bootstrap

### Entry 10 : 24/05/2020

Worked on creating views

Updated Models

Worked on registration page/ template/ html file

### Entry 11 : 25/05/2020

Faced this problem: Data was not being saved via forms

Solution, I assumed that is_valid function will check for validity. It does, but not if you have have already saved the form.
I missed the .form_save() fx and hence I was able to 'register' with same username twice. 



### Entry 12 : 26/05/2020

*problem*

```
'*You must either define the environment variable DJANGO_SETTINGS_MODULE...*
```

solution : manage.py sets this env var.

*Problem* and its solution: In case, a custom registration form is required. We need to override the default
contrib form. I assumed that, the name that appears in the form has to given in meta class.
The reality is, that Django makes up the word itself. For example house_id will show up as House id.

*Problem* I overloaded a function, instead of a class when I wanted to make a  custom form. That was silly.

Spend too much time, theming the IDE. Plus considered about switching to VS Code, in case I get used to
professional version of Pycharm, but turns out most of the features that I use are in community version as well. 
In reality, I am investing on learning the shortcuts, which are available in the community version as well.



### Entry 13 [ Missing date]

​     Inconvenience: The background page some times loads, and doesn't the other times. I guess it may be because the
​     source file is being protected from being used as CDN.
​     Tried to host the image on Google Drive, and then use it as CDN, but did not worked. Plus I am not too happy about the choice of image as well.
​     Currently Imgur is working fine, but I need to use S3 at later point.
​     Also, Must remember to attribute the photographer of the image [Photo by NeONBRAND on Unsplash]

### Entry  14 :  27/05/2020

Add Device Page

 Want to first format the date in DD MM YYY on the device card page.
 Looked up document at  https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
 and the the format in the tenplate |"d M, Y" Does not seems to work. It works now, was a typo.

 Also, I think in order to use celery, and sendgrid. I need to reopen issue, user registration feature on github.
 So I am working on that now. Removed from done to in progress.

 Send grid is working, but I am not sure how to set the env variables for the secret key, in such a way, that it works
 on heroku as well. I can set the envvars in .bashrc file and run the file before the project starts. But, when I will
 push the code to github, that file should NOT be included. Hence I updated the .gitignore. Trying to make it work.
 There must be a way.



### Entry  15: 29/05/2020

Made a favicon[TB -> thingsbaord] using online tool favicon.io



### Entry 17: 28/05/2020

Configure Postgres


     Started at : 18:59
     Estimated Time: 30 mins
     Finished at: 21:24 PM
     Remarks: Also, migrate the data using dumpdata command

*Problem*: While switching from sqlite to postgres, I first need to apply the existing migrations(?)
While, Migrating, i.e. makemigrations, and then migrate. I get the following error.

`TypeError: __str__ returned non-string (type Address)`

In order to get a small win, I renamed a model class from value_stream to camel case, PEP 8 style. Complicated further.

Did you rename the dashboard.value_stream model to ValueStream? [y/N] y
You are trying to add a non-nullable field 'mfg' to things without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py

https://stackoverflow.com/questions/16046478/django-model-nullable-field

### Entry 18: 28/05/2020

Worked on Manufacturer ,device and address template

Worked on their models ,views

### Entry 18: 30/05/2020

Completed the work on forms

### Entry 19: 30/05/2020

User's image was not being uploaded correctly, resolved that

\Wanted to show a clear message to a user why their form was rejected. In a way it is shown, but not formatted for easy reading

wanted to create a shortcut for git add ., commit and push, like in class. But found a npm package git-upload, npm install git-update.

Usage: gitu COMMIT MSG

### Entry 20 : 2/06/2020

​     *Problem* Tried to solve the above problem by using pyhton decouple, as soon as I get the variable, set by .env file
​     using config('SECRET_KEY') I get an exception
​     
​      print(config('SENDGRID_API_KEY'))
​      
​        File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\decouple.py", line 124, in __init__
​    for line in file_:

`  File "C:\Python38\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
`
*Solution*  It was encoded as utf-16, changed it to utf-8.
OK, so this was something, I never noticed, i.e. the encoding of the file(it matters!).
I did not paid any special attention to the encoding when I created the .env file, it was in utf-16(?) format.
I referred stackoverflow, in fact the error ITSELF says that. "utf-8' codec can't decode ". 
I opened the file in notepad and save as, and then chose utf-8 encoding, and it worked! Also, here I found the discussion on
discord useful, because, I initially put the value of secret key in quotes, 
but something made me recall the conversation on discord regarding AWS key, so I avoided that mistake.
     
Moved away from is_authenticated and then redirect, to decorators, since they are more concise, and easy to understand (not the actual mechanism of decorators,
which seems a bit of mystery). But it the disadvantage is that the redirect URL is not visible in the same file.

### Entry 21 : 31/05/2020

Worked on using date picker for selecting dates in forms



### Entry 22 : 31/05/2020

Worked on sentry for logging and notifying errors in the application

### Entry 23 : 31/05/2020

Worked on decouple library for securing secret key, instead of environment variables

Created procfile for heroku deployement

### Entry 24 : 1/06/2020

Unit Testing: used django test library, tests.py

Checks for whether more than one email can exists etc

Test Fixtures: The preparation/ setup for the test to execute

Tear Down or cleanup: Removing the side effects of the test execution.

Both of these are handled by django test library, it creates the temporary database in case the test is related to models, and destroys it , when test is completed.

### Entry 25 :  1/06/2020

Created Entity relationship diagram with graphviz

### Entry 26 :  2/06/2020

Worked on registration ,profile and base template

Made the UI look better using bootstrap classes

Made First page load faster by compressing the background image

### Entry 27 :  3/06/2020

Heroku deployment, migrations and testing

### Entry 28 :  4/06/2020

Refactored,made the notification as separate app. so that this notifications service can be resued later on for example sms and push notfications can be added

Celery

ERD Update

Password reset

### Entry 29 :  1/06/2020

json table dumps

Updated Readme

Updated models for nullable values



### Entry 30:  5/06/2020

Worked Redis Caching issue. Newly created device will not appear because of time to life. So If I install a device it will appear after max of TTL

---------------------------------



## Todo Future:

1. GeoDjango and maps
2. Attribute photos
3. Change The image background on the login page to css pattern so it loads faster
4. Change the form input field style, should not span the whole width
5. Add the 



-----------------------------------

# Error Logs

## These are error notes and could be ignored



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



UTF-8 Errr again-changed to UTF-8, as earlier.

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

##Entry 13

-[ ] Remodeling


     Started at : 2 a hours
     Estimated Time: 6 hours
     Finished at:
     Remarks:



Create User -> Using Registration Forms

WTH!! Changing the model was a big mistake. Should have just stuck to whatever I was thinking, and should not have though of improvingfeatures.

migrations are not working. for example

```
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\db\backends\utils.py", line 86, in _execute
    return self.cursor.execute(sql, params)
django.db.utils.ProgrammingError: column dashboard_manufacturer.address_id does not exist
LINE 1: ...ufacturer"."id", "dashboard_manufacturer"."name", "dashboard...
                                                             ^
```

There is no reference to column dashboard_manufacturer. Address_id . And django is supposed to create this column itself.!!

Solution: 18:20 PM, after 2 hours of despair. Dropping the table, delete the migrations, and then again make migrations seems to work. 

Forgot to add {% load crispy_forms_tags %} at the start, the error is not helpful, but it mentions crispy casually.


Problem X: I spent some time fixing a problem that was not a problem, django was invalidating a form, because of duplicate value on pk.

30/05/2020 6:48 PM : Wanted to show a clear message to a user why their form was rejected. In a way it is shown, but not formatted.

Problem: When uploading a picture I get this error, I provided a valid image while uploading via form, though.

```
'Image', ['This field is required.']
```

Solution: I did not put default image in there and also missed upload_to param, additionally i also added enc_typ in the template(but I did not verified its effect)

Additionally, there was an issue with me copying wring section from the django documentation

from the page https://docs.djangoproject.com/en/3.0/howto/static-files/ . I was supposed to get this

```
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

but instead I copied the static file section in settings.py

```
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

Side Note: It seems the darkness of the cell in my git contribution graph seems to be relative. Earlier I got a very dark green on 5 commits, but now 5 is light green. May be I am wrong. https://github.com/isaacs/github/issues/627

-----------------


-[ ] Change The Date input on UI to datepicker

It can be done via overriding the widget, in case of ModelForms, it is slightly different

https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields   &

https://stackoverflow.com/questions/49440853/django-2-0-modelform-datefield-not-displaying-as-a-widget


     Started at : 00:39 PM
     Estimated Time: 30 mins
     Finished at: 2:31 AM
     Remarks: 



```
remote: -----> $ python manage.py collectstatic --noinput
remote:        Traceback (most recent call last):
remote:          File "manage.py", line 21, in <module>
.

.



remote:        https://devcenter.heroku.com/articles/django-assets
remote:  !     Push rejected, failed to compile Python app.
remote:
remote:  !     Push failed
remote: Verifying deploy...
remote:
remote: !       Push rejected to thingboard.
remote:
To https://git.heroku.com/thingboard.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://git.heroku.com/thingboard.git'
```

Solution: In the settings.py file add 

```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
##Entry 18
Problem next: on accessing the site, i get error that i need to see the logs via

```
 heroku logs --tail
```

I get the following logs 

```verilog
2020-05-30T14:57:58.000000+00:00 app[api]: Build started by user manasvi.tyagi@gmail.com
2020-05-30T14:58:37.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/c802be5a-6c0c-4e32-9005-0e0d33cf40a1/activity/builds/c3d4cda6-f521-4904-98f3-107162d15c23
2020-05-30T15:11:18.000000+00:00 app[api]: Build started by user manasvi.tyagi@gmail.com
2020-05-30T15:11:55.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/c802be5a-6c0c-4e32-9005-0e0d33cf40a1/activity/builds/529d7920-718b-4221-94b9-a4f82ed22d64
2020-05-30T15:14:41.000000+00:00 app[api]: Build started by user manasvi.tyagi@gmail.com
2020-05-30T15:15:19.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/c802be5a-6c0c-4e32-9005-0e0d33cf40a1/activity/builds/e608a6d5-fcbf-4ed4-8c18-1b71841452c6
2020-05-30T15:18:04.000000+00:00 app[api]: Build started by user manasvi.tyagi@gmail.com
2020-05-30T15:18:41.000000+00:00 app[api]: Build failed -- check your build output: https://dashboard.heroku.com/apps/c802be5a-6c0c-4e32-9005-0e0d33cf40a1/activity/builds/fd790663-54b0-46d6-bb70-f1b77965cc4e
2020-05-30T15:19:43.000000+00:00 app[api]: Build started by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.568578+00:00 app[api]: Attach DATABASE (@ref:postgresql-slippery-34466) by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.568578+00:00 app[api]: Running release v3 commands by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.583207+00:00 app[api]: Release v4 created by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.583207+00:00 app[api]: @ref:postgresql-slippery-34466 completed provisioning, setting DATABASE_URL. by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.845937+00:00 app[api]: Release v5 created by user manasvi.tyagi@gmail.com
2020-05-30T15:20:35.845937+00:00 app[api]: Deploy a5c407e4 by user manasvi.tyagi@gmail.com
2020-05-30T15:20:45.000000+00:00 app[api]: Build succeeded
2020-05-30T15:21:04.909254+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/" host=thingboard.herokuapp.com request_id=89bbbdbe-d3cd-4765-b315-c4d1d4d54a20 fwd="101.100.128.204" dyno= connect= service= status=503 bytes= protocol=https
2020-05-30T15:21:06.239655+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/favicon.ico" host=thingboard.herokuapp.com request_id=67b67c3e-4404-4db0-b806-3ab0ea39af8e fwd="101.100.128.204" dyno= connect= service= status=503 bytes= protocol=https
```

I did not configured postgres, so that was expected.

Solution: Add a  Procfile in the project root.

Problem Next: The {UI/Page is all messed up. Probably because the static files contain the css, and I need to host it somewhere.

-------------

Setup S3

<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>

31/06/2020 6:04 AM : So after struggling for about 2 hours. The problem is that python decouple is not working somehow for AWS keys!!

Commented out line does not works


```
# AWS_ACCESS_KEY_ID = Config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = Config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = Config('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = 'AKIA3P7JVJJBEXXXXXXXX'
AWS_SECRET_ACCESS_KEY = 'i0F4vr7ENwg82JFFVJJBEXXXXXXX'
AWS_STORAGE_BUCKET_NAME = 'thingboard-bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = Config('DEFAULT_FILE_STORAGE')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

-[ ] Create Entity Relationship Diagram

Since I changed the modeled a lot, i need to recreate it. Because of lack of time, i need to automate it, via library that I found, graphviz

Apparently graphiviz had the following problem in windows, it needs additional non python package to be installed. Installing it did not worked!

    graphviz_wrap.obj : error LNK2001: unresolved external symbol agwrite
    graphviz_wrap.obj : error LNK2001: unresolved external symbol agisdirected
    graphviz_wrap.obj : error LNK2001: unresolved external symbol agopen
    graphviz_wrap.obj : error LNK2001: unresolved external symbol agraphof
    graphviz_wrap.obj : error LNK2001: unresolved external symbol Agstrictdirected
    build\lib.win-amd64-3.8\pygraphviz\_graphviz.cp38-win_amd64.pyd : fatal error LNK1120: 50 unresolved externals
        error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.24.2
    8314\\bin\\HostX86\\x64\\link.exe' failed with exit status 1120
        ----------------------------------------
    ERROR: Command errored out with exit status 1: 'w:\workspace\webdev_ds\django\iot_dashboard\venv\scripts\python
    .exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\manas\\AppData\\Local\\Temp\\pip-i
    nstall-bsq0yl66\\pygraphviz\\setup.py'"'"'; __file__='"'"'C:\\Users\\manas\\AppData\\Local\\Temp\\pip-install-b
    sq0yl66\\pygraphviz\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"
    '"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' build_ext '-IC:\Program Fi
    les (x86)\Graphviz2.38\include' '-LC:\Program Files (x86)\Graphviz2.38\lib\release\lib' install --record 'C:\Us
    ers\manas\AppData\Local\Temp\pip-record-711n49m1\install-record.txt' --single-version-externally-managed --comp
    ile --install-headers 'w:\workspace\w

So I switched to github -> django-dia which creates a .dia file, for which  I had to install a tool to open it and the final diagram is not that great because internal models are now visible, and the resolution is not great, so not really readable. That is the reason I have kept the previous model in readme as well to present the idea. I could have created the diagram manually much faster, as I did with version 1.

python manage.py graph_models dashboard users -o EntityRelationshipDiagramSelective.png 


     Started at : 8:19 PM
     Estimated Time: 15 mins
     Finished at: 9:48 PM
     Remarks: django graphviz does not works easily on windows.! Also there is a buig in graphviz, if you pass an application which has no models, it will crash, and gives the following error. The command used to create selective models is also given

------

```
PS W:\workspace\WebDev_DS\django\IoT_Dashboard> python manage.py graph_models dashboard users notifications -o EntityRelationshipDiagramSelective.png
System check identified some issues:

WARNINGS:
?: (urls.W005) URL namespace 'admin' isn't unique. You may not be able to reverse all URLs in this namespace
Traceback (most recent call last):
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\apps\registry.py", line 155, in get_app_config
    return self.app_configs[app_label]
KeyError: 'notifications'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\core\management\__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\core\management\__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\core\management\base.py", line 328, in run_from_argv
    self.execute(*args, **cmd_options)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\core\management\base.py", line 369, in execute
    output = self.handle(*args, **options)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django_extensions\management\utils.py", line 62, in inner
    ret = func(self, *args, **kwargs)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django_extensions\management\commands\graph_models.py", line 238, in handle
    graph_models.generate_graph_data()
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django_extensions\management\modelviz.py", line 90, in generate_graph_data
    self.process_apps()
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django_extensions\management\modelviz.py", line 279, in process_apps
    app = apps.get_app_config(app_label)
  File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\django\apps\registry.py", line 162, in get_app_config
    raise LookupError(message)
LookupError: No installed app with label 'notifications'.
Sentry is attempting to send 0 pending error messages
Waiting up to 2 seconds
Press Ctrl-Break to quit
```




Create User -> Using Registration Forms

https://stackoverflow.com/questions/1644455/django-form-not-saving-default-image-name

https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield

Quit the server with CTRL-BREAK.
Session data corrupted

https://stackoverflow.com/questions/38970832/session-data-corrupted-in-django

`heroku pg:psql`.

heroku restart; heroku pg:reset DATABASE --confirm thingboard; heroku run rake db:migrate


`heroku pg:psql`.



```
Received invalid task message: Refusing to deserialize untrusted content of type json (application/json)
```



 Note
tyagi.tech does not work, but www.tyagi.tech does ! Something to do with dns configuration, but could not find anything on the controlpanel of domain provider.

##Entry 26 : Note
application cache on redis
Read cache can help in minimizing the db reads.  So the idea is that, the bottleneck in some application performance is hard disk read and write. And thats the DB operations in web apps mostly(?) To solve this, redis helps , because it is faster, because it works in memory, i.e. RAM. But I do not know how to us in my application. 

But, when I make writing to IoT devices feature. And my application can can receive million of data points, this will be very suitable.

https://realpython.com/caching-in-django-with-redis/

https://devcenter.heroku.com/articles/celery-heroku



https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

##Entry 26 : Note
Extremely misleading error

|  Exception Type: | InvalidCacheBackendError                                     |
| ---------------: | ------------------------------------------------------------ |
| Exception Value: | `Could not find backend 'django_redis.cache.RedisCache': No module named 'django_redis'` |

not really misleading, but the rest of therror is, I just forgot to put pip freeze > req.....txt. Which created problem on heroku

heroku run python manage.py migrate       || Saved a of of time

So the problem I faced is that after adding a smart device, I am unable to see the device, immediately, and this has caused like lot of loss of confidence and therefore distraction. The thing is, the cache is not returning from permanent db., it is for fast response and may not reflect the true state. The variable that i mindlessely pasted from page, CACHE_TTL, stands for time to live, which I am guessing is the time after it will sync with postgres, where the accurate data is present. So the caches should not be used where absolute truth depends on the order of operation.



