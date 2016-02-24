from sikuli import*
import unittest
import json
import os


class SavedProperties(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(2)
        if exists("UsernameMyAccount-4.png"):
            click(Pattern("UsernameMyAccount-4.png").targetOffset(104,3))
            click("MyAccount_SignOut_Button.png")
            click("SigninPage_SignIn_Button.png")
            click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
            type(config["username"])
            type(Key.TAB)
            type(config["password"])
            click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.92))
            wait(3)

        else:
                
            click("SigninPage_SignIn_Button.png")
            click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
            type(config["username"])
            type(Key.TAB)
            type(config["password"])
            click(Pattern("SignInPopUp_SignIn_Button.png").similar(0.92))
            wait(3)

    def tearDown(self):
        type(Key.BACKSPACE)
        click("SavedPropertiesPage_Remove_Button.png")
        type(Key.F5)
        wait(1)
        click(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click("MyAccountDropdown_SignOut_Button.png")
        wait(3)
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        appTaskName = config["appTaskName"]
        os.system("taskkill /f /im " +appTaskName)

        
    def test_CommercialSaveProperty_BW131(self):           
        wait(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click(Pattern("FrontPage_Commercial_Button.png").similar(0.80))
        wait(2)
        click("FrontPage_Search_Button-1.png")
        wait(2)
        find("FrontPage_CommercialFacet.png")
        click("FrontPageSearchResults_SaveProperty_Button-1.png")
        find("SaveProperty_Check_Button-1.png")
        click(Pattern("UsernameMyAccount-2.png").targetOffset(86,-5))
        click("AccountDropdown_Profile_Button-1.png")
        click("ProfilePage_SavedProperties_Button-1.png")
        wait(1)
        find("SavedPropertiesPage_MoreDetailsRemove_Button-1.png")
        click("SavedPropertiesPage_MoreDetails_Button.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_ResidentialSavedProperties_BW128(self):
        wait(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click("FrontPage_Buy_Button.png")
        wait(2)
        click("FrontPage_Search_Button.png")
        wait(2)
        find("FrontPage_ResidentialFacet.png")
        click("FrontPageSearchResults_SaveProperty_Button.png")
        find("SaveProperty_Check_Button.png")
        click(Pattern("UsernameMyAccount-3.png").targetOffset(85,-5))
        click("AccountDropdown_Profile_Button.png")
        click("ProfilePage_SavedProperties_Button.png")
        wait(1)
        find("SavedPropertiesPage_MoreDetailsRemove_Button.png")
        click("SavedPropertiesPage_MoreDetails_Button-2.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_RuralSavedProperties_BW129(self):
        wait(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click("FrontPage_RuralSearch_Button.png")
        wait(2)
        click("FrontPage_Search_Button.png")
        wait(2)
        find("FrontPage_RuralFacet.png")
        click("FrontPageSearchResults_SaveProperty_Button.png")
        find("SaveProperty_Check_Button.png")
        click(Pattern("UsernameMyAccount-3.png").targetOffset(85,-5))
        click("AccountDropdown_Profile_Button.png")
        click("ProfilePage_SavedProperties_Button.png")
        wait(1)
        find("SavedPropertiesPage_MoreDetailsRemove_Button.png")
        click("SavedPropertiesPage_MoreDetails_Button-2.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False

    def test_RentalSavedProperties_130(self):
        wait(Pattern("UsernameMyAccount-1.png").targetOffset(81,-2))
        click("FrontPage_Rent_Button.png")
        wait(2)
        click("FrontPage_Search_Button.png")
        wait(2)
        find("FrontPage_RentalFacet.png")
        click("FrontPageSearchResults_SaveProperty_Button.png")
        find("SaveProperty_Check_Button.png")
        click(Pattern("UsernameMyAccount-3.png").targetOffset(85,-5))
        click("AccountDropdown_Profile_Button.png")
        click("ProfilePage_SavedProperties_Button.png")
        wait(1)
        find("SavedPropertiesPage_MoreDetailsRemove_Button.png")
        click("SavedPropertiesPage_MoreDetails_Button-2.png")
        wait(1)
        if exists("PropertyDetailPage_SavedProperty_Button-1.png"):
            assert True
        else:
            assert False
        

