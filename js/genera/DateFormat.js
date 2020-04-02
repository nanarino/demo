/**
 *
 *本文件只针对日期格式做兼容IE7的处理
 *如"Y/m/d" "Y-m-d"  而不处理时刻
 *
 *注意 本文件的代码会污染Date的原型链
 *按需引入时需要注意调用关系
 */


/**
 * @desc 日期格式化 不改变原对象
 * @param connchar 分隔符如"-"，如果不传则什么也不会做
 * @return -> 参数如上的返回值将是 '2004-06-18'
 */
Date.prototype.format = function (connchar) {
    if (!connchar) return this;
    return [this.getFullYear(), ("0" + (this.getMonth() + 1)).slice(-2), ("0" + this.getDate()).slice(-2)].join(connchar)
}


/**
 * @desc 针对IE7兼容的日期对象生成 静态方法
 * @param dateStr 如'2004-06-05' （兼容不写0如'2004-6-5'，纯数字'20040605'，也兼容多种连接符）
 * @return -> 参数如上的返回值将是 [date] Sat Jun 5 00:00:00 UTC+0800 2004
 */
Date.from = function (dateStr) {
    if (!isNaN(+dateStr) && (dateStr.length === 8)) {
        dateStr = [dateStr.slice(0, 4), dateStr.slice(4, 6), dateStr.slice(6, 8)].join('/')
    }
    var _newDate = new Date(dateStr.replace(/\W/g, "/"))
    if (isNaN(_newDate)) throw new Error('时间格式错误');
    return _newDate
}

/**
 * @desc 判断日期是否符合格式
 * @param -> string 待检验的日期字符串dateStr
 * @return -> boolean
 */
Date.isDateStr = function (dateStr) {
    try {
        this.from(dateStr)
    } catch (e) {
        return false
    }
    return true
}

/**
 * @desc 日期区间计算及格式化 静态方法
 * @param start  字符串如'2004-06-18'或[date]对象
 * @param stop  字符串如'2004-06-20'或[date]对象
 * @param connchar  分隔符如"-" , 如果不传则返回[date]对象构成的区间
 * @return -> 参数如上的返回值将是 ['2002-06-18','2004-06-19']
 */
Date.dateRange = function (start, stop, connchar) {
    if ({}.toString.call(start) != "[object Date]") { start = this.from(start) }
    if ({}.toString.call(stop) != "[object Date]") { stop = this.from(stop) }
    var _dateRange = [];
    for (var i = start.getTime(); i < stop.getTime(); i += 86400000) {
        _dateRange.push(new Date(i).format(connchar));
    }
    return _dateRange
}