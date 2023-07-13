export type treeNode<nodeData> = nodeData & {
  id: number
  children?: treeNode<nodeData>[]
  parentId?: number
}
export type treeRoot<nodeData> = Partial<nodeData> & {
  id: 0
  children: treeNode<nodeData>[]
}

export function find<nodeData>(tree: treeNode<nodeData> | treeRoot<nodeData>, id: number): treeNode<nodeData> | treeRoot<nodeData> | null {
  let i = 0, found: treeNode<nodeData> | treeRoot<nodeData> | null
  if (tree.id === id) return tree
  if (Array.isArray(tree.children)) {
    for (; i < (tree.children).length; i++) {
      if (tree.children[i].id === id) {
        return tree.children[i]
      } else if (Array.isArray(tree.children[i].children)) {
        found = find(tree.children[i], id)
        if (found) return found
      }
    }
  }
  return null
}

export function flat<nodeData>(tree: treeNode<nodeData> | treeRoot<nodeData>, parentId?: number): treeNode<nodeData>[] {
  if (Array.isArray(tree.children) && tree.children.length) {
    return tree.children.reduce((t: treeNode<nodeData>[], node) => [
      ...t,
      parentId ? { ...node, parentId } : node,
      ...(Array.isArray(node.children) && node.children.length ? flat(node, node.id) : [])
    ], [])
  }
  return []
}

export function del<nodeData>(tree: treeNode<nodeData> | treeRoot<nodeData>, id: number): boolean {
  if (Array.isArray(tree.children)) {
    for (let i = 0; i < tree.children.length; i++) {
      if (tree.children[i].id === id) {
        tree.children.splice(i, 1)
        return true
      } else if (Array.isArray(tree.children[i].children)) {
        if (del(tree.children[i], id)) return true
      }
    }
  }
  return false
}

export function getAncestors<nodeData>(tree: treeNode<nodeData> | treeRoot<nodeData>, id: number): number[] {
  const getIds = (flatArray: treeNode<nodeData>[]) => {
    let ids = [id]
    let child = flatArray.find(_ => _.id === id)
    let hasChild: number | undefined
    while (hasChild = (child && child.parentId)) {
      ids = [child.parentId, ...ids]
      child = flatArray.find(_ => hasChild === _.id)
    }
    return ids
  }
  return getIds(flat(tree))
}
