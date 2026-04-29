
def check(func):
   def wrapper(page,username="",password=""):
    if page == "home":
      func(page)
    elif page == "about":
        func(page)
    elif page == "view_cart":
        if username == "admin" and password == "12345":
            func(page)
        else:
            print("Authentication failed....")      
   return wrapper 

@check
def home_page(pageName):
    print("Home Page")
    
@check
def about_page(pageName):
    print("This is about page")

@check
def view_cart_page(pageName,username="",password=""):
    print("This is view cart page")

#home_page("home")    
#about_page("about")
view_cart_page("view_cart","admin","1234567")