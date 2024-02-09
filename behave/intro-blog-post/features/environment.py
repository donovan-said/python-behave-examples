#!/usr/bin/env python3


def before_all(context):
    userdata = context.config.userdata
    if userdata["env"] == "dev":
        context.domain = "donovan-said.github.io/"
    elif userdata["env"] == "uat":
        context.domain = "donovan-said.github.io/"
    elif userdata["env"] == "prod":
        context.domain = "donovan-said.github.io/"
