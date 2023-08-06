from typing import Dict
import pytest
from pytest import StashKey, CollectReport

phase_report_key = StashKey[Dict[str, CollectReport]]()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep


def pytest_addoption(parser):
    # :help : сообщение, которое будет выведено при запуске тестов с флагом --help
    parser.addoption('--url', help='SUT stand')
    