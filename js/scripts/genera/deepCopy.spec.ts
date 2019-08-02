import deepCopy from "./deepCopy"

const KEY = Symbol("☘")

const o1 = {
    [KEY]: 1,
    name: "test",
    arr: [1, 2, 3],
}

const o2 = deepCopy(o1)

console.log(Reflect.has(o1, KEY))
console.log(Reflect.has(o2, KEY))
console.log(Reflect.get(o1, "arr") === Reflect.get(o2, "arr"))
