# Imports
from signUpBackend import *
from signIn import check_password, authenticate_user
from signUpBackend import *
from taipy import Gui
from taipy.gui import Html

## MAKE THIS TRIGGER IN THE SIGN IN PAGE
# # Given Details
# first_name = "Esha"
# last_name = "VigneswaranSS"
# street_name = "Her Mom's House"
# street_number = "0"
# password = "bad"
# confirm_password = "bad"
# state = "NJ"
# city = "Dayton"
# zip_code = "08810"
# phone_number = "2313-456-7802"
# email = "eshaSSSSSSSSSSSs.vigneswaran@mit.edu"
# IDS = []

# # Create a new user and complete all necessary steps
# result = create_complete_new_user(last_name=last_name, first_name=first_name, street_name=street_name, 
#                                   street_number=street_number, state=state, city=city, zip_code=zip_code,
#                                   phone_number=phone_number, email=email, password=password, 
#                                   confirm_password=confirm_password)

# # get the customer id of the new user
# customer_id_example = CUSTOMER_ID



# # Example usage:
# result = create_accounts_for_customer123("64fd0b3e9683f20dd51880cc")
# print(result)



computer_nav = Html("""
    <div class="navbar">
        <div id="navicon"></div>
        <p id="navtitle">brokemenot</p>
        <div id="navlinks">
            <p id="dashboardnav" class="navlink">Dashboard</p>
            <img class="navlinkicon" src="./icons/dashboard.png" id="dashboardicon"></img>
            <p id="quiznav" class="navlink">Selector</p>
            <img class="navlinkicon" src="./icons/selector.png" id="selectoricon"></img>
            <p id="coursenav" class="navlink">Course</p>
            <img class="navlinkicon" src="./icons/course.png" id="courseicon"></img>
            <p id="blognav" class="navlink">Blog</p>
            <img class="navlinkicon" src="./icons/blog.png" id="blogicon"></img>
            <p id="accountnav" class="navlink">Account</p>
            <img class="navlinkicon" src="./icons/account.png" id="accounticon"></img>
        </div>
    </div>
""")
                    
tab_nav= Html("""
    <div class="navbar">
        <div id="tabnavheader">
            <div id="navicon"></div>
            <p id="navtitle">brokemenot</p>
        </div>
        <div id="tabnavlinks">
            <div class="navlinkiconbody" id="firstnavicon">
                <img class="tabnavlinkicon" src="./icons/dashboard.png" id="tabdashboardicon"></img>
            </div>
            <div class="navlinkiconbody">
                <img class="tabnavlinkicon" src="./icons/selector.png" id="tabselectoricon"></img>
            </div>
            <div class="navlinkiconbody">
                <img class="tabnavlinkicon" src="./icons/course.png" id="tabcourseicon"></img>
            </div>
            <div class="navlinkiconbody">
                <img class="tabnavlinkicon" src="./icons/blog.png" id="tabblogicon"></img>
            </div>
            <div class="navlinkiconbody">  
                <img class="tabnavlinkicon" src="./icons/account.png" id="tabaccounticon"></img>
            </div>
        </div>
    </div>
""")
              
computer_landing = Html("""
    <h1 id="landingheader">The All in One College Finance Personal Assistant</h1>
    <div id="accountlinks">      
        <p id="loginnav" class="navlink">Log In</p>
        <img class="navlinkicon" src="./icons/login.png" id="loginicon"></img>
        <p id="signupnav" class="navlink">Sign Up</p>
        <img class="navlinkicon" src="./icons/signup.png" id="signupicon"></img>
    </div>
    <div id="landingimage"></div>
""")
                        
tab_landing = Html("""
    <div style="position:relative; right: 20px;">
    <h1 id="tablandingheader">The All in One College Finance Personal Assistant</h1>
    <div id="tabaccountlinks">      
        <p id="loginnav" class="navlink">Log In</p>
        <img class="navlinkicon" src="./icons/login.png" id="loginicon"></img>
        <p id="signupnav" class="navlink">Sign Up</p>
        <img class="navlinkicon" src="./icons/signup.png" id="signupicon"></img>
    </div>
    <div id="tablandingimage"></div>
    </div>
""")

