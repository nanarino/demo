const { createInterface } = require("readline")
const axios = require('axios').default
const crypto = require('crypto')
const url = "https://ifanyi.iciba.com/index.php?"

const input = question => {
    return new Promise((resolve, reject) => {
        const readline = createInterface({
            input: process.stdin,
            output: process.stdout
        })
        readline.question(question, input => {
            input ? resolve(input) : reject()
            readline.close()
        })
    })
}

void async function main(){
    let q
    try {
        q = await input(`请输入你要翻译的单词::`)
    } catch (err) {
        console.log(`无输入，结束程序`)
        return
    }
    const key = "6key_cibaifanyicjbysdlove1" + q
    const sign = crypto.createHash('md5').update(key).digest("hex").substring(0, 16)
    const data = new URLSearchParams()
    data.set('from', "auto")
    data.set('to', 'auto')
    data.set('q', q)
    const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    try {
        const resp = await axios.post(url, data.toString(), {
            'headers': headers,
            'params': {
                'c': 'trans',
                'm': 'fy',
                'client': 6,
                'auth_user': 'key_ciba',
                'sign': sign
            }
        })
        console.log(resp.data["content"]["out"])
    } catch (err) {
        console.log(`请求失败：${err}`)
    }
}()
