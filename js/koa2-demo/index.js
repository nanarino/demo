const Koa = require('koa2')
const static = require('koa-static')
const Router = require('koa-router')
const cors = require('@koa/cors')
const fs = require('fs')
const { join } = require("path")


const app = new Koa
const router = new Router

app.use(static(join(__dirname, 'static')))
router.get('/index', async (ctx, next) => {

    ctx.body = fs.readFileSync(join(__dirname, 'index.html'), 'utf8')

})

app.use(cors())

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(80)