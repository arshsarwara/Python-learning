# Create class user
# standard convention is we write filename with small letter; class starts with capital letter
#class is like an object contructor;
# all class have a __init__() function
# __init__() is executed automatically, whenever we create the objects from this class
#functions that belongs to an class are called Methods
class User:
    def __init__(self, user_email, name, password, current_job_title):  #this init function is also sometimes called constructor; sle si reference to current instance of class; is used to access variables that belong to class
        self.email = user_email #name doesn't have to be same as above in def, that is just for parameters
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. you can contact them at {self.email}")

# crete a new user object from class above
app_user_one = User("as@as.com", "Arsh Singh", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

#change job title using function
app_user_one.change_job_title("DevOps Trainer")
app_user_one.get_user_info()
