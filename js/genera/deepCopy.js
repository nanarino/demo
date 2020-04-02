//使用重写的type函数实现深拷贝
function deepCopy(obj) {
    if (type(obj) == 'array') {
        let newobj = []
        for (let i in obj) {
            newobj[i] = deepCopy(obj[i])
        }
        return newobj
    }
    if (type(obj) == 'object') {
        let newobj = {}
        for (let i in obj) {
            newobj[i] = deepCopy(obj[i])
        }
        return newobj
    }
    return obj
}
//以上方法未对对象是否成环进行判断。