import unittest
import os
import os.path
import json
import time
from AlternateAgentProfile import *
from AgentProfile1 import *
from BranchProfile import *
from Content import *
from FindUsBar import *
from FindUsPage import *
from FooterLinks import *
from QuickSearch import*
from WebsiteLoginComponent import*
from SavedProperties import*
from GlobalMobileSignIn import*
from PasswordReset import*
from SavedSearch import*
from PropertyDetail import*
import HTMLTestRunner
reload(HTMLTestRunner)

timestr = time.strftime("%d%m%Y%H%M%S")#creates a unique username for testing/date and time as a file name
configPath = os.path.join(os.path.dirname(os.getcwd()), "SikuliScripts\Repository\config.json")
with open(configPath, "r") as config:
    data = json.load(config)
tmp = data["username"]
data["username"] = timestr + "@test.com"
with open(configPath, "w") as config:
    config.write(json.dumps(data))

fileName = timestr + "Report.html"
dir='C:\SikuliScripts\Results'
outfile=file(os.path.join(dir,fileName), "wb")


suite=unittest.TestLoader().loadTestsFromTestCase(WebsiteLoginComponent) # setup new test suite
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SavedProperties))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SavedSearch))





runner = HTMLTestRunner.HTMLTestRunner(stream = outfile, title = 'Barfoot.co.nz Regression', description = 'Test barfoot.co.nz site')
#runner = HTMLTestRunner.HTMLTestRunner(stream = outfile, verbosity=2, dirTestScreenshots = 'c:\\SikuliScripts\\Results')
runner.run(suite)
outfile.close()