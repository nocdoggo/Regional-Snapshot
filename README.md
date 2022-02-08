## Regional ~~Community~~ Snapshot Project

In this project, we are aiming at designing a new community-based snapshot web-front to replace the existing [County Snapshot](https://iecam.illinois.edu/category/snapshots/) at IECAM. However, unlike the original project, we start with school district report, then expand to all possible geographical categories.

## Changelog

02-08-2022:

==Homevisiting==:

- Add home visiting page
- Improved the landing page design
- Square some errors

## FF. What Next

### FF.1 Change in Coding Engine

It is evident that there exist severe limitations of `Python` with `ArcGIS` frame support, and the constraints on performance issue. (The C-Panel has slow performance, and the Phison loader is rather shit to begin with.) In the near future, the project might migrate to a `Node.js` application with `Express.js` and potential `Ruby` backend processing support. In this way, it will widen the possible things that we could achieve with the existing hosting platform.

Please acknowledge such change in roadmap, and pardon us to make further evaluation before making huge version change.

The current working branch is `Homevisiting` branch, it will be converted to a milestone for this project.

### FF.2 Code Polishing

In the next couple weeks, please try to polish the program by squaring those ==TO-DO== sections.

## 0. Getting Started

Before getting started, make sure you have [Git](https://git-scm.com/) installed configured with your name and email address.

### 0.1 Cloning the Repository

There are 2 ways to clone the repository. One via `SSH`, and one via `HTTPS`. Either way is okay. However:

* If you choose `SSH` as method for synchronization, please visit the following link to have keys properly set up:

  ```javascript
  https://docs.gitlab.com/ee/ssh/
  ```

* If you choose `HTTPS`, you may even use [GitHub Desktop](https://desktop.github.com/) for the synchronization. For more information, please visit:

  ```javascript
  https://community.reclaimhosting.com/t/using-github-desktop-with-gitlab/876
  ```

After that, please switch to `sandbox` branch for the development work!

### 0.2 Python Environment

Even though the applet can be done in <kbd>R</kbd>. However, the code in this repository only works with <kbd>Python</kbd>, more specifically, `Python 3.5+`. You may download and install the environment either by directly installing all-in-one solution from [Anaconda](https://www.anaconda.com/products/individual), or simply install [Python](https://www.python.org/downloads/) (64-bit is recommended) and whichever editor you fancy.

==Please update your runtime environment with Python 3.6.11+.==

### 0.3 Required Libraries

Simply run:

```bash
pip install -r requirements.txt
```

Or, if there is `Python 2.7` exiting in your environment, run:

```bash
pip3 install -r requirements.txt
```

By doing so, all the required libraries will be downloaded and installed as `wheels`.

### 0.4 (OPTIONAL) Virtual Environment Configuration

Please leave your virtual environment compiler and library folder somewhere `outside of your cloned repository folder` in order not to interfere with other users' work environment.

### 0.5 (For Lazy Lad) GitHub Desktop

I know, it is almost 5 in the afternoon, you are about to rush out for the air of freedom. Wanna get it done in 2 minutes, if your internet is fast enough? Here is the solution! 

1. Download and install [GitHub Desktop](https://desktop.github.com/).

2. Make sure you also have a [GitHub account](https://github.com/), which is different from your GitLab account.

3. Clone a repository from `URL`, obtain the link by doing:

   ![GitLab Clone](doc/img/00_01.png)

4. Make sure you are in the `Sandbox` branch, then click on `Fetch origin`.

   ![Branch_Change](doc/img/00_02.PNG)

5. Oye, look! You are done!

## 1. Kickstart Your Applet

After all the dependencies are installed properly, please navigate into the directory of the repository, and we can run the applet simply by executing:

```bash
python app.py
```

Or

```bash
python3 app.py
```

Once executed properly, you shall see feedbacks as:

![Run the applet](doc/img/01_01.png)

Then, simply fire up your browser and visit the web address given in the terminal. In the case above, it is:

```bash
http://127.0.0.1:8050/
```

Note that, number after <kbd>:</kbd> refers to the port number opened for local hosting the website. If you can’t visit the site, please check the firewall settings based on your system. Sometimes, VPN may also cause issues.

## 2. Start To Write Some Bugs

Excited? I know. Please make sure to work in `sandbox` branch for now!

Wonder what to do after you see the task list, or figure out where you need to go in order to change the world? It is simple. You will see something like this:

![To-Do Block Sample](doc/img/02_01.png)

Let me walk you through on what they are!

### 2.1 To-Do Tags

In general, if anything is not added/finished, or requires further modification, you will see a <kbd># TO-DO:</kbd> tag somewhere in the scripts. For better book-keeping, `Visual Studio Code`, `PyCharm`, and `Atom`, have settings or plug-ins to highlight the tags. You shall see something like  ==# TO-DO:==. Underneath the tags, you shall see the functionality type of the code block, followed by the instructions on what it is, and what needs to be done.

### 2.2 Object Tags

Then you might wonder, what is under the `# TO-DO:`? Or maybe how you allocate the object blocks on the draft PDFs? Well, don’t you worry, it is not as hard as Morse Code. All you need to do is have <kbd>Ctrl</kbd> or <kbd>⌘</kbd> + <kbd>F</kbd> ready, and remember the following decoding steps.

==# Object ID== tags are generated in the format of:

```c++
# < Object Type > ID: < Object Type Short Code >-< Page ID >-< Index Number >
```

Quite complicated? No! It is intuitive.

#### 2.2.1 Object Type

Currently I categorized them into the following categories:

| Short Code | Type Name | Description                                                  |
| ---------- | --------- | ------------------------------------------------------------ |
| F          | Function  | Function which can be made into stand-alone module, or function block inside the render pipeline. |
| I          | Image     | The static images being used as logo or maps, which is different than the dynamically rendered plots based on the data. |
| T          | Text      | Text which in paragraphs or titles.                          |
| B          | Table     | Since T is being used, so we use B(lock) instead, they are generated based on the data lively. |
| G          | Graph     | The interactive graph plots which is dynamically rendered based on the data. |
| P          | Page      | The page ID, simply that.                                    |

In the future, if `ArcGIS` integration goes well, we might have `M` for `Map`. Fingers crossed.

#### 2.2.2 Page ID

In order to keep on track on what pages to be represented for the readers, a simple page ID is also added. At the very top of each <kbd>.py</kbd> file, you will see something like this:

![Page ID](doc/img/02_02.PNG)

## 3. How Things Works As A Whole

Then you might wonder, how exactly the pages are played out for the users? And how can I find which part of the app can be modified to fit my need? Wait no further.

### 3.1 Overall Diagram

First, let's take a look of a simple diagram.

![Diagram of the Flow](doc/img/03_01.png)

As we know that, the project is written in Python, so on the hosting server side, a python engine or docker environment is required to host the project. First, the users will be greeted with a `Map/Area Selection` page. Once a valid selection is given, the `App Engine` will be triggered, and corresponding datasets from `Prefetched Data` directory will be loaded for the `Overview` page, which can be considered as the cover page of the snapshot report. From there, users have the ability to choose which category of report he or she would like to read, or even export as PDF as a whole.

As for the pages based on the categories of data, the name in the light purple circle refers to the corresponding python source file name. So, if we are looking for the `Demographic` page, it will be <kbd>Demographic.py</kbd>.

### 3.2 Data Prefetch

You might wonder where the `Prefetched Data` is coming from? Why it is not directly from the database? Here are the reasons.

1. Data Stability

   Rather than fetching from the database using queries, the app only uses the prefetched data under the app directory. By prefetching the data from the database before the app being triggered, it gives us chances to inspect the data to maintain high data integrity. It lowers the chances for our app to crash unexpectedly. (Well, if the data causes the issue, the certain page won't load properly. However, if the database connection is somehow broken, then the app won't load at all. That also means, fail protection is needed, and therefore, more work is needed.)

2. Loading Speed

   Since the app might be hosted separately on other virtual machine rather than the existing DB server or web-hosting machine. This increases the latency on data transmission if we were to let our app connect to the DB server every time the app is triggered. Hence, the data is being prefetched.

After listening to my reasoning (for being lazy), you might wonder: then, how does the system cache the data and any rules have to be followed while caching? Wait no further.

#### 3.2.1 Cron Job



#### 3.2.2 Data Format

## 4. How Pages Are Rendered

Now, you have probably hosted this project somewhere, and presumably works. Wanna mess around with the blocks in the page, but don't know where and how they will show up on the canvas?



## 5. How Data Are Processed

But you also wonder, the contents shown on the web pages are not all prepared way in front of time, isn’t it? You are absolutely right!

## 9. Something Wrong With Data!

### 9.1 Race

**Problem:**

The total number doesn’t equal to the sum of the categories for FY2016 and FY2017. And for FY2015, there are missing stuff. This is for the `SD U46`. Also, it seems like the categories for ethnicity have 2 types missing for this particular fiscal year. 

**Solution:**

Well, first, let's simply not show the `Total Population`, since it does not add up or give meaningful information to the users. And as for the missing category for the ethnicity, we just leave ==0== in there. Why? Well, we are only attempting to show a range of 4 years' data. (Even so, the pages are overloaded. So, we could even reduce the number of years' data being included down to 3, or… 2? It can't be 5, right? Unless the users all use 21:9 phones or tablets, or print the reports on A3 paper instead.)

## 10. Ready For Publication?

Let’s say, at one point of time, you think we are cleared with all the ==# TO-DO:== tags?