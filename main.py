from taipy import Gui
from taipy.gui import Html
            
computer_nav = Html("""
    <div class="navbar">
        <div id="navicon"></div>
        <p id="navtitle">brokemenot</p>
        <div id="navlinks">
            <p id="dashboardnav" class="navlink">Dashboard</p>
            <img class="navlinkicon" src="./icons/dashboard.png" id="dashboardicon"></img>
            <p id="budgetingnav" class="navlink">Budgeting</p>
            <img class="navlinkicon" src="./icons/budgeting.png" id="budgetingicon"></img>
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
                <img class="tabnavlinkicon" src="./icons/budgeting.png" id="tabbudgetingicon"></img>
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

    """),
    'signup': Html("""

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
            </form>
        </div>
    """),
    'account': Html("""

    """)
}

Gui(pages=pages, css_file='./styles.css').run(dark_mode=True)

# first name, last name, street name, street number, password, confirm password, state, city, zip code, phone number, email
