import os
import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.moneyhelper.org.uk/en/money-troubles/coronavirus/use-our-money-navigator-tool')
    request.cls.driver = driver

    yield
    driver.quit()
    print('using yield to quit the browser')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            take_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:400px;height=300px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def take_screenshot(name):
    driver.save_screenshot(name)


def pytest_html_report_title(report):
    report.title = 'money helper'

