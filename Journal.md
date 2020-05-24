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
I also wantend to make a grid of cards. Which is what I am working on at the moment.

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

```
'*You must either define the environment variable DJANGO_SETTINGS_MODULE...*
```

manage.py sets this env var.

-[ ] Make Login/Logout Feature

     Started at : 20/05/2020 10:29 PM
     Estimated Time: 90
     Finished at: 
     Remarks: 
          
===

-[ ] Make models in Django

     
     Started at : 
     Estimated Time: 20 mins
     Finished at:
     Remarks:

-[ ] Make UI Wire-frame /  Sketch

     
     Started at : 
     Estimated Time:
     Finished at:
     Remarks:

-[ ] Make Templates

    
     Started at : 
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
     

  
