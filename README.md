IoT Dashboard for devices in a Premises  :
----------------------------------------------------
### Problem It Solves
Offers single point of management of 'on premise' smart devices.

##### A User can logon to his home's dashboard and see useful info about smart devices installed on premise.

Following Features are planned
- Register A User
- Login/Logout User
- Register Devices
- Add a picture of the device
- Delete a Device
- See the dashboard of user's devices, with some KPIs
- On clicking the Device Card, Some additional info, such as trend should be visible
- Send Notification when the lifetime of the 'thing' is about to end.

---------------------------------
Following Devices are supported 
---------------------------------
- **Energy Meter**
    - Your Property's Consumption pattern
    - Pay bill reminder
    
- **Water Meter**
    - Your Property's Consumption pattern
    - Pay bill reminder
    
- **Coffee Machine**
    - Usage Pattern
    - Coffee buying reminder
    
- **Smart Light**
    - Turn it OFF or ON, Usage Pattern, 
 
- **Bike**
    - Track the Current location
    - Distance Travelled Till date
    - Reminder to change tire
    - Reminder to change Brakes
    
- **Fridge**
    - Is Something Missing
    - Energy Consumption
    
- **Door Lock**
    - Lock Unlock History  [Who Did it and When]
    - Lock Unlock from Web Page
    
- **Vacuum Cleaner**
    - Running Hours
    - Time to change dust bag


## Entity Relationship diagram

<img src="https://i.imgur.com/205T6KZ.png">
<br>

## Note

 Since most smart devices, like Smart bulb, Energy Meter have different
protocols and message structure. In Real market, we need smart hub like 
alexa or google home (or even better) common agreed standards to access the
 requisite data for this application. In this application W have assumed 
 a convenient format for the information interchange.

## How server side rendering(SSR) works?

In this architecture, the Markup or the template, along with dynamic functionalities are constructed by the server.
Post construction the document is sent to the client in its entirety. While the opposite is client side rendering(CSR), In which
the page or a document is constructed by the client with the help of some scripting mechanism, for example Javscript famework 
such as React or Angular. SSR is heavy on the server, because the entire document has to be made by the server, on the other hand 
CSR distributes the load to the client as well. Another effect as a result of the difference is that, Each response on case of SSR
would be smaller, however for similar features, CSR would require lower number of reponses or round trips, but each one would be much larger size.


:four_leaf_clover:

 
