import readDirPathDeep from './readDirPathDeep'

void async function test() {
    console.dir(await readDirPathDeep(process.cwd()), {
        depth: Infinity
    })
}()
