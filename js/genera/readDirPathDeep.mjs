import fs from 'fs'
import path from "path"
import { promisify } from "util"
const readDir = promisify(fs.readdir)
const stat = promisify(fs.stat)
/*
* dirpath 目录相对路径或绝对路径
* @return 该目录下所有文件和目录的绝对路径列表
*/
const readDirPathDeep = async (dirpath) => {
    let result_path = []
    for (let filepath of (await readDir(dirpath)).map((filename) => path.join(dirpath, filename))) {
        result_path.push(path.resolve(filepath))
        if ((await stat(path.resolve(filepath))).isDirectory()) {
            result_path.push.apply(result_path, await readDirPathDeep(filepath))
        }
    }
    return result_path
}
void async function test() {
    const cwd = process.cwd()
    //console.log(await readDir(cwd, {withFileTypes:'pug'}))
    console.log((await readDirPathDeep(cwd)))//.map(f=>f.replace(cwd,'')))
}()