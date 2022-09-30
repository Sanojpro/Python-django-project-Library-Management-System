# Python-django-project-Library-Management-System

SANOJ KUMAR PRADHAN

OBJECTIVE-

The purpose is to create a Library management system, wherein a Admin can maintain the library online by performing various operations.
Such as:- 1. Add a book to the book list
          2. Update an entry of a book
          3. Delete a book
          4. View all the books (Students can access this feature only)
          
  
ABOUT THE PROJECT-

1. MODEL-
    
    a. User Model(In-built)-
          i. Columns used = "name" , "email" , "password"
          ii. Unique attribute= "email"
          
    b. Book Model(Registered in admin.py)-
          i. Columns created = "BID" , "BNAME" , "AUTHOR" , "PUBLISHER"
          ii. Primary_key = "BID"
          
 2. VIEW-
      
      Templates used-
      
      i. addbook.html
        
        This page when rendered, shows "Add a book" page to the admin, where admin can add a book to the list.
      
      ii. admview.html
      
        This page when rendered, shows "Admin view" page to the admin, where admin has the power to make changes to the book list.
      
      iii. home.html
      
        This page when rendered, shows "Home" page to the admin also acts as base for login.html.
      
      iv. signup.html
      
        This page when rendered, shows "Admin Signup" page to the admin, where a new admin can signup using a different email.
      
      v. login.html
      
        This page when rendered, shows "Admin signin page" page to the admin, where a admin can login using their credentials.
      
      vi. stuview.html
      
        This page when rendered, shows "Student view" page to the user, where they can see all the books present in the database.
      
      vii. update.html
        
        This page when rendered, shows "Update and save" page to the admin, where a admin can update the book details and save it to the database.
        
        
  3. CONTROL-
  
          i. Functions are created in views.py of the app directory to perform operations when called upon.
          ii. urlpatterns are created in urls.py of the app directory to route the URLs to appropriate view functions.
      
  4. REST API used-
  
          a.Http requests used-
                    i.GET
                    ii.POST
      
          b.Http verbs used-
                    i. "/"- This API endpoint sends a http request to the server and gets the home extended login page(DEFAULT PAGE)
                    ii. "/home" -This API endpoint sends a http request to the server and gets the home extended login page.
                    iii. "/login" - This API endpoint sends a http request to the server and gets the home extended login page, takes data from the user and logs him in.
                    iv. "/signup" - This API endpoint sends a http request to the server and gets the signup page, takes data from the admin and creates a new account.
                    v. "/stuview" - This API endpoint sends a http request to the server and gets the student view page along with the data from the database.
                    vi. "/admview" - This API endpoint sends a http request to the server and gets the Admin control page along with the data from the database.
                    vii. "/updatebutton" - This API endpoint sends a http request to the server,helps in assigning keys- to the instance "book" of the object Book.The instance is created using the primary key, which was fetched by splitting the URI.
                    viii. "/updatebook" - This API endpoint sends a http request to the server, takes input from the admin and updates the book instance based on the data fetched on another request.
                    ix. "/deletebook"- This API endpoint sends a http request to the server, takes the primary key after splitting the URI and helps in deleting the instance.
                    x. "/addbook" - This API endpoint sends a http request to the server, takes value from the admin and adds the data into the database on another request.
                    xi. "/addbutton" - This API endpoint sends a http request to the server and gets the Add a book page.
                    xii. "/logout" - This API endpoint sends a http request to the server and logs admin out.
         
         
   5. How to start the server-
   
      Open the file in an IDE> Open Terminal > Change directory to the project directory(i.e lib) > Type "python manage.py createsupersuser" >fill in credentials > when successful > Type "python manage.py runserver" > Click on the generated server link > Explore the amazing website.
  
   
  
