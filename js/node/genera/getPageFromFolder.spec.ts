import { getMenuTree } from './getPageFromFolder'

void async function test() {
    console.dir(await getMenuTree(process.cwd()), {
        depth: Infinity
    })
}()