pages = {
    '/': computer_nav,
    'landing': computer_landing,
    'dashboard': Html("""
    
    """),
    'budgeting': Html("""

    """),
    'quiz': Html("""

    """),
    'course': Html("""

    """),
    'blog': Html("""
        <div id="bloglinks">
            <a class="bloglink" href="https://docs.google.com/document/d/18Zeyh6zOmSa6WwuFdGvN1dmjN_5Oj68iYXyRXn98RZ0/edit#heading=h.tgpfmijzask">Strategies for Managing Your Food Expenses While in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/12mKkWZqUA_mCkjdUQ8B6Nh6ce2Ej7iJgkgR9VCR-LEE/edit#heading=h.2tlm7cbcpb1l">A Comprehensive Guide to Transportation in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1Gxo02lb2NnpexArZ0t0NJ5_InoWlteb-yIqcTjg41Fo/edit#heading=h.ldk03fwuqxgc">Mastering the Art of Networking to Secure Your Dream Internship</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1S3PCqwP00-LCbzLsAEeU-jJEsAqRqjONzAhAJA2cs-M/edit#heading=h.oq30f560mkcw">Dorming in College: Your Ultimate Guide to Campus Living</a>
            <a class="bloglink" href="https://docs.google.com/document/d/18Zeyh6zOmSa6WwuFdGvN1dmjN_5Oj68iYXyRXn98RZ0/edit#heading=h.tgpfmijzask">Strategies for Managing Your Food Expenses While in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/12mKkWZqUA_mCkjdUQ8B6Nh6ce2Ej7iJgkgR9VCR-LEE/edit#heading=h.2tlm7cbcpb1l">A Comprehensive Guide to Transportation in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1Gxo02lb2NnpexArZ0t0NJ5_InoWlteb-yIqcTjg41Fo/edit#heading=h.ldk03fwuqxgc">Mastering the Art of Networking to Secure Your Dream Internship</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1S3PCqwP00-LCbzLsAEeU-jJEsAqRqjONzAhAJA2cs-M/edit#heading=h.oq30f560mkcw">Dorming in College: Your Ultimate Guide to Campus Living</a>
            <a class="bloglink" href="https://docs.google.com/document/d/18Zeyh6zOmSa6WwuFdGvN1dmjN_5Oj68iYXyRXn98RZ0/edit#heading=h.tgpfmijzask">Strategies for Managing Your Food Expenses While in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/12mKkWZqUA_mCkjdUQ8B6Nh6ce2Ej7iJgkgR9VCR-LEE/edit#heading=h.2tlm7cbcpb1l">A Comprehensive Guide to Transportation in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1Gxo02lb2NnpexArZ0t0NJ5_InoWlteb-yIqcTjg41Fo/edit#heading=h.ldk03fwuqxgc">Mastering the Art of Networking to Secure Your Dream Internship</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1S3PCqwP00-LCbzLsAEeU-jJEsAqRqjONzAhAJA2cs-M/edit#heading=h.oq30f560mkcw">Dorming in College: Your Ultimate Guide to Campus Living</a>
            <a class="bloglink" href="https://docs.google.com/document/d/18Zeyh6zOmSa6WwuFdGvN1dmjN_5Oj68iYXyRXn98RZ0/edit#heading=h.tgpfmijzask">Strategies for Managing Your Food Expenses While in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/12mKkWZqUA_mCkjdUQ8B6Nh6ce2Ej7iJgkgR9VCR-LEE/edit#heading=h.2tlm7cbcpb1l">A Comprehensive Guide to Transportation in College</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1Gxo02lb2NnpexArZ0t0NJ5_InoWlteb-yIqcTjg41Fo/edit#heading=h.ldk03fwuqxgc">Mastering the Art of Networking to Secure Your Dream Internship</a>
            <a class="bloglink" href="https://docs.google.com/document/d/1S3PCqwP00-LCbzLsAEeU-jJEsAqRqjONzAhAJA2cs-M/edit#heading=h.oq30f560mkcw">Dorming in College: Your Ultimate Guide to Campus Living</a>
        </div>
    """),
    'signup': Html("""
        <div id="signupbody">
            <h2 id="logintitle">Sign Up</h2>
            <form action="/action_page.php" style="margin-top: 15px">
                <img class="loginicon" src="./icons/account.png"></img>
                <input class="logininput" type="text" name="firstname" placeholder="First Name"></input><br></br><br></br>
                <img class="loginicon" src="./icons/account.png"></img>
                <input class="logininput" type="text" name="lastname" placeholder="Last Name"></input><br></br><br></br>
                <img class="loginicon" src="./icons/location.png"></img>
                <input class="logininput" type="text" name="streetname" placeholder="Street Name"></input><br></br><br></br>
                <img class="loginicon" src="./icons/location.png"></img>
                <input class="logininput" type="number" name="streetnumber" placeholder="Street Number"></input><br></br><br></br>
                <img class="loginicon" src="./icons/location.png"></img>
                <input class="logininput" type="text" name="city" placeholder="City"></input><br></br><br></br>
                <img class="loginicon" src="./icons/location.png"></img>
                <input class="logininput" type="text" name="state" placeholder="State"></input><br></br><br></br>
                <img class="loginicon" src="./icons/location.png"></img>
                <input class="logininput" type="number" name="zipcode" placeholder="Zip Code"></input><br></br><br></br>
                <img class="loginicon" src="./icons/email.png"></img>
                <input class="logininput" type="text" name="email" placeholder="Email"></input><br></br><br></br>
                <img class="loginicon" src="./icons/password.png"></img>
                <input class="logininput" type="password" name="password" placeholder="Password"></input><br></br><br></br>
                <img class="loginicon" src="./icons/password.png"></img>
                <input class="logininput" type="password" name="password" placeholder="Confirm Password"></input><br></br><br></br>
                <img class="loginicon" src="./icons/phone.png"></img>
                <input class="logininput" type="number" name="phonenumber" placeholder="Phone Number"></input><br></br><br></br>
                <p id="loginsubmit">Get OTP</p>
                <img class="loginicon" src="./icons/password.png"></img>
                <input class="logininput" type="text" name="otp" placeholder="OTP"></input><br></br><br></br>
                <input id="loginsubmit" type="submit" value="Submit"></input>
            </form>
        </div>
        <div style="height: 200px;"></div>
    """),
    'login': Html("""
        <div id="loginbody">
            <h2 id="logintitle">Log In</h2>
            <form action="/action_page.php" style="margin-top: 15px">
                <img class="loginicon" src="./icons/email.png"></img>
                <input class="logininput" type="text" name="email" placeholder="Email"></input><br></br><br></br>
                <img class="loginicon" src="./icons/password.png"></img>
                <input class="logininput" type="password" name="password" placeholder="Password"></input><br></br><br></br>
                <input id="loginsubmit" type="submit" value="Submit"></input>
                <p id="loginsubmit">Sign Up</p>
            </form>
        </div>
        <div style="height: 200px;"></div>
    """),
    'account': Html("""

    """)
}

Gui(pages=pages, css_file='./styles.css').run(dark_mode=True)