# create_author: HuangYaxing
# create_time: 2021/10/12 8:43 下午

import json
import sqlite3

import re
import requests
import time

HOSTNAME = "127.0.0.1"


# TODO: 要用class来改写这个文件，不然第一眼都无法区分那些是函数那些是变量了
class ApiTestCase(object):
    def __init__(self):
        self.task_id = ""
        self.task_num = ""
        self.id = ""

    def url_param(self, param):
        param_1 = param.replace("&quot;", "\"")
        return param_1

    def read_res(self, res, res_check):
        if str(res) == res_check:
            return "pass"
        return "fail"

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
        sql = "update apitest_apistep set api_status=? where id=?"
        param = (result, case_id)

        conn = sqlite3.connect("../djangotest.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql, param)
        conn.commit()
        cursor.close()
        conn.close()

    def write_bug(self, bug_id, interface_name, request, response, res_check):
        interface_name = interface_name.encode("utf-8")
        res_check = res_check.encode("utf-8")
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        bug_name = "{0}_{1}_出错了".format(bug_id, interface_name)
        # TODO: <br/>在html里换行符，这里是否需要换/n呢？
        bug_detail = "[请求数据]<br/>{0}<br/>[预期结果]<br/>{1}<br/>[响应数据]<br/>{2}<br/>".format(request, res_check, response)
        print(bug_detail)

        sql = "insert into 'bug_bug' ('bug_name', 'bug_detail', 'bug_status', 'bug_level', 'bug_creator', 'bug_assign', 'create_time', 'product_id') " \
              "values ('{0}', '{1}', '1', '1', 'test', 'test', '{2}', '2');".format(bug_name, bug_detail, now)
        conn = sqlite3.connect("../db.sqlite3")
        cursor = conn.cursor()
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
                case_id = case[0]
                interface_name = case[1]
                url = case[2]
                method = case[3]
                param = case[4]
                res_check = case[5]
            except Exception as e:
                return "测试用例格式不正确， {0}".format(e)

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
            responses.append(response)
            res = self.read_res(response.status_code, res_check)
            print(res)

            if "pass" == res:
                self.write_result(case_id, "1")
                res_flags.append("pass")
            else:
                self.write_result(case_id, "0")
                res_flags.append("fail")
            self.write_bug(case_id, interface_name, url, response, res_check)

    def read_sql_case(self):
        sql = "select id, api_name, api_url, api_method, api_param_value, api_result, api_status from apitest_apistep where apitest_apistep.id<10"
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
