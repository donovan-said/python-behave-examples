#!/usr/bin/env python3

import json
import copy
from behave.model import ScenarioOutline
from pathlib import Path


def before_all(context):
    userdata = context.config.userdata
    if userdata["env"] == "dev":
        context.something = "something"
    elif userdata["env"] == "uat":
        context.something = "something"
    elif userdata["env"] == "prod":
        context.something = "something"


# Please see: https://github.com/behave/behave/issues/622
def before_feature(context, feature):
    userdata = context.config.userdata
    env_mapping = Path(
        f"static/features/context/{userdata['env']}_context.json"
    )

    endpoint_prefix = []

    with open(env_mapping) as f:
        data = json.load(f)

    for env_k, env_v in data.items():
        sub_env = env_v.keys()
        for i in sub_env:
            endpoint_prefix.append(i)

    """
    The following is used to dynamically populate the "Scenario Outline
    Examples", specifically by adding the sub environments.
    """
    features = (
        scenario
        for scenario in feature.scenarios
        if type(scenario) == ScenarioOutline and "dynamic" in scenario.tags
    )
    for scenario in features:
        for example in scenario.examples:
            orig = copy.deepcopy(example.table.rows[0])
            example.table.rows = []
            for row in endpoint_prefix:
                n = copy.deepcopy(orig)
                n.cells = ["{}".format(row)]
                example.table.rows.append(n)
