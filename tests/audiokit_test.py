"""
audiokit_test.py Test audiokit.

@history
 2021-06-07 wangxq Created.

Copyright (c) 2021~ wangxq.
"""

import argparse
import os

import pytest
import audiokit

def test_version():
    assert audiokit.__version__ == '0.0.2'
