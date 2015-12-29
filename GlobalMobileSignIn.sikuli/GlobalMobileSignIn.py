from sikuli import*
import unittest
import json



class GlobalMobileSignIn(unittest.TestCase):
    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["globalsignin"] + Key.ENTER)
        wait(2)

    def tearDown(self):       
        click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
        click("MyAccount_SignOut_Button.png")
        wait(3)
        click(Pattern("closeButtonChrome.png").targetOffset(26,0))

#    def test_invalidInputSignin(self):
#        click("globalMobileSigninPage_signin_Button.png")
#        if exists("globalMobileSigninPage_signin_Error.png"):
 #           assert True
##       else:
#            assert False
#   def test_invalidInputSignin(self):        
#        click("globalMobileSigninPage_registerNow_Button.png")
#        if exists("globalMobileSigninPage_register_error.png"):
#           assert True
#        else:
#            assert False

    def test_signin(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())#reads the jsonfile
        click(Pattern("globalMobileSigninPage_signInEmail_textbox.png").targetOffset(-59,16))
        type(config['username'])
        click(Pattern("globalMobileSigninPage_signinPassword_textBox.png").targetOffset(-21,42))
        type(config["password"])
        click("globalMobileSigninPage_signin_Button.png")   
        wait(2)
        click("globalMobileSigninPage_continue_Button.png")
        wait(4)
        if exists(Pattern("UsernameMyAccount.png").similar(0.86)):
            assert True
        else:
            assert False
                
    def test_register(self):
        timestr = time.strftime("%d%m%Y%H%M%S")#creates a unique username for testing
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        with open(configPath, "r") as config:
            data = json.load(config)
        tmp = data["username"]
        data["username"] = timestr + "@test.com"
        with open(configPath, "w") as config:
            config.write(json.dumps(data))
        config = json.loads(open(configPath).read())#reads the json file
        click("1447891969153.png")
        type("FirstName")
        click("1447892073664.png")
        type("LastName")
        click("1447892469068.png")
        type(config['username'])
        click(Pattern("1447892483156.png").targetOffset(-2,102))
        type(config['password'])
        click("1447892508827.png")
        wait(2)
        find("1447891263803.png")
        click("globalMobileSigninPage_continue_Button.png")
        wait(4)
        if exists(Pattern("UsernameMyAccount.png").similar(0.86)):
            assert True
        else:
            assert False
                

