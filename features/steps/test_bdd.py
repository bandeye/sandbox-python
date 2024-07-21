from pytest_bdd import parsers, given, scenarios, when, then
from playwright.sync_api import *
import pytest


@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()

scenarios("../features/api.feature")

@given(parsers.parse('The API endpoint is "{url}"'), target_fixture="api")
def api_endpoint(url, request_context):
    target = {"url": url, "request_context": request_context}
    return target


@when(parsers.parse("A GET request is made"))
def get_request(api):
    response = api["request_context"].get(api["url"])
    api["response"] = response


@then(parsers.parse("The response status code should be {status_code}"))
def get_response(api, status_code):
    response: APIResponse = api["response"]
    assert int(status_code) == response.status


@then(parsers.parse('The response should contain "{attribute}"'))
def get_attribute(api, attribute):
    response: APIResponse = api["response"]
    assert attribute in response.json()