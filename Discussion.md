##
# **Manasvi Tyagi**

**1525972**

**-------------------------------------------------------------------------------------------------------------------------------------**

## Architecture: -

**When would you prefer to develop an Assignment 1 style web application (Server-side rendering, serving HTML)?**

1. A smaller project, when there is no requirement of future expansion of the application. For example, if we know that there would be no mobile clients in future. In case we have REST APIs, we can use mobile clients for example an android or iOS app; with template-based application there is no scope of integration. Therefore, for smaller and simpler application we can use template based or server-side rendered applications.
2. A second suitable candidate will be static websites, where there is minimum requirement of server round trips, for example a news website, a notice board etc.

**When would you prefer an Assignment 2 one (REST API &amp; Single Page Application)?**

Except the situations described in previous question ,I would prefer REST API based Single Page Applications most of the time _because_: -

1. There is a possibility of multiple type of clients (Web applications, Mobile applications, or even third-party applications).
2. Second benefit is that when a new data is required, only the payload (typically JSON) needs to be sent from the server, which requires lower bandwidth than whole template.
3. Single Page applications can also be used offline once loaded (sometimes), for example a calculator application can be developed as SPA and once rendered by client, it can be used even without internet.

Version Control: -

What is git and what is it used for?

Git is a graph-based version-control system, which contains both client and server. A git client can work independently, but using the server, capabilities are enhanced. We can use many publicly available git servers such as githhub, gitlab etc. However, we can also deploy our own git server such as bonobo on windows (https://bonobogitserver.com/)

Its uses are :-

1. tracking source code change.

2. Coordinating development amongst many developers.

3. Code review

4. Integration with continuous Integration and Deployment tools.

5.It is also beneficial for backup purposes but that is not the primary use case.

It was developed by Linus Torvalds for of the Linux development is free and open-source slicensed under GNU GPL Version

**List 3 git commands you&#39;ve learned in this course.**

Git init -\&gt; used to initialize a directory as git repository

Git status -\&gt; used to check the changes done with respect to the master on server, it also informs about staging status

Git add .

**What is GitHub and what is it used for?**

![](RackMultipart20200706-4-1esbxc3_html_bbeadf276ffa59ba.png)

Github is a publicly available git server, there are others like gitlab, bitbucket etc. Although git can work on local system without a server, a server would enhance its capabilities because

- Allows remote backup
- It allows coordination with other programmers, via git server&#39;s remote repositories

**What is Kanban and what is it used for?**

Kanban is a product development management methodology, with clear idea for each team members to see their role and progress of the team as well as the entire project.

It involves three principles

1. Visualize what you do: This is done with the help of Kanban boards, usually contains a board for each

A) The work to be done

B) The work in progress

C) The finished work

1. Limit or quantify work in progress (WIP)
2. Enhance flow: The team members can visualize the work that is pending what they have done.

- **What is Markdown and what is it used for?**

