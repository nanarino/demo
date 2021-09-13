"""
需求：
    不裁切打印纸币的时候
    要求堆叠后上下张连号
    请按单张的顺序给出序列号
"""

size = int(input("请输入单页最大值    "))
limit = int(input("请输入起始序号    "))
offset = int(input("需要处理的序号数    "))


def creapagi(size, limit, offset):
    '''
    size    单页最大值
    limit   起始序号
    offset  需要处理的序号数
    @->     分页后的列表
    '''
    overflow = offset % size
    page = offset // size
    li = list(range(limit, limit + offset))
    overflowli = li[offset - overflow:]
    li = list(zip(*[iter(li)] * page))[:size]
    for j in range(page)[::-1]:
        for i in li[::-1]:
            overflowli.insert(0, i[j])
    return overflowli


pagi = creapagi(size, limit, offset)

filename = 'pagi.txt'
with open(filename, "w") as f:
    for i in pagi:
        f.writelines(str(i) + '\n')