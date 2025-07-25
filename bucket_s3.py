#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MPL-2.0

__commit_date__ = "2025-07-24"
__commit_msg__ = "v002 + add gitleaks allow :bucket_s3.py"
__repository__ = "https://github.com/wilsonmar/sample-secrets/blob/main/sample-secrets.py"
# Adapted from https://github.com/GitGuardian/sample-secrets
__status__ = "Intentional secrets for secret scanners gitleaks and GitGuardian to find secrets in code."
# WARNING: GitHub scans would disallow git commit of this file.

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkja")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

# Mark a secret value to ignore by the scanner:
# https://help.aikido.dev/code-scanning/scanning-practices/ignoring-secrets-via-code-comments
a = "live_cdrBarsVQi4EGFRJi" # gitleaks:allow

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
