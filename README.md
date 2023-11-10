# Drone-Company-Management-System
The Drone Company Management System is a comprehensive solution designed to streamline and enhance the operations of a drone services company. This system provides a centralized platform for managing various aspects of the company, including project management, fleet monitoring, client interactions, and employee administration.


---
## screenshots
### Homepage

          
---
## Functions
###Admin

    - Admin account creation is achieved using the createsuperuser command.
    - After login, the admin can manage customer accounts (view/update/delete).
   -  Can manage policy categories such as Life, Health, Motor, and Travel.
    - Has control over policies (add/update/delete).
    - Can view total policy holders, approved policy holders, and disapproved policy holders.
    - Approval of policies applied by customers is under the admin's jurisdiction.
    - Admin can respond to customer inquiries.

### Customer


    Customers can create an account without admin approval.
    After login, customers can view all policies added by the admin.
    If interested, customers can apply for a policy, which goes into pending status until approved by the admin.
    Customers can check the status of their policies under the history section.
    Customers have the option to ask questions from the admin.

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)
- Open Terminal and Execute Following Commands :
```
python -m pip install -r requirements.txt
```
- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to gmail through host email id in your browser and open following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```


## Disclaimer
This project is developed for demo purpose and it's not supposed to be used in real application.

## Feedback
Any suggestion and feedback is welcome. You can message me on facebook

