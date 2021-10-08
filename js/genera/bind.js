Function.prototype.bind = function () {
    var bindThis = arguments[0]
    var arg = Array.prototype.slice.call(arguments, 1)
    var that = this
    return function () {
        that.apply(bindThis, arg)
    }
}