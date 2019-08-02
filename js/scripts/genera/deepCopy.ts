import _type from "./type"
export default function deepCopy(obj: any): any {
    if (_type(obj) === "Array") {
        return (obj as any[]).map(deepCopy)
    } else if (_type(obj) === "Object") {
        return Object.fromEntries(
            Object.entries(obj as Record<string | symbol, any>).map(
                ([k, v]) => [k, deepCopy(v)]
            )
        )
    } else if (typeof obj === "object") {
        return {}.toString.call(obj)
    } else {
        return obj
    }
}
// 以上方法未对对象是否成环进行判断。
