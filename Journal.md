##DEV JOURNAL


Before starting I felt the need of frontend developement knowledge,
 Hence did majority of chapters of freecodecamp's frontend development stream

-[x] Make Class Diagram for Devices, Users and Household

     
     Started at : 20/05/2020 11:22 AM
     Estimated Time: 60 mins
     Finished at: 20/05/2020 20:24 PM
     Remarks: Took way too long. And it still may need modification
     as I move along
     
    
=====
Emphasis 23/05

Before Login and Logout feature I am working on Bootstrap. Tried Bootstrap studio, I feel it is 
not that great, so plain css file editing is better. Used some examples from Bootstrap site.
I also wanted to make a grid of cards. Which is what I am working on at the moment.

24/05 OK, so I need to make signup view/functionality before,  login or logout.

Problem 1: Somehow, I am able to register the same user twice, even though I have put registration_form.is_valid() condition

Problem 2: When I try to debug (For problem 1), I am getting following error 
(apparantly, I can't put image in markdown, can link to local filesystem, but on github, that would be a problem)
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
    
          
===
     Inconvenience: The background page some times loads, and doesnt the other times. I guess it may be because the
     source file is being protected from being used as CDN.
     Tried to host the image on Google Drive, and then use it as CDN, but did not worked. Plus I am not too happy about the choice of image as well.
     Currenlty Imgur is working fine, but I need to use S3 at later point.
     Also, Must remember to attribute the photgrapher of the image [Photo by NeONBRAND on Unsplash]

-[ ] Add Device Page

     
     Started at : 2:15 PM
     Want to first format the date in DD MM YYY on the device card page.
     Looked up document at https://docs.djangoproject.com/en/3.0/ref/templates/builtins/#date
     and the the format in the tenplate |"d M, Y" Does not seems to work. It works now, was a typo.
     
     Also, I think in order to use celery, and sendgrid. I need to reopen user registration feature.
     So I am working on that now. Removed from done to in progress.
     
     Send grid is working, but I am not sure how to set the env variables for the secret key, in such a way, that it works
     on heroku as well. I can set the envvars in .bashrc file and run the file before the project starts. But, when I will
     push the code to github, that file should NOT be included. Hence I updated the .gitignore. Trying to make it work.
     There must be a way.
     
     
     Problem 5: Tried to solve the above problem by using pyhton decouple, as soon as I get the variable, set by .env file
     using config('SECRET_KEY') I get an exception
     
      print(config('SENDGRID_API_KEY'))
      
        File "W:\workspace\WebDev_DS\django\IoT_Dashboard\venv\lib\site-packages\decouple.py", line 124, in __init__
    for line in file_:
    
  File "C:\Python38\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

Solution to Problem 5: It was encoded as utf-16, changed it to utf-8.
OK, so this was something, I never noticed, i.e. the encoding of the file(it matters!).
I did not paid any special attention to the encoding when I created the .env file, it was in utf-16(?) format.
I referred stackoverflow, infact the error ITSELF says that. "utf-8' codec can't decode ". 
I opened the file in notepad and save as, and then chose utf-8 encoding, and it worked! Also, here I found the discussion on
discord useful, because, I initially put the value of secret key in quotes, 
but something made me recall the conversation on discord regarding AWS key, so I avoided that mistake.
     
Moved away from is_authenticated and then redirect, to decorators, since they are more concise, and easy to understand (not the actual mechanism of decorators,
which seems a bit of mystery). But it the disadvantage is that the redirect URL is not visible in the same file.
     
     Estimated Time:
     Finished at:
     Remarks:


<br>
<br>
<br>

##Format

-[ ] What needs to be done

     
     Started at : 
     Estimated Time:
     Finished at:
     Remarks:
     

  
