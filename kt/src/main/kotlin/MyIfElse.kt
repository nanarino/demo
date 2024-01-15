typealias case = () -> Unit

class If(private val a: Boolean) {
    infix fun 𝚎𝚕𝚜𝚎(cb: case) {
        if(a) cb()
    }
}

val 𝚒𝚏 = {
    b: Boolean, cb: case ->
    if(b) cb()
    If(!b)
}

fun main() {
    𝚒𝚏(0.1 + 0.2 == 0.3) {
        println("0.1 + 0.2 == 0.3")
    } 𝚎𝚕𝚜𝚎 {
        println("0.1 + 0.2 != 0.3")
    }
}
