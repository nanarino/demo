export type TreeKey = number | bigint | string

export type TreeNode<Data> = Data & {
    id: TreeKey
    children?: TreeNode<Data>[]
    parentId?: TreeKey
    level?: number
}
export type TreeRoot<Data> = Partial<Data> & {
    id: 0
    children: TreeNode<Data>[]
}

export function find<Data>(
    tree: TreeNode<Data> | TreeRoot<Data>,
    id: TreeKey
): TreeNode<Data> | TreeRoot<Data> | null {
    let i = 0
    let found: TreeNode<Data> | TreeRoot<Data> | null
    if (tree.id === id) return tree
    if (Array.isArray(tree.children)) {
        for (; i < tree.children.length; i++) {
            if (tree.children[i].id === id) {
                return tree.children[i]
            } else if (tree.children[i].children?.length) {
                found = find(tree.children[i], id)
                if (found) return found
            }
        }
    }
    return null
}

export function flat<Data>(
    tree: TreeNode<Data> | TreeRoot<Data>,
    parentId?: TreeKey
): TreeNode<Data>[] {
    if (tree.children?.length) {
        return tree.children.reduce(
            (t: TreeNode<Data>[], node) => [
                ...t,
                parentId ? { ...node, parentId } : node,
                ...(node.children?.length ? flat(node, node.id) : []),
            ],
            []
        )
    }
    return []
}

export function remove<Data>(
    tree: TreeNode<Data> | TreeRoot<Data>,
    id: TreeKey
) {
    if (Array.isArray(tree.children)) {
        for (let i = 0; i < tree.children.length; i++) {
            if (tree.children[i].id === id) {
                tree.children.splice(i, 1)
                return true
            } else if (Array.isArray(tree.children[i].children)) {
                if (remove(tree.children[i], id)) return true
            }
        }
    }
    return false
}

export function getAncestors<Data>(
    tree: TreeNode<Data> | TreeRoot<Data>,
    id: TreeKey
) {
    const getIds = (flatArray: TreeNode<Data>[]) => {
        let child = flatArray.find(_ => _.id === id)
        const children = child ? [child] : []
        let hasChild: TreeKey | undefined
        while ((hasChild = child?.parentId)) {
            child = flatArray.find(_ => hasChild === _.id)
            child && children.push(child)
        }
        return children
    }
    return getIds(flat(tree))
}
