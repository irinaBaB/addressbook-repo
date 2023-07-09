import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseurl = request.config.getoption("--baseUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, baseurl=baseurl)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, baseurl=baseurl)
    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default='chrome')
    parser.addoption("--baseUrl", action='store', default="http://localhost/addressbook/")
    parser.addoption('--username', action='store', default='')
    parser.addoption('--password', action='store', default='')



