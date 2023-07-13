import { find, flat, del, getAncestors } from './tree'

type nodeData = { name: string }
const treeData = [
    {
        id: 1,
        name: 'No.1'
    },
    {
        id: 2,
        name: 'No.2',
        children: [
            {
                id: 3,
                name: 'No.3',
                children: [
                    {
                        id: 4,
                        name: 'last'
                    }
                ]
            }
        ]
    }
]

console.log(find<nodeData>({ id: 0, children: treeData }, 2)?.name)
console.log(del<nodeData>({ id: 0, children: treeData }, 1))
console.dir(flat<nodeData>({ id: 0, children: treeData }), { depth: Infinity })
console.log(getAncestors<nodeData>({ id: 0, children: treeData }, 4))
