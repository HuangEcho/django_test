# create_author: HuangYaxing
# create_time: 2021/10/16 12:41 上午
import os

from HtmlTestRunner import HTMLTestRunner
import unittest

import time


if __name__ == '__main__':
    test_cases = unittest.defaultTestLoader.discover("./")
    runner = HTMLTestRunner()
    runner.run(test_cases)
