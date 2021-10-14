# create_author: HuangYaxing
# create_time: 2021/10/12 8:43 下午

import json
import sqlite3

import re
import requests
import time

HOSTNAME = "127.0.0.1"


class ApiTestCase(object):
    def __init__(self):
        self.task_id = ""
        self.task_num = ""
        self.id = ""

    # 暂时用不上
    def url_param(self, param):
        param_1 = param.replace("&quot;", "\"")
        return param_1

    def get_status_code(self, res):
        return res.status_code

    def get_url(self, res):
        return res.url

    # TODO: 这里的想法是把要验证的点都写上，意味着不能动态，只能自己写
    def check_response_exception(self, response, exception):
        for key, value in exception.items():
            if "status_code" == key:
                if value != self.get_status_code(response):
                    return "response key {0} not equal expect value {1}".format(self.get_status_code(response), value)
            elif "url" == key:
                # is是判断内存，in判断值
                if value not in self.get_url(response) or len(value) != len(self.get_url(response)):
                    return "response key {0} not equal expect value {1}".format(self.get_url(response), value)
            # 如果还有其他要验证的点，需要在这里加上
            else:
                return "{0} not in response".format(key)

        return "pass"

    def credential_id(self):
        url = "http://api.test.com.cn/api/security/authentication/signin/web"
        body_data = json.dumps({"Identity": "test", "Password": "test"})
        headers = {"Connection": "keep-alive", "Content-Type": "application/json"}
        response = requests.post(url=url, data=body_data, headers=headers)
        data = response.text
        regx = '.*"CredentialId":"(.*)","Scene"'
        pm = re.search(regx, data)
        self.id = pm.group(1)

    def write_result(self, case_id, result):
        result = result.encode("utf-8")
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        sql = "update apitest_apistep set api_status=?, create_time=? where id=?"
        param = (result.decode("utf-8"), now, case_id)

        conn = sqlite3.connect("../djangotest.sqlite3")
        cursor = conn.cursor()
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
        conn = sqlite3.connect("../djangotest.sqlite3")
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
                # TODO:看看怎么写的更好看
                case_id, interface_name, url, method, param, expected_response = case
            except Exception as e:
                return "测试用例格式不正确， {0}".format(e)
            # eval将str转化为dict
            try:
                expected_response = eval(expected_response)
            except:
                print("please check 预期结果 format")
                return
            param = self.url_param(param)
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
                headers = {"Authorization": "Credential" + self.id, "Content-Type": "application/json"}
                response = requests.post(url, param, headers=headers)

            print("response is get {0}".format(response))
            print(response.url)
            responses.append(response)
            res = self.check_response_exception(response, expected_response)
            res_flags.append(res)

            if "pass" == res:
                self.write_result(case_id, "1")
            else:
                self.write_result(case_id, "0")
                self.write_bug(case_id, interface_name, url, res)

    def read_sql_case(self):
        sql = "select id, api_name, api_url, api_method, api_param_value, api_result from apitest_apistep where apitest_apistep.id<10"
        conn = sqlite3.connect("../djangotest.sqlite3")
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


if __name__ == '__main__':
    ApiTestCase().read_sql_case()



