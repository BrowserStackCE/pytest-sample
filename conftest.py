import json
from threading import Thread
import pytest
from os import environ
from browserstack.local import Local

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection
import urllib3


@pytest.fixture(scope='function')
def driver(request):

    desired_caps = {}
    with open('config/capabilities_single.json') as json_file:
         data = json.load(json_file)

    capabilities = data["capabilities"]
    desired_caps.update(capabilities)
    username = environ.get('BROWSERSTACK_USERNAME', None)
    access_key = environ.get('BROWSERSTACK_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.browserstack.com/wd/hub".format(username, access_key)
    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    driver = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=desired_caps)
    yield driver


    def fin():
        if request.node.rep_call.failed:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Test execution had some issues,PLease refer the logs for more details"}}')
            driver.quit()
            # bs_local.stop()
        else:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Test case executed without any errors"}}')
            driver.quit()
            # bs_local.stop()
    request.addfinalizer(fin)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
