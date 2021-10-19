# create_author: HuangYaxing
# create_time: 2021/10/12 8:43 下午

import sqlite3

import requests
import time

import unittest

HOSTNAME = "127.0.0.1"


class ApiTestCase(object):

    # TODO: 目前写的，只验证了url和status_code，可以直接转化为str，但对于list，dict等类型就没有处理到
    def check_response_exception(self, response, exception):
        for key, value in exception.items():
            if hasattr(response, key):
                # 这里只验证了结果只在response第一个层级，且为int或str这种类型的，没有处理list这些的，等后面遇到了，再写
                except_value = str(getattr(response, key))
                value = str(value)
                if except_value not in value or len(except_value) != len(value):
                    return "response key {0} not equal expect value {1}".format(value, except_value)
            else:
                return "{0} not in response".format(key)

        return "pass"

    def write_result(self, case_id, result):
        result = result.encode("utf-8")
        now = time.strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("../../djangotest.sqlite3")
        cursor = conn.cursor()

        # sqlite不支持update与join一起，需要用子表改写
        # sql = "update apitest_apitest inner join apitest_apistep on apitest_apitest.id=apitest_apistep.api_test_id set apitest_apitest.api_test_result=?, apitest_apitest.create_time=?, apitest_apistep.api_status=?, apitest_apistep.create_time=? where apitest_apistep.id=?"
        sql = "update apitest_apistep set api_status=?, create_time=? where id=?"
        param = (result.decode("utf-8"), now, case_id)
        cursor.execute(sql, param)
        sql = "update apitest_apitest set api_test_result=?, create_time=? where id=(select api_test_id from apitest_apistep where id=?)"
        param = (result.decode("utf-8"), now, case_id)
        cursor.execute(sql, param)

        conn.commit()
        cursor.close()
        conn.close()

    def write_bug(self, bug_id, interface_name, url, res):
        interface_name = interface_name.encode("utf-8")
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        bug_name = "{0}_{1}_{2}".format(bug_id, str(interface_name, encoding="utf-8"), url)
        bug_detail = res

        sql = "insert into 'bug_bug' ('bug_name', 'bug_detail', 'bug_status', 'bug_level', 'bug_creator', 'bug_assign', 'create_time', 'product_id') " \
              "values ('{0}', '{1}', '1', '1', 'test', 'test', '{2}', '2');".format(bug_name, bug_detail, now)
        conn = sqlite3.connect("../../djangotest.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def interface_test(self, case_list):
        res_flags = []
        request_urls = []
        responses = []

        for case in case_list:
            try:
                case_id, interface_name, url, method, param, expected_response = case
            except Exception as e:
                return "测试用例格式不正确， {0}".format(e)
            # eval将str转化为dict
            try:
                expected_response = eval(expected_response)
            except:
                print("please check 预期结果 format")
                return
            # param = self.url_param(param)
            url = "http://" + url
            request_urls.append(url)
            response = ""

            if method.upper() == "GET":
                headers = {"Authorization": "", "Connect-Type": "application/json"}
                if param == "" or param == "null":
                    response = requests.get(url, headers=headers)
                else:
                    response = requests.get(url + "?" + param, headers=headers)
            elif method.upper() == "PUT":
                headers = {"Host": HOSTNAME, "Connection": "keep-alive", "CredentialId": id, "Content-Type": "applicaton/json"}
                if param == "" or param == "null":
                    body_data = None
                else:
                    body_data = param
                response = requests.put(url, body_data, headers=headers)
            elif method.upper() == "POST":
                headers = {"Authorization": "Credential", "Content-Type": "application/json"}
                response = requests.post(url, param, headers=headers)

            responses.append(response)
            res = self.check_response_exception(response, expected_response)
            res_flags.append(res)
            print("{0} result is {1}".format(interface_name, res))
            if "pass" == res:
                self.write_result(case_id, "1")
            else:
                self.write_result(case_id, "0")
                self.write_bug(case_id, interface_name, url, res)

    def test_read_sql_case(self):
        sql = "select apitest_apistep.id, apitest_apitest.api_test_name, apitest_apistep.api_url, apitest_apistep.api_method, apitest_apistep.api_param_value, apitest_apistep.api_result from apitest_apistep inner join apitest_apitest on apitest_apistep.api_test_id=apitest_apitest.id"
        conn = sqlite3.connect("../../djangotest.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()

        case_list = []
        for ii in info:
            case_list.append(ii)
        self.interface_test(case_list)

        conn.commit()
        cursor.close()
        conn.close()


# unnitest.TestCase
class TestCase(unittest.TestCase):
    # lost assert
    def test_read_sql_case(self):
        sql = "select apitest_apistep.id, apitest_apitest.api_test_name, apitest_apistep.api_url, apitest_apistep.api_method, apitest_apistep.api_param_value, apitest_apistep.api_result from apitest_apistep inner join apitest_apitest on apitest_apistep.api_test_id=apitest_apitest.id"
        conn = sqlite3.connect("../../djangotest.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()

        case_list = []
        for ii in info:
            case_list.append(ii)
        ApiTestCase().interface_test(case_list)

        conn.commit()
        cursor.close()
        conn.close()


if __name__ == '__main__':
    ApiTestCase().test_read_sql_case()



