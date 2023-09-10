from taipy import Gui
from taipy.gui import Html

text="hi"
            
computer_nav = Html("""
    <div class="navbar">
        <img id="navicon" src="./icons/logo.png" style="object-fit: contain; background-color: transparent; position: relative; top: 10px;"></img>
        <p id="navtitle">brokemenot</p>
        <div id="navlinks">
            <p id="dashboardnav" class="navlink">
                <a id="dashboardnav" class="navlink" href="/dashboard" style="position: fixed; top: 10px; left: 10px;">Dashboard</a>
            </p>
            <img class="navlinkicon" src="./icons/dashboard.png" id="dashboardicon"></img>
            <p id="quiznav" class="navlink">
                <a id="dashboardnav" class="navlink" href="/quiz" style="position: fixed; top: 10px; left: 10px;">Selector</a>        
            </p>
            <img class="navlinkicon" src="./icons/selector.png" id="selectoricon"></img>
            <p id="coursenav" class="navlink">
                <a id="dashboardnav" class="navlink" href="/course" style="position: fixed; top: 10px; left: 10px;">Course</a>        
            </p>
            <img class="navlinkicon" src="./icons/course.png" id="courseicon"></img>
            <p id="blognav" class="navlink">
                <a id="dashboardnav" class="navlink" href="/blog" style="position: fixed; top: 10px; left: 10px;">Blog</a>        
            </p>
            <img class="navlinkicon" src="./icons/blog.png" id="blogicon"></img>
            <p id="accountnav" class="navlink">
                <a id="dashboardnav" class="navlink" href="/account" style="position: fixed; top: 10px; left: 10px;">Account</a>        
            </p>
            <img class="navlinkicon" src="./icons/account.png" id="accounticon"></img>
        </div>
    </div>
""")
                    
tab_nav = Html("""
    <div class="navbar">
        <div id="tabnavheader">
            <img id="navicon" src="./icons/account.png" style="object-fit: contain; background-color: transparent;"></img>
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
        <p id="loginnav" class="navlink">
            <a id="dashboardnav" class="navlink" href="/login" style="position: fixed; top: 10px; left: 10px;">Log In</a>                
        </p>
        <img class="navlinkicon" src="./icons/login.png" id="loginicon"></img>
        <p id="signupnav" class="navlink">
            <a id="dashboardnav" class="navlink" href="/signup" style="position: fixed; top: 10px; left: 10px;">Sign Up</a>
        </p>
        <img class="navlinkicon" src="./icons/signup.png" id="signupicon"></img>
    </div>
    <img id="landingimage" src="./icons/landing.jpg" style="object-fit: contain; background-color: transparent;"></img>
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
    <img id="tablandingimage" src="./icons/landing.jpg" style="object-fit: contain; background-color: transparent;"></img>
    </div>
""")

