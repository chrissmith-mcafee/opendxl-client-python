# -*- coding: utf-8 -*-
################################################################################
# Copyright (c) 2017 McAfee Inc. - All Rights Reserved.
################################################################################


class DxlException(Exception):
    """
    A general Data Exchange Layer (DXL) exception
    """


class MalformedBrokerUriException(DxlException):
    """
    An exception that is raised when a URL related to a DXL broker is malformed
    """


class WaitTimeoutException(DxlException):
    """
    Exception that is raised when a wait timeout is exceeded
    """


class BrokerListError(Exception):
    """
    Exception raised when a specified broker list is invalid
    """
    pass
