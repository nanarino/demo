from pydantic import ValidationError, BaseModel
from enum import Enum
from typing import Optional


# $('.wi-form-item.hide').show()

class http_method(Enum):
    get = "GET"
    post = "POST"
    put = "PUT"
    delete = "DELETE"
    patch = "PATCH"

    def __repr__(self):
        return repr(self.value)


class prms_child(BaseModel):
    url: str
    method: http_method = http_method.get
    title: str

    def __init__(self, *, url: str, method: http_method = http_method.get, title: str, **data):
        return super().__init__(url=url, method=method, title=title, **data)

    def __new__(cls, *args, url="", method=http_method.get, title="", id="", children=None, **kwargs):
        if not hasattr(cls, '_instance_id_set'):
            cls._instance_id_set = set()
        if id:
            if id in cls._instance_id_set:
                raise ValidationError(f'id {id} 已存在')
            cls._instance_id_set.add(id)
        return super().__new__(cls, *args, **kwargs)

    def __repr__(self):
        return self.json()


class prms(prms_child):
    id: str = ''
    children: list[prms_child] = list()

    def __init__(self, *, url: str, method: http_method = http_method.get, title: str, id: str, children: Optional[list[prms_child]] = None):
        if children is None:
            children = list()
        return super().__init__(url=url, method=method, title=title, id=id, children=children)


资源创建 = [
    prms(
        url='/reserve-service/res/create',
        title='资源创建',
        method=http_method.post,
        id='l:cc:rescreate',
        children=[
            prms_child(title='规则条件下拉', url='/reserve-service/rule/getConditionList'),
            prms_child(title='身份规则下拉', url='/reserve-service/rule/selectIdentity'),
            prms_child(title='流程下拉', url='/reserve-service/flow/getReserveFlowList'),
            prms_child(title='环境下拉', url='/reserve-service/scenes/getScenesList'),
            prms_child(title='分组下拉', url='/reserve-service/res/selectGroupList'),
            prms_child(title='类型下拉', url='/reserve-service/res/selectTypeList'),
            prms_child(title='资源回显', url='/reserve-service/res/{id}'),
            prms_child(title='获取资源规则', url='/reserve-service/rule/{id}'),
            prms_child(title='获取日期禁用规则', url='/reserve-service/rule/ruleList'),
            prms_child(title='新增类型', url='/reserve-service/resType/',method=http_method.post),
            prms_child(title='新增分组', url='/reserve-service/resGroup/',method=http_method.post),
            prms_child(title='新增环境', url='/reserve-service/scenes/',method=http_method.post),
        ]
    )
]

print(资源创建)
