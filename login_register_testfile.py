from services import userService
from validation import userValidation
# the reward now of using good OOP practices we don't have many lines in the main class

# Calling the service layer handling business logic, if made login method static would'nt need to make a userService Object
# Creating a userService Object to access methods of UserService
UserService =userService(userValidation)

# Calling the login method from UserService
userService.login()