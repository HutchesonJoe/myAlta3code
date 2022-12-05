#!/usr/bin/python3

import module53challenge01
import pytest
import os

def test_challenge():
    with pytest.raises(RuntimeError) as this_test:
        module53challenge01.main()
    path = '~mycode/testing/challengetest.py'

    assert os.path.exists(path) in str(this_test.value)
