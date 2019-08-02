fun test1() {
    val set1: MutableSet<Number> = mutableSetOf(114, 514)
    val set2: MutableSet<in Int> = set1
    set1.add(19.19)
    // set2.add(19.19) // 报错
    set2.add(1919)
    println(set2)
}
fun test2() {
    val set1: MutableSet<Int> = mutableSetOf(114, 514)
    val set2: MutableSet<out Number> = set1
    set1.add(1919) 
    // set2.add(1919) // 报错
    println(set2)
}
fun main() {
    test1()
    test2()
}