Markdown is meta information added to document in order to format it. The main document is in plain text format, but a markdown file has the extent ion or \*.md or \*. markdown. It is standardised format and the specs are available at [https://spec.commonmark.org/](https://spec.commonmark.org/)

Platform vs Infrastructure: -

**What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?**

PaaS is form of cloud computing service, the way it differs from IaaS is that it is more abstracted from bare metal computing.

**Pros** include

1. Easier deployment: As compared to owning a server or even using IaaS, PaaS requires lower time and skills to deploy and therefore lower costs.
2. Easier Configuration: Hence lower time configuring leading to lower costs.
3. As compared to owning a server, it is easier to scale.
4. As compared to owning a server, the benefits of pay as you go applies.

**Cons**

1. Compared to IaaS it costs more to run.
2. Not all services are provided, for example static files are not supported by Heroku.
3. Since we cannot use containers, they can be difficult to migrate from one provider to other.

- **What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?**

Again, it is a form of cloud computing, and is less abstracted when compared to PaaS

**Pros** include

1. Infrastructure as a service are cheaper to run, as compared to PaaS
2. Compared to owning a server, it is easier to scale.
3. Compared to owning a server, it is cost effective, they can cost 3x - 7x cheaper than owning the server because of economies of scale as per this paper [https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-28.pdf)

**Cons**

1. Compared to PaaS it is more complex to configure and requires more skill
2. If we use proprietary database or some cloud vendor specific technology, it can be difficult to migrate
3. Requires Application to be built specific to cloud deployment.
4. Data security can be a concern for some agencies.
5.

Web Frameworks: -

**What is Django? What are some of its useful features? - What is a model? - What is a view?**

Django is an open-source web applications framework. Which means it is a set of libraries which makes it easier to build complete modern web application easily. It is based on Model-View-Controller architecture, although it is more appropriate to call it Model Template and View architecture

Model - Database, in case of Django we use Object Relational Mapping i.e. ORM

View - These are the HTTP responses, or could be plain text as well, serialized as http response. In conventional sense, the Django view is a controller.

Template - conventionally, the Django template is the view, used to present the User interface to the client.

Additionally, it has the following features

- It includes a web server;
- Admin panel
- Commonly used features such as Forms, validations, file handling etc
- An ORM (Object Relational Mapper);
- HTTP libraries;
- A Python unit test framework.
- Database migrations support

**Name two other popular non-Python web frameworks.**

- Spring Framework in Java
- Ruby on Rails (Perl)

**What is WSGI?**

It is the web server in Python world, it separates the web applications from the server. To be specific, Web Server Gateway Interface specifies how a web server communicates with web applications, and how web applications can be sequenced together to process web requests. If a web framework is compatible with WSGI, it can be guaranteed to run on any server that is WSGI compatible.

**What is ASGI?**

Asynchronous Server Gateway Interface is a successor to WSGI, most notable feature is its asynchronous compatibiltiy (although it is backwords compatible wirh WSGI),. In Django&#39;s context, starting from 3.0 we can use ASGI. What it means in real world is that we can write async functions for example asynch views like

**async**** def ****view** (request):

**await** asyncio.sleep(0.5)

**return** HttpResponse(&quot;Hello, async world!&quot;)

although,asynchronous features like channels were already compatible with WSGI

WSGI provided a standard for synchronous Python apps, whereas ASGI provides one for both asynchronous and synchronous apps

Performance wise according to async version is more stable in case of failures ([https://arunrocks.com/a-guide-to-asgi-in-django-30-and-its-performance/](https://arunrocks.com/a-guide-to-asgi-in-django-30-and-its-performance/))

**What is celery and what are task queues used for?**
It is like outsourcing a task in async manner. What it means is , that a task is queued in a buffer(for example in Redis, could be RabbitMQ), and
the executer will complete the task, out of context of the outsourcer. In assignment 1's case, django outsources a task, by placing the task in Redis queue.

Databases **:** -

What is PostgreSQL?

PostgreSQL is an open source relational database management system, started as INGRES in 1977. It has most of the fatures required for any large scale modern applications such as:-

- It supports ACID transactions. i.e. atomicity, consistency, isolation, durability. What it means is that we can use it transactional records such as financial transactions. This is not possible in some distributed databases, where consistency is not guaranteed across the distributed records

- Provides admin tools via a web console called as PGAdmin.
- Compatible with most major languages such as Java, Python, JavaScript, C++ etc.
- Foreign keys
- Trigger
- Views
- Aggregate functions
- Index methods etc.

**Using StackShare, list 3 well-known companies that use PostgreSQL**.

1. Reddit
2. Instagram (Facebook)
3. Spotify

- **List two other well-known databases**.

1. Oracle
2. MongoDB

What are some of the pros and cons of using an Object Relational Mapper (ORM)?

ORM provides a way to abstract the SQL queries from the programming language, it does it via mapping the class to the database table. In short it makes the object of class to behave as a database table.

Pros

1. No need to write SQL queries
2. It makes the application database independent, i.e. we can seamlessly switch from one database to another (for example as we did from SQLite to Postgres in assignment 1)
3. Makes the whole application more object oriented, hence it makes it more consistent.
4. We do not have to worry about security loopholes like SQL injection

Cons

1. Complex queries can lead to performance issues if not written properly.
2. N+1 problem which can lead to more roundtrips, or query executions than ideally required ([https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping](https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping)) . It happens in case of queries are issued for the parent record, and then one query for each child record. Although it can be avoided with the features provided in the ORMs, but it is generally considered a issue with ORMs
3. It can lead to ignorance of basic SQL, if we directly use ORMs first without learning in SQL.

**What is the purpose of database migrations?**

Database migrations provide us a way to change the database schema in a step by step manner, with the option of moving back, i.e. doing a rollback in case it is required. The changes once made in the models can be used to create migrations file(a record of changes in the database) using &#39;makemigrations&#39; command and then followed by actually making the database changes by issuing &#39;migrate&#39; command.

**What is redis and what are two things it can be used for?**

Redis is in-memory data structure record. What it means is that the data resides in RAM and hence it is faster than normal databases (being developed in C also helps). It also means that it is non persistent, and hence it is volatile. Most commonly used data structure is key value pair.

Main usage of Redis is

1. Caching
2. Message Broking, i.e. routing messages.

**Why do we use caches?**

Cache ** ** is a temporary storage area where the data is stored so that in future, data can be served faster. Hence for caching, we need to use faster form of memory, in case of databases, RAM is the preferred storage.

HTTP &amp; REST: -

Which four HTTP methods does REST use for performing CRUD operations?

1. Post - Create
2. Get – Read
3. Put for update
4. Delete for deleting a record

What is Django REST Framework used for?

Django REST framework provides the library for building the API serving capabilities to Django applications. Although we can return a JSON response which will technically be a JSON REST API, but DRF provides a &quot;out of the box&quot; classes which can be used with varying features to make a view class as REST API server. At the core it serializes the model into JSON response. It provides a way to respond to all http methods i.e. get, post, update, delete etc.

**What is serialization and why do we use it?**

Serialization means that an object that is native to a language, for example an object of class in python (could be a model class), is converted into a format that is interoperable, i.e. = language independent. For example, a python model class is _serialized_ into a JSON format.

**Which type of object serialization notation is most commonly used on the web?**

JSON – JavaScript Object Notation

**What is Postman and what is it used for?**

Postman is an API client for testing APIs, it therefore helps in the development of the API. In theory it basically a web browser for developers, because the browser executes the same HTTP method as Postman does. But it has additional developer specific features like :-

1. We can write automated test cases
2. Save a set of requests, called collections, so that we can use it later for testing.
3. Document the API, i.e. its expected headers and response.

**What are websockets and what are they used for**?

In normal HTTP request the data flows to the client only when client asks for it, this is half duplex communication. Additionally, the connections is closed as soon as the request is over, essentially making another call for another data point .

In WebSocket connection, the connection remains open and the data can be sent to the client even if the client has not asked for it. This saves a lot of requests in case the data is updated in the sever, because the client does not have to ask explicitly each time. Hence, in case there is frequently updated data on the server and clients require it, WebSocket&#39;s are faster and requires lower bandwidth. They start with ws:// as opposed to http.

JavaScript: -

**What is NodeJS and how is it different from in-browser Javascript?**

Its is open source JavaScript runtime built over Chrome&#39;s V8 runtime engine. Its use case is similar to Django i.e. we can use it to build and server web applications. It is not different from the core of chrome browser, i.e. V8 engine, rather it is additional set of libraries, i.e. Node modules specific to a web _server_ application. Since it can be used to replace Django it provides the following features

- Generate dynamic page content
- Create, open, read, write, delete, and close files on the server
- Collect form data
- Create, Read, Update and Delete (CRUD) operation to a model/database

![](RackMultipart20200706-4-1esbxc3_html_c420919b53039da7.png)

**What is npm and what is it used for?**

Node Package Manager is an application used via command line to install, update and delete node modules which are nothing nut JavaScript libraries. It is cross platform and it can resolve dependencies based on the required modules.

**What is ES6?**

ES6 is a version of ECMAScript, which is a standard/specification (_not_ the actual language) followed by many programming languages such as ActionScript, JavaScript, Jscript. Any language complying with ES6 has to follow the standard, although it can have other features besides the ES6 specifications. ([https://stackoverflow.com/questions/912479/what-is-the-difference-between-javascript-and-ecmascript](https://stackoverflow.com/questions/912479/what-is-the-difference-between-javascript-and-ecmascript))

**List the names of 3 features that ES6 provides**

These are different from other languages such as python

1. Arrow functions
2. Promises
3. Destructuring

**What is ReactJS and what is it used for?**

It is JavaScript library for building user interfaces, developed and maintained by Facebook and open source community. React is suitable for developing single-page applications. The development involves creating components, which are the building blocks. There are further two types, functional and class-based components.

**List two popular alternative Javascript libraries to ReactJS.**

1. Angular
2. Vuejs

**What is the DOM?**

Document Object Model represents the web application that is loaded in the browser. It is a combination of static (HTML) as well as the dynamic (ES) part. It also provides a language-neutral interface that allows programs and scripts to dynamically access and update the content, structure, and style of a document, and thereby giving the ability to interact with the web application.DOM is a World Wide Web Consortium standard. It is basically a single object in a tree structure, which has nodes, it can be visualized in the developer&#39;s tool console.

**What is a virtual DOM?**

It is conceptual representation of the real DOM. The UI (which is the DOM) is kept in in sync with the virtual DOM with the help of ReactDOM library. In React, changes are first made in Virtual DOM and then they are synced with the actual DOM. ReactDOM constantly keeps diffing the real and virtual DOM. This makes React faster because: -

1. Only makes the selective changes in the real DOM,
2. The changes are done in batch.

**What is the difference between sessionStorage and localStorage?**

Within browser localStorage and sessionStorage, are two web storage API which provides the facility to store key value pairs. Both accomplish the same task of storing temporary data required for the application to be stored on the client side. However, data in sessionStorage is cleared as soon as the _browser tab is closed_, on the other hand, data in the localStorage is stored till it is _manually cleared from the browser&#39;s cache or cleared by the application itself_.

The APIs are similar for both the storages and only strings can be stored, however more complex datatype can be serialized and then casted to string via stringy method for further storage.

**What is a library like Material-UI used for?**

It is a library which provides components that implement material design. Material design is a coherent design system for creating User interfaces. The primary benefit is that using this library the application can look professional without the knowledge of designing concepts. Additionally, a large number of UI elements are available out of the box which can save a lot of time and still present a unified design experience for the end user.

Docker: -

**Why do we run apt-get update &amp;&amp; apt-get install -y in one command when using Docker?**

Since on starting the container, we cannot work interactively with the shell we need to run it in the same line with -y switch

**What are Docker containers and what are the pros and cons of using them**

Containers aim at running and deploying an application as independently as possible. Therefore, a container packages up code and all its dependencies in a single software unit, so the application runs quickly and reliably from one computing environment to another. A docker container image  is standalone, executable package of software that includes everything needed to run an application.

However, a docker container is a process which runs on a host. The host may be local or remote. When a user executes docker run, the container process that runs is isolated in that it has its own file system, its own networking, and its own isolated process tree separate from the host.

**What is the difference between ADD and COPY with Docker? –**

COPY is Same as &#39;ADD&#39;, but without the tar and remote URL handling.

**What is a .dockerignore file used for?** –

Docker can build images automatically by reading the instructions from a Docker file. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.Using this file, you can specify ignore rules and exceptions from these r_ules for files and folder, that_ _won&#39;t_ _be included in the build_ context and thus won&#39;t be packed into an archive and uploaded to the Docker server.

**What is Kubernetes and why didn&#39;t we use it?**

Kubernetes is used to manage docker containers in runtime, i.e. when a number of containers are running. Kubernetes can help in running additional or fewer containers as per the demand, it provides elasticity in terms of resources deployed. In this case, resource is a docker container, which is basically a unit for computing.

We did not used it _because_ our application is small and is not divided into various processes in order to be elastic. For example, we could have divided and containerized the registration functionality, and in case we expect a lot of users to be registered, we could have used Kubernetes to scale up additional containers that serve the registration feature. Also, from the cursory look it looks a bit complex to implement.

Deployment: -

What is Amazon S3 used for? –

Simple Storage Service, provides a storage place as well as a secure way to access it from within our application. It is sort of google drive, but for applications. It is primarily used for storing media files that may be used in a web application.

**What is Amazon ECS? –**

Elastic Container Service allows us to run and manage, docker containers via tasks. These containers run in a defined cluster, and can be scaled up and down, they are actually EC2 instances.ECS does not runs the container, it only provides the control plane to manage tasks. ECS is basically EC2+ container agent.

**What is the difference between ECS Fargate and EC2?**

Fargate works with ECS, but does not involves the management of the containers, i.e. no server management is required, hence it is also called serverless (AWS lambda is also closely related service), i.e. Amazon manages the underlying cluster. We only need to manage and configure the task and not the EC2 instances. If we need to scale the application without operational work for scaling it, it is better to use Fargate.

![](RackMultipart20200706-4-1esbxc3_html_1bf5ccb6018dde93.png)

**Name 3 other cloud providers. –**

1. Azure
2. Google Cloud Platform
3. Digital Ocean

**What is Sentry and what is it used for?**

It is a cloud hosted application that we can configure with our web applications, in order to monitor errors. It can be configured to send emails as soon as any error occurs, along with the detailed report of the error.

**What is Cloudflare and what is it used for?**

We used Cloudflare to protect and hide our application. By configuring the DNS in Cloudflare we let it handle the security aspects such as DDoS. It can also provide Content Delivery Network services, which helps in improving the performance of the application around the world.

**What is SendGrid and what is it used for?**

It is a cloud hosted application that we can use to send emails via the APIs it provides. It also has monitoring capabilities such as how many emails were reported spams i.e. reputation monitoring, email templates. Tracking the performance of the email (whither it was opened, interacted with etc)

**What is the difference between a DNS A record and a CNAME record?**

&#39; **A record&#39;**  maps a name to specific IP addresses, whereas &#39; **CNAME** record&#39; points a name to another name instead of to an IP

**A record**

[www.example.com](http://www.example.com/) A 123.321.11.21

**CNAME**

[www.example.com](http://www.example.com/) CNAME somename.github.io

**Meta**** : -**

**What are some of the mistakes or difficulties you encountered in developing these 2 assignments?**

1. There are many ways to do the same thing in React, which is confusing, and there is no natural flow of the execution in JavaScript, python is much more natural.
2. My Time estimation was way off, I planned for more but ended up making a subpar from the initial plan. This was partly because of the errors I ran into.
3. Some silly mistakes can drain hours and sometimes days, for example error related to &#39;CORS&#39; (many more are logged in the journal, but not all)

**What have you learned from this course that you think might be useful in your career?**

1. It feels like everything is important in this course. Considering that, most jobs are in web-based technologies, therefore this is the most important subject, and nothing out-dated was taught. Assignments were the key, and very well designed. I wish to do it once more, for the drill.