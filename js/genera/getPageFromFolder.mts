import fs from 'fs';
import path from "path";
import { promisify } from "util";

const stat = promisify(fs.stat);
const readDir = promisify(fs.readdir);


export const getMenuList = async (currentDir: string, rootDir: string = currentDir): Promise<string[]> => {
    const fileList: string[] = [];
    if ((await stat(path.resolve(currentDir))).isFile()) {
        return [
            path.relative(rootDir, currentDir)
                .split(path.sep)
                .join(path.posix.sep)
                .replace(/\/(index\.html)$/i, "")
                .replace(/(\.html)$/i, "")
        ];
    }
    for (const filePath of (await readDir(currentDir)).map((fileName) => path.join(currentDir, fileName))) {
        fileList.push(...await getMenuList(filePath, rootDir));
    }
    return fileList;
}

export interface page {
    path: string;
}
export interface menu extends page {
    children: page[];
}

export const getMenuTree = async (currentDir: string): Promise<Array<page | menu>> => {
    const children: Array<page | menu> = [];
    if ((await stat(path.resolve(currentDir))).isFile()) return []
    for (const fileName of (await readDir(currentDir))) {
        const filePath = path.join(currentDir, fileName);
        children.push({
            path: `/${fileName}`,
            ...((await stat(filePath)).isFile()) ? null : {
                children: await getMenuTree(filePath),
            }
        });
    }
    return children;
}