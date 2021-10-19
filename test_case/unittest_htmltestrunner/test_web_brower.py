# create_author: HuangYaxing
# create_time: 2021/10/17 11:11 下午

import os
import sqlite3
import time
import unittest
from selenium import webdriver


global driver
HOSTNAME = "127.0.0.1"


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        time.sleep(1)

    def test_read_sql_case_1(self):
        sql = "select id, web_case_find_method, web_case_element, web_case_opt_method, web_case_test_data " \
              "from web_test_webcasestep where web_case_id=3"
        conn = sqlite3.connect("../djangotest.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)

        db_info = cursor.fetchall()
        case_list = []
        for message in db_info:
            case_list.append(message)
        self.web_test_case(case_list)
        conn.commit()
        cursor.close()
        conn.close()

    def tearDown(self):
        self.driver.quit()

    def web_test_case(self, case_list):
        for case in case_list:
            try:
                (case_id, find_method, element, opt_method, test_data) = case
            except Exception as E:
                return "{0},param is {1}".format(E, case)

            time.sleep(2)
            if opt_method == "sendkeys" and find_method == "find_element_by_id":
                self.driver.find_element_by_id(element).send_keys(test_data)
            elif opt_method == "click" and find_method == "find_element_by_name":
                self.driver.find_element_by_name(element).click()
            elif opt_method == "click" and find_method == "find_element_by_id":
                self.driver.find_element_by_id(element).click()

