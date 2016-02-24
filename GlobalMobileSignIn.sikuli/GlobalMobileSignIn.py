from sikuli import*
import unittest
import json
import os


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
        if exists(Pattern("globalMobileSigninPage_continue_Button.png").exact()):
            click("globalMobileSigninPage_continue_Button.png")
            wait(2)
            click(Pattern("MainPage_MyAccount_dropdown-1.png").exact())
            click("MyAccount_SignOut_Button.png")
            wait(3)
            type("l", KeyModifier.CTRL)
            type(config["globalsignin"] + Key.ENTER)

    def tearDown(self):
        if exists(Pattern("MainPage_MyAccount_dropdown-1.png").exact()):
            click(Pattern("MainPage_MyAccount_dropdown-1.png").exact())
            click("MyAccount_SignOut_Button.png")
            wait(3)
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)
        else:
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)

    def test_invalidInputSignin_BW188(self):
        click("globalMobileSigninPage_signin_Button.png")
        if exists("globalMobileSigninPage_signin_Error.png"):
           assert True
        else:
            assert False
    def test_invalidInputRegisterNow_BW188(self):
        click("GlobalMobileSignin_CreateAccount_Button.png")
        click("globalMobileSigninPage_registerNow_Button.png")
        if exists("globalMobileSigninPage_register_error.png"):Click o
           assert True
        else:
            assert False

    def test_invalidInputEmail_BW188(self):
        click(Pattern("1456277744919.png").targetOffset(-63,19))
        type(Key.ENTER)
        if exists("1456277796102.png"):
            assert True
        else:
            assert False


    def test_signin_BW184(self):
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
                
    def test_register_BW185(self):
        timestr = time.strftime("%d%m%Y%H%M%S")#creates a unique username for testing
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        with open(configPath, "r") as config:
            data = json.load(config)
        tmp = data["username"]
        data["username"] = timestr + "@test.com"
        with open(configPath, "w") as config:
            config.write(json.dumps(data))
        config = json.loads(open(configPath).read())#reads the json file
        click("GlobalMobileSignin_CreateAccount_Button.png")
        click(Pattern("GlobalMobileSigninCreateAccount_FirstName_Textbox.png").exact())
        type("FirstName")
        click(Pattern("GlobalMobileSigninCreateAccount_SurName_Textbox.png").exact())
        type("LastName")
        click(Pattern("GlobalMobileSigninCreateAccount_EmailAddress_Textbox.png").exact().targetOffset(-3,-2))
        type(config['username'])
        click(Pattern("GlobalMobileSigninCreateAccount_Password_Textbox.png").exact().targetOffset(-3,1))
        type(config['password'])
        click("globalMobileSigninPage_registerNow_Button.png")
        wait(2)
        find("globalMobileSigninPage_ThankYou_Page.png")
        click("globalMobileSigninPage_continue_Button.png")
        wait(4)
        if exists(Pattern("UsernameMyAccount.png").similar(0.86)):
            assert True
        else:
            assert False

    def test_googleLogin_BW186(self):
        click(Pattern("globalMobileSignIn_Google+_button.png").exact())
        wait(4)
        click(Pattern("GlobalMobileSignIn_Allow_GoogleButton.png").similar(0.97))
        wait(4)
        click("globalMobileSigninPage_continue_Button.png")
        if exists(Pattern("MainPage_MyAccount_dropdown-2.png").exact()):
            assert True
        else:
            assert False

    def test_haveAnAccountLink_BW187(self):
        click("GlobalMobileSignin_CreateAccount_Button.png")
        click(Pattern("GlobalMobileSignin_HaveAnAccount_Button.png").exact())
        if exists(Pattern("GlobamMobileSignin_SignInPage.png").exact()):
            assert True
        else:
            assert False
                
    #def test_resetPassword(self:
    #(on its way)