pages = {
    '/': computer_nav,
    'landing': computer_landing,
    'dashboard': Html("""
        <h1 id="dashboardtitle">Welcome, Tejas!</h1>
        <h2 id="dashboardprogresstitle">Progress: $41,972/$59,342</h2>
        <div class="progressbar">
            <div class="progress" id="p1"></div>
        </div>
        <h2 id="dashboardprogresstitle">Rent Budgeting: $1,925/$1,925</h2>
        <div class="progressbar">
            <div class="progress" id="p2"></div>
        </div>
        <h2 id="dashboardprogresstitle">Food Budgeting: $1,472/$1,000</h2>
        <div class="progressbar">
            <div class="progress" id="p3"></div>
        </div>
        <h2 id="dashboardprogresstitle">Miscellaneous Expenses: $503/$1,000</h2>
        <div class="progressbar">
            <div class="progress" id="p4"></div>
        </div>
        <h2 id="dashboardprogresstitle">Loan Payment Goal: $1,750/$2,000</h2>
        <div class="progressbar">
            <div class="progress" id="p5"></div>
        </div>
        <div id="loginbody" style="margin-top: 50px; height: 700px">
            <h2 id="logintitle" style="margin-top: 25px;">Modify Budgeting</h2>
            <form style="margin-top: 15px">
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="email" placeholder="Total Loan"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Rent Budget"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Rent Paid"></input><br></br><br></br>
                
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Food Budget"></input><br></br><br></br>
                    
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Food Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Miscellaneous Budget"></input><br></br><br></br>
                
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Miscellaneous Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Monthly Goal"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Monthly Paid"></input><br></br><br></br>
                      
                <p id="loginsubmit">
                    <a id="dashboardnav" class="navlink" href="/dashboard" style="position: fixed; top: 10px; left: 10px;">Submit</a>  
                </p>
                
            </form>
        </div>
        <div style="height: 50;"></div>
    """),
    'dasnboard': Html("""
        <h1 id="dashboardtitle">Welcome, Tejas!</h1>
        <h2 id="dashboardprogresstitle">Progress: N/A</h2>
        <div class="progressbar">
        </div>
        <h2 id="dashboardprogresstitle">Rent Budgeting: N/A</h2>
        <div class="progressbar">
        </div>
        <h2 id="dashboardprogresstitle">Food Budgeting: N/A</h2>
        <div class="progressbar">
        </div>
        <h2 id="dashboardprogresstitle">Miscellaneous Expenses: N/A</h2>
        <div class="progressbar">
        </div>
        <h2 id="dashboardprogresstitle">Loan Payment Goal: N/A</h2>
        <div class="progressbar">
        </div>
        <div id="loginbody" style="margin-top: 50px; height: 700px">
            <h2 id="logintitle" style="margin-top: 25px;">Modify Budgeting</h2>
            <form style="margin-top: 15px">
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="email" placeholder="Total Loan"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Rent Budget"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Rent Paid"></input><br></br><br></br>
                
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Food Budget"></input><br></br><br></br>
                    
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Food Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Miscellaneous Budget"></input><br></br><br></br>
                
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Miscellaneous Paid"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Monthly Goal"></input><br></br><br></br>
                      
                <img class="loginicon" src="./icons/dollar.png"></img>
                <input class="logininput" type="text" name="a" placeholder="Loan Monthly Paid"></input><br></br><br></br>
                      
                <p id="loginsubmit">
                    <a id="dashboardnav" class="navlink" href="/dashboard" style="position: fixed; top: 10px; left: 10px;">Submit</a>  
                </p>
                
            </form>
        </div>
        <div style="height: 50;"></div>
    """),
    'quiz': Html("""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSebj0xhzHsSjnTNL6PxUNreE5NwXmM4_jWbaiXKO-5mrOmCww/viewform?embedded=true" width="640" height="2388" frameborder="0" marginheight="0" marginwidth="0" style = "margin-left: 23vw; margin-top: 150px;">Loading…</iframe>
    """),
    'course': Html("""
        <h2 style = "margin-left: 25vw; margin-top: 150px;">Lesson 1: Funding Strategies</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vTFlNEuloGoT21ey_h0M5TriNYtXjrf_HMp1HUqeXILm-BcxLY7WU1QjKlOQM2WUeNrxjYkDi9pkOrv/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 2: Irregular Family Situation</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vT5PGN062vpaQbHiNu18FNH3Vy9q4kYAKXWjzwNtV7lsgalgTlr42HTHheKlqqdOjwz_ypQvWYPCGIs/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 3: Need Based Aid</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vR5hygFdcwjsX0Y4i2deezgC4Lp-2JPWF5TISvk_73Wn5QuDqReIRo1-R-jyw4X01IYu4dl2DJwJIS-/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 4: In-State vs Out-of-State</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vS67PmNWjK-84zRSlcAgvGofNaoiK3gQyVxVN2eYizfpH2heP5UUHhwDI57DMEI_Qm6KEuNwN8VR2vi/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 5: Considerations</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vR28NF5swtyPZqEqJ_96z9dI5B3aL7UvzpkssDs3ILXZtwjS6IHRdEco69tjetI52UHJB9wVLxzSwH6/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 6: Considerations for Parents</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vTcc1nErKBhTulPM-ZkGRaUiqgdIcTGTsmVx3PxpfyAlK20tTWvOraje50Z1kbuGwR1uqR6eN11YNwj/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; mmargin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 7: Paying for College</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vQs5ql01ze7ZkKLrVA3OYzLuxMgjxmgPdOOzX9pbeaAfYYRY9L6CA4khTDgIeNY_nCObsNKCzFnru3v/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>
        
        <h2 style = "margin-left: 25vw;">Lesson 8: Finnancial Aid as an Immigrant</h2>          
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vQOSs6A-kUWQhhgA-Xok-4UpotVr0xtHv5PXlsTI85g8Z_3o2iCJLDNpdgs6SwZRV2WudeunKxtd1x_/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 9: FAFSA Setup</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vQPrYwzOSQTtMinZnCx3OeWPA3Klr_OLwRc9UZrJgG55EA1DGswKvql4z-AV3hESOT4LhbLCDpWjl9d/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 10: FAFSA and CSS Profile</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vRvz-XeE2mFzbKWtIS9nGUKhLpV4lv5GsK8L7ymFN-xEoCe5Xm54PRo_QjmnFh9BnzHoGFSCwW6IK60/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>
        

        <h2 style = "margin-left: 25vw;">Lesson 11: Athletic Scholorships</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vQQFV5wUigZ_8x9zSOXx2uWIKfsviMCMWgcglXZzL9WJWaUZPZi_82XNcr5cmU-r0zzZIfp9Y287Yzg/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 12: Grants and Scholorships</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vRGZa_85uW-9RDvkawjXUoV6BE5qNWgpn0J_KP2JasCxpefXaYjF2V--5rzNv-mbTh4SCBmwIoeYqpT/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 13: Searching for Scholorships</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vS969XJI9AGI1FkNa6zxRzeqQb_d0mOIDdIkQPN5dkOl_6mWBVGbz_Z9lbcUKM7aIbK23-MfEvG02PI/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 14: Applying for Scholarships Part 1</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vTZobbU0bPFcXXG7ox3x7gbb_7bzNjU55x-znWCQY90T55ecUrNsZ4F3okKDKPkLHVB68rQWyfzK8jw/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 15: Applying for Scholarships Part 2</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vTZ7F1aYi_2aCHwBBDuXasWnw2g97sJlN49GIKP4z6U3fe9pq1CgCWE2zkZmZqnyUU0PHpN4Pl2KhmA/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>

        <h2 style = "margin-left: 25vw;">Lesson 16: Applying for Scholarships Part 3</h2>
        <iframe src="https://docs.google.com/document/d/e/2PACX-1vSVWPZ7RChdq8o0JTEV42jZ4O_0QpklkdFGgI2RDUzWF0VJPWbRbo-j_-0IAjwWKcoC4Vyh3sP740g2/pub?embedded=true" style="height: 400px; width: 50vw; margin-left: 25vw; margin-bottom: 100px;"></iframe>
    """),
    'blog': Html("""
        <div id="bloglinks">
            <h1 style="text-align: center">Blog Articles</h1>
            <a class="bloglink" href="https://docs.google.com/document/d/18Zeyh6zOmSa6WwuFdGvN1dmjN_5Oj68iYXyRXn98RZ0/edit#heading=h.tgpfmijzask" style="margin-top: 20px;">Strategies for Managing Your Food Expenses While in College</a>
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
                <p id="loginsubmit">
                    <a id="dashboardnav" class="navlink" href="/dasnboard" style="position: fixed; top: 10px; left: 10px;">Submit</a>  
                </p>
            </form>
        </div>
        <div style="height: 200px;"></div>
    """),
    'login': Html("""
        <div id="loginbody">
            <h2 id="logintitle">Log In</h2>
            <form style="margin-top: 15px">
                <img class="loginicon" src="./icons/email.png"></img>
                <input class="logininput" type="text" name="email" placeholder="Email"></input><br></br><br></br>
                <img class="loginicon" src="./icons/password.png"></img>
                <input class="logininput" type="password" name="password" placeholder="Password"></input><br></br><br></br>
                <p id="loginsubmit">
                    <a id="dashboardnav" class="navlink" href="/dashboard" style="position: fixed; top: 10px; left: 10px;">Submit</a>  
                </p>
                <p id="loginsubmit">
                    <a id="dashboardnav" class="navlink" href="/signup" style="position: fixed; top: 10px; left: 10px;">Sign Up</a>  
                </p>
            </form>
        </div>
        <div style="height: 200px;"></div>
    """),
    'account': Html("""
        <div id="accountbody">
            <h2 id="logintitle" style="margin-top: 50px">Account Information</h2>
            <form action="/action_page.php" style="margin-top: 15px">

                <img class="loginicon" src="./icons/account.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   Tejas</p><br></br><br></br>

                <img class="loginicon" src="./icons/account.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   Raghuram</p><br></br><br></br>

                <img class="loginicon" src="./icons/location.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   Foxhill Run</p><br></br><br></br>

                <img class="loginicon" src="./icons/location.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   16</p><br></br><br></br>

                <img class="loginicon" src="./icons/location.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   Monmouth Junction</p><br></br><br></br>

                <img class="loginicon" src="./icons/location.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   New Jersey</p><br></br><br></br>

                <img class="loginicon" src="./icons/location.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   08852</p><br></br><br></br>

                <img class="loginicon" src="./icons/email.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   tejas.raghuram101@gmail.com</p><br></br><br></br>


                <img class="loginicon" src="./icons/phone.png"></img>
                <p style="font-size: 16px; display: inline; padding: 10px;">   +17328237778</p><br></br><br></br>


            </form>
        </div>
        <div style="height: 200px;"></div>
    """)
}

def login_action(state):
    print(state.email)
    print(state.password)

Gui(pages=pages, css_file='./styles.css').run(dark_mode=True)
