import { networkInterfaces } from "os"
import { promisify } from "util"
import http from "http"
import path from "path"
import fs from "fs"
const readFile = promisify(fs.readFile)
import pug from "pug"            // 需要安装
const pugRenderSync = pug.render
import styl from "stylus"        // 需要安装
const stylRender = promisify(styl.render)
import { createInterface } from "readline"
const input = question => {
    return new Promise((resolve, reject) => {
        const readline = createInterface({
            input: process.stdin,
            output: process.stdout
        })
        readline.question(question, ipt => {
            ipt ? resolve(ipt) : reject('')
            readline.close()
        })
    })
}

let localWlanHost = '127.0.0.1';

const server = http.createServer(async (req, res) => {
    let pathname = path.join(process.cwd(), decodeURIComponent(req.url))
    if (path.extname(pathname) == "") {
        pathname += "/";
    }
    if (pathname.charAt(pathname.length - 1) == "/") {
        pathname += "index.html";
    }
    let data
    try {
        data = await readFile(pathname)
    } catch (err) {
        res.writeHead(404, { "Content-Type": "text/html" });
        try {
            data = await readFile('./404.html')
        } catch (err) {
            res.end(`<h1>404 Not Found</h1>`);
            return
        }
    }
    switch (path.extname(pathname)) {
        case ".pug":
            res.writeHead(200, { "Content-Type": "text/html" });
            try {
                data = pugRenderSync(data)
            } catch (err) {
                data = err.toString()
            }
            break;
        case ".styl":
            res.writeHead(200, { "Content-Type": "text/css" });
            try {
                data = await stylRender(data.toString('utf8'))
            } catch (err) {
                data = err.toString()
            }
            break;
        case ".html":
            res.writeHead(200, { "Content-Type": "text/html" });
            break;
        case ".js":
            res.writeHead(200, { "Content-Type": "text/javascript" });
            break;
        case ".mjs":
            res.writeHead(200, { "Content-Type": "text/javascript" });
            break;
        case ".css":
            res.writeHead(200, { "Content-Type": "text/css" });
            break;
        case ".json":
            res.writeHead(200, { "Content-Type": "application/json" });
            break;
        case ".ico":
            res.writeHead(200, { "Content-Type": "image/x-ico" });
            break;
        case ".gif":
            res.writeHead(200, { "Content-Type": "image/gif" });
            break;
        case ".jpg":
            res.writeHead(200, { "Content-Type": "image/jpeg" });
            break;
        case ".png":
            res.writeHead(200, { "Content-Type": "image/png" });
            break;
        case ".webp":
            res.writeHead(200, { "Content-Type": "image/webp" });
            break;
        case ".svg":
            res.writeHead(200, { "Content-Type": "image/svg+xml" });
            break;
        default:
            res.writeHead(200, { "Content-Type": "application/octet-stream" });
    }
    res.end(data);
})


void async function main() {
    try {
        const ifaces = networkInterfaces();
        for (let lans of Object.values(ifaces)) {
            lans.forEach(details => {
                if (details.family === 'IPv4' && details.address !== '127.0.0.1' && !details.internal) {
                    localWlanHost = details.address;
                }
            });
        }
    } catch (err) {
        console.log(err);
    }
    let port = 80
    try {
        port = Number.parseInt(await input(`input port:`))
    } catch (err) {
        console.log(err)
    }
    try {
        server.listen(port);
    } catch (err) {
        console.log(`Error：${err}`)
    }
    console.log(`Server running at \x1b[36mhttp://${localWlanHost}:${port}/\x1b[39m`);
}()