import fs from 'fs'
import path from "path"
import { promisify } from "util"
const readDir = promisify(fs.readdir)
const stat = promisify(fs.stat)
/*
* dirpath 目录相对路径或绝对路径
* @return 该目录下所有文件和目录的绝对路径列表
*/
export default async function readPathDeep(dirpath: string) {
    let result_path: string[] = []
    if ((await stat(path.resolve(dirpath))).isFile()) {
        return [path.resolve(dirpath)]
    }
    for (let filepath of (await readDir(dirpath)).map((filename) => path.join(dirpath, filename))) {
        result_path.push(... await readPathDeep(filepath))
    }
    return result_path
}