

def pytest_sessionfinish(session, exitstatus):
    print("\nTotal run:", session.testscollected)
    print(">>>>>>>>>>>>>>>Passed:", session.testscollected - session.testsfailed)
    print(">>>>>>>>>>>>>>>Failed:", session.testsfailed)