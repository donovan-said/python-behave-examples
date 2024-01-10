#!/usr/bin/env python3

"""
The following is a suite of behave steps common to all steps in these behave
tests
"""

from behave import given, when, then


@given('TBC "{x}" with value "{y}"')
def step(context, x, y):
    pass


@when("TBC")
def step(context):
    pass


@then("TBC")
def step(context, status_code):
    pass
