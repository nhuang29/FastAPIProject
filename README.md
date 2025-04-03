# FastAPIProject

## Instructions On How to Run the Project

### Step 1: Cloning and Locating the Project
After cloning and getting the project onto your local machine. First cd into the main directory 
of ./FastAPIProject

### Step 2: Downloading Requirements
Once at the top directory. There will be a "requirements.txt" file in that directory. 
Please type in this command:
```commandLine
pip install -r requirements.txt
```

### Step 3: Running the Application
After all necessary packages have been installed, please type in this command to run the application:
```commandline
uvicorn main:app --reload
```

### Step 4: Registering a Few Users
Please open another terminal and go to the /FastAPIProject/client directory. There, you will 
see a tester.py file. Please run the command:
```commandline
python tester.py
```
This will populate the database with users with a default "pending" state. 
Feel free to change the properties to add as many users as you like. 

**Important:** To prevent people from using similar emails and resume, the email and resume must be 
unique. Otherwise, the user will not register.

### Step 5: Testing Out the UI
Please go to URL:
```
http://127.0.0.1:8000/
```
This will bring you to the login page. The username/password is **admin**/**admin**.
Once logged in, you can click the "Get All Leads" button, and you will receive a list of all 
registered leads. 

If you would like to change the status of one user to "reached out". Please enter the first name, last
name, and email of the user you want to change. Then press the "Confirm Lead has been reached out" button.

### Step 6: Uninstalling Everything 
Please run:
```commandline
pip uninstall -r requirements.txt
```
This will clear your computer of any packages needed to run this project. 

## Design Choices (And What I Would've Done Differently)

**1. SQLite: I decided to use this database because it works seamlessly with SQL Alchemy.**

Improvements:
* Use a relational database with stronger concurrency capabilities (Postgres, MySQL)
* Use third party db such as Supabase. This would've decoupled the database from the actual server.
Even though the database will persist since it's written in a file. If the machine goes down then it 
would be hard to access that file.
* Blob Storage to store resume. One big flaw is that the system takes in the resume/CV as a string. A
blob storage such as S3 or even a file store in the project itself would've been better.

**2. Separation of services: As shown, the main.py file holds EVERYTHING (from database creation to 
model creation to route creation to database R/W)**

Improvements:
* I would've put those functionalities into separate folders (i.e. config, models, etc.). This would've 
made my code look a lot cleaner. My code was just too cluttered.


**3. Security of login: If someone logs into the admin dashboard and the presses the "logout" button, 
they don't need to log in again. They can simply press the back button and go back to the admin 
dashboard. Also, the admin/password are hard coded into the application.** 

Improvements:
* I would've put in place session tracking and cookies to make sure that when someone logs out, then 
can't simply log back in by pressing the back button

**4. Ease of use: The application requires a user to input first name, last name, and email to check off
that lead.**

Improvements:
* I would've either had a checkbox or just require the admin to input the email since it's unique

**5. Doesn't Send Emails: Due to time constraints, when a lead registers, it doesn't send any 
confirmation email to either the admin or user.** 

**6. Hardening the back-end: Using technologies like UWSGI and NGINX would've been helpful in ensuring 
the health of the backend (load balancing and reverse-proxying). UWSGI provides "workers" which can spawn multiple instances of 
the application on the same machine. I didn't incorporate any caching as well as I would've done that through 
UWSGI as well as NGINX for a hybrid architecture.** 

**7. Quicker Testing: I had the initial plan of wrapping the application in a docker container to make it 
easier to run for testers, but I ran out of time.**

**8. Unit Testing: I had no definitive unit tests, and everything I did was behavior driven.**

**9. Auto updating on the list for the UI: This would auto update when a lead is "reached out" to.** 
