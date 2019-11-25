from datetime import datetime

from test_wework.api.department import Department


class TestDepartment:
    department = Department()

    def setup_class(self):
        pass

    def test_list(self):
        r = self.department.list("")
        assert r["errcode"] == 0
        assert r["department"][0]["name"] == "海鑫金融"

    def test_create(self):
        name = "影音子部门8" + str(datetime.now().second)

        r = self.department.create(name, 2, 97, 48)
        assert r["errcode"] == 0
        assert r["id"] != None

        # 写法一：
        # exist = False
        # for depart in self.department.list("")["department"]:
        #     if depart["id"] == r["id"]:
        #         exist = True
        # assert exist == True

        #写法二：
        self.department.list("")
        print("&*&*&*&*&*&")
        print("$.department[?(@.id==%s)]" % r["id"])
        assert self.department.jsonpath("$.department[?(@.id==%s)]" % r["id"]) == 46
        assert self.message.jsonpath("$.errcode") == 0
        # print(self.department.jsonpath("$.department"))
        # assert self.department.jsonpath("$.department[?(@.id==%s)]" % r["id"])[0]["name"] == name

    def test_delete(self):
        cre_r = self.department.create("影音子部门5", 2, 96, 25)
        if cre_r["errcode"] == 0:
            del_id = cre_r["id"]
            del_r = self.department.delete(del_id)
        assert del_r["errcode"] == 0

    def test_update(self):
        cre_r = self.department.create("影音子部门7", 2, 95, 27)
        if cre_r["errcode"] == 0:
            upd_id = cre_r["id"]
            update_r = self.department.update(upd_id, "修改后的子部门", 2, 98)
        assert update_r["errcode"] == 0

    def test_update_1(self):
        depart = self.department.list("")['department'][1]
        id = depart['id']
        name = depart['name']
        assert self.department.update_1(id, name=name + '1')['errcode'] == 0
        assert self.department.list(id)['department'][0]['name'] == name + '1'



