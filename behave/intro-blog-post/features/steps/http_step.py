#!/usr/bin/env python3

"""
The following is a suite of behave steps to perform an HTTP request and retrieve the HTTP response code.
"""

import requests
from behave import given, when, then


@given("the HTTP endpoint has been defined")
def step(context):
    context.endpoint = f"https://{context.domain}"


@when("we connect to the HTTP endpoint")
def step(context):
    result = requests.get(context.endpoint)
    context.status_code = result.status_code


@then('we get the response code "{status_code}"')
def step(context, status_code):
    assert context.status_code == int(status_code)
