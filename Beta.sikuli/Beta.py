wheel("1455070857902.png", WHEEL_DOWN, 10)
find("BrancPage_SorroundingSuburbs.png").below(30).left(-15).click()
if exists(Pattern("ResultsPage_Title.png").similar(0.79)):
    assert True
else:
    assert False