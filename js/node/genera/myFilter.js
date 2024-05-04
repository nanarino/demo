function myFilter(arr, cb) {
    let a = []
    for (let i = 0; i < arr.length; i++) {
        if (cb(arr[i], i, arr)) {
            a.push(arr[i])
        }
    }
    return a
}

Array.prototype.myFilter = function () {
    Array.prototype.unshift.call(arguments, this)
    return myFilter.apply(this, arguments)
}
