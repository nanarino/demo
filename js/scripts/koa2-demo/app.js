const Koa = require("koa2")
const static = require("koa-static")
const router = require("./routers/router")
const cors = require("@koa/cors")
const fs = require("fs")
const { join } = require("path")
const render = require("koa-ejs")
const bodyParser = require("koa-bodyparser")

//生成Koa实例
const app = new Koa()

//配置静态资源目录
app.use(static(join(__dirname, "static")))
app.use(bodyParser())

render(app, {
    root: join(__dirname, "views"),
    layout: "layout",
    viewExt: "html",
    cache: false,
    debug: false,
})

//允许跨域请求
app.use(cors())
//注册路由信息
app.use(router.routes()).use(router.allowedMethods()).listen(80)
