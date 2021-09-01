# Copyright The Cloud Custodian Authors.
# SPDX-License-Identifier: Apache-2.0

import logging
from c7n_ibmcloud.resources import (
    virtual_server,
)

log = logging.getLogger('custodian.ibmcloud')

ALL = [
virtual_server]


def initialize_ibmcloud():
    """ibmcloud entry point
    """