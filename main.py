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

pages = {
    '/': computer_nav,
    'landing': Html("""

    """),
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

    """),
    'account': Html("""

    """)
}

Gui(pages=pages, css_file='./styles.css').run(dark_mode=False)
