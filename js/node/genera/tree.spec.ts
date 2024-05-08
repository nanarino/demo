import { find, flat, remove, getAncestors } from "./tree"

type Data = { name: string }
const treeData = [
    {
        id: 1,
        name: "No.1",
        level: 1,
    },
    {
        id: 2,
        name: "No.2",
        level: 1,
        children: [
            {
                id: 3,
                name: "No.3",
                level: 2,
                children: [
                    {
                        id: 4,
                        name: "last",
                        level: 3,
                    },
                ],
            },
        ],
    },
]

console.log(find<Data>({ id: 0, children: treeData }, 2)?.name)
console.log(remove<Data>({ id: 0, children: treeData }, 1))
console.log(flat<Data>({ id: 0, children: treeData }))
console.log(getAncestors<Data>({ id: 0, children: treeData }, 4))
