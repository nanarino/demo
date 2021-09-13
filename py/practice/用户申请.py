'''
用户审核
        1、逐个添加新用户
        2、打印出未审核的用户姓名及名单
        3、输出正在审核的用户名单，正在审核的用户名单从未审核中去除
        4、待审核完成后，输出已完成审核的用户名单，并提示：xxx，恭喜你，已完成注册审核，可以使用了！
        5、审核完成的用户信息从正在审核的名单中删除
        6、要求使用面向对象来解决
'''


class UserModel:
    beforeChecked = set()  #未审核
    beingChecked = set()  #审核中
    afterChecked = set()  #已审核

    class User:
        def __init__(self, name):
            self.motif = "未审核"
            self.name = name

        def __repr__(self):
            return str(self.name) + "(" + self.motif + ")"

    def __init__(self, name):
        newUser = self.User(name)
        self.beforeChecked.add(newUser)

    @classmethod
    def all(cls):
        return cls.beforeChecked | cls.beingChecked | cls.afterChecked

    @classmethod
    def ready(cls, name):
        def motif_set(obj):
            setattr(obj, 'motif', "审核中")
            return obj

        queryset = set(
            map(motif_set, filter(lambda x: x.name == name,
                                  cls.beforeChecked)))
        if len(queryset):
            cls.beforeChecked = cls.beforeChecked - queryset
            cls.beingChecked = cls.beingChecked | queryset
            return name + "正在审核中"
        else:
            return "查无此人"

    @classmethod
    def checked(cls, name):
        def motif_set(obj):
            setattr(obj, 'motif', "已审核")
            return obj

        queryset = set(
            map(motif_set, filter(lambda x: x.name == name, cls.beingChecked)))
        if len(queryset):
            cls.beingChecked = cls.beingChecked - queryset
            cls.afterChecked = cls.afterChecked | queryset
            return name + "已完成审核，恭喜"
        else:
            return "查无此人"


while 1:
    print("\n\n 菜单：\n")
    print("\t a.添加新用户\n")
    print("\t b.申请审核用户\n")
    print("\t c.完成审核用户\n")
    print("\t d.查看完整名单\n")
    print("\t e.查看未审核名单\n")
    print("\t f.查看审核中名单\n")
    print("\t g.查看已审核名单\n")
    msg = input("请选择\t")

    def a():
        name = input("请输入name\t")
        UserModel(name)
        print("\t 新用户创建成功")

    def b():
        name = input("\t\t 请输入准备申请审核的用户name")
        print('\n\t' + UserModel.ready(name))

    def c():
        name = input("\t\t 请输入准备通过审核的用户name")
        print('\n\t' + UserModel.checked(name))

    def d():
        print('\n\t' + str(UserModel.all() or "空"))

    def e():
        print('\n\t' + str(UserModel.beforeChecked or "空"))

    def f():
        print('\n\t' + str(UserModel.beingChecked or "空"))

    def g():
        print('\n\t' + str(UserModel.afterChecked or "空"))

    if msg in ["a", "b", "c", "d", "e", "f", "g"]:
        eval(msg + "()")
