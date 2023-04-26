export function find(tree, id) {
  let i = 0, found
  if (tree.id === id) return tree
  for (; i < tree.children.length; i++) {
    if (tree.children[i].id === id) {
      return tree.children[i]
    } else if (Array.isArray(tree.children[i].children)) {
      found = find(tree.children[i], id)
      if (found) return found
    }
  }
}

export function flat(tree, parentId) {
  return tree.children.reduce((t, node) => [
    ...t,
    parentId ? { ...node, parentId } : node,
    ...(Array.isArray(node.children) && node.children.length ? flat(node, node["id"]) : [])
  ], [])
}

export function del(tree, id) {
  for (let i = 0; i < tree.children.length; i++) {
    if (tree.children[i].id === id) {
      tree.children.splice(i, 1)
      return true
    } else if (Array.isArray(tree.children[i].children)) {
      if (del(tree.children[i], id)) return true
    }
  }
}

export const getTAncestors = (tree, nodeId) => {
  const getIds = flatArray => {
    let ids = [nodeId]
    let child = flatArray.find(_ => _["id"] === nodeId)
    while (child && child.parentId) {
      ids = [child.parentId, ...ids]
      child = flatArray.find(_ => _["id"] === child.parentId)
    }
    return ids
  }
  return getIds(flat(tree))
}
