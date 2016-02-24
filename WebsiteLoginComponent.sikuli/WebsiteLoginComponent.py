from sikuli import*
import unittest
import json
import os

class WebsiteLoginComponent(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(2)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        if exists("UsernameMyAccount.png"):
            click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
            click("MyAccount_SignOut_Button.png")
        wait(3)
        
    def tearDown(self):

        if exists("UsernameMyAccount.png"):
            click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
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

        

    def test_1CreateAccount_BW21(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        click("Account_Register_Button.png")
        click(Pattern("RegisterPage_FirstName_TextBox.png").targetOffset(-133,12))
        wait(1)
        type("FirstName")
        click(Pattern("RegisterPage_LastName_TextBox.png").similar(0.86).targetOffset(-144,1))
        wait(1)
        type("LastName")
        click(Pattern("RegisterPage_Email_TextBox.png").similar(0.80))
        wait(1)
        type(config["username"])
        click(Pattern("RegisterPage_Password_TextBox.png").similar(0.93))
        wait(1)
        type(config["password"])
        click("RegisterPage_Register_Button.png")
        wait(4)
        
        if exists("UsernameMyAccount-1.png"):
            assert True
        else:
            assert False
   

    

   