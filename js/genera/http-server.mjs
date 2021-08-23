import fs from "fs"
import http from "http"
import path from "path"
import {networkInterfaces} from "os"
import {createInterface} from "readline"

let localWlanHost = '127.0.0.1';

const server = http.createServer((req, res) => {
    let pathname = path.join(process.cwd(), decodeURIComponent(req.url))
    if (path.extname(pathname) == "") {
        pathname += "/";
    }
    if (pathname.charAt(pathname.length - 1) == "/") {
        pathname += "index.html";
    }

    fs.readFile(pathname, (err, data) => {
        if (err) {
            res.writeHead(404, { "Content-Type": "text/html" });
            fs.readFile('./404.html', (err, data) => {
                res.end(err ? `<h1>404 Not Found</h1>` : data);
            });
        } else {
            switch (path.extname(pathname)) {
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
        }
    });
})

try {
    const ifaces = networkInterfaces();
    for (let lans of Object.values(ifaces)) {
        lans.forEach(details => {
            if (details.family === 'IPv4' && details.address !== '127.0.0.1' && !details.internal) {
                localWlanHost = details.address;
            }
        });
    }
} catch (e) {
    console.log(e);
}

const readline = createInterface({
    input: process.stdin,
    output: process.stdout
})

readline.question('input port:', input => {
    let port = Number.parseInt(input) || 80;
    server.listen(port);
    console.log(`Server running at \x1b[36mhttp://${localWlanHost}:${port}/\x1b[39m`);
    readline.close();
})