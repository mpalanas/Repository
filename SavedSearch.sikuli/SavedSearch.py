from sikuli import*
import unittest
import json
import os

class SavedSearch(unittest.TestCase):

    def setUp(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        app = App(config["application"])
        openApp(app)
        wait(1)
        type("l", KeyModifier.CTRL)
        type(config["url"] + Key.ENTER)
        wait(4)
        if exists("UsernameMyAccount-1.png"):
            wait(1)
        else:
            click("SigninPage_SignIn_Button-1.png")
            click(Pattern("SignInPopUp_emailAddress_field-1.png").similar(0.62).targetOffset(-100,15))
            type(config["username"])
            type(Key.TAB)
            type(config["password"])
            click(Pattern("SignInPopUp_SignIn_Button-1.png").similar(0.94))

        

    def tearDown(self):
        if exists("UsernameMyAccount.png"):
            click(Pattern("UsernameMyAccount.png").targetOffset(104,3))
            click("MyAccount_SignOut_Button.png")
            wait(3)

            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)

            wait(2)
            
        else:
            configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
            config = json.loads(open(configPath).read())
            appTaskName = config["appTaskName"]
            os.system("taskkill /f /im " +appTaskName)
            wait(2)



    def test_1createSavedSearch_BW132(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        
        wait("MainPage_MyAccount_Dropdown.png")
        click("SearchBar_Region_Dropdown.png")
        click("Region_AucklandCity_Dropdown.png")
        find("SearchBar_Suburb_DropdownName.png").below(20).click()
        click("1455054875641.png")
        find("SearchBar_SurroundingSuburbs_DropdownName.png").below(20).click()
        find("SurroundingSuburb_Avondale_DropdownName.png").left(15).click()
        click("FrontPAge_Search_Button.png")
        click("MainPage_SaveSearch_Button.png")
        click(Pattern("SaveSearchWindow_ClearName_Button.png").similar(0.74))
        type("SavedSearch")
        click(Pattern("SavedSearch_Never_EmailAlertDropdown.png").similar(0.72))
        click("SavedSearch_Weekly_EmailAlertDropdown.png")
        click("SaveSearchWindow_SaveSearch_Button.png")
        click("MainPage_MyAccount_Dropdown.png")
        click("AccountDropdown_Profile_Button.png")
        click("Profilepage_SaveSearches_Button.png")
        
        if exists(Pattern("ProfilePage_SaveSavesearch_Details.png").similar(0.76)):
            assert True
        else:
            assert False


    def test_2EditSavedSearch_BW136(self): 
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait("MainPage_MyAccount_Dropdown.png")
        click("MainPage_MyAccount_Dropdown.png")
        click(Pattern("AccountDropdown_SaveSearch_Dropdown.png").similar(0.74).targetOffset(-29,10))
        click(Pattern("SaveSearchPage_ChangeName_Button.png").similar(0.76))
        wait(1)
        click("SaveSearchPAge_SaveSearchName_Textbox.png")
        type("a", KEY_CTRL)
        type(Key.DELETE)
        type("Saved Search Blockhouse Bay")
        click("SaveSearchPage_SaveChanges_Button.png")
        if exists(Pattern("SaveSearchPage_SaveSearch_Name.png").similar(0.84)):
            assert True
        else:
            assert False

        
    def test_3SavedSearchEditSchedule_BW136(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait("MainPage_MyAccount_Dropdown.png")
        click("MainPage_MyAccount_Dropdown.png")
        click("AccountDropdown_Profile_Button.png")
        click("Profilepage_SaveSearches_Button.png")
        click("SavedSearch_ViewAndEdit_Button.png")
        click("SavedSearch_EmailAlertWeekly_Dropdown.png")
        click("SavedSearch_EmailAlertDaily_Dropdown.png")
        find(Pattern("SavedSearch_OpenHome_Checkbox.png").similar(0.80)).left(15).click()
        click("SaveSearchPage_SaveChanges_Button.png")
        wait(2)
        type(Key.F5)
        wait(3)
        if exists("SaveSearchPage_ScheduleOpenHome_Details.png"):
            assert True
        else:
            assert False  


    def test_4SavedSearchRemove_BW141(self):
        configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
        config = json.loads(open(configPath).read())
        wait("MainPage_MyAccount_Dropdown.png")
        click("MainPage_MyAccount_Dropdown.png")
        click("AccountDropdown_Profile_Button.png")
        click("Profilepage_SaveSearches_Button.png")
        click("SavedSearchPage_Delete_Button.png")
        wait(1)
        type(Key.F5)
        wait(1)
        if exists("SavedSearch_NoSavedSearch_IE.png"):
            assert True
        elif exists("SavedSearch_NoSavedSearch_Chrome.png"):
            assert True
        else:
            assert False
    
