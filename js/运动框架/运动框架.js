function getStyle(ele) {
  return ele.currentStyle || getComputedStyle(ele)
}

//简单的解决兼容问题
window.requestAnimationFrame = window.requestAnimationFrame || function (cb) { return setTimeout(cb, 1000 / 60) }
window.cancelAnimationFrame = window.cancelAnimationFrame || clearTimeout

function animation(ele, data = {}, time = 500, cb) {
  /*
   * ele => 已获取的HTML标签对象
   * data => 需要改变的样式:目标数值 可以带单位
   * time => 改变样式所需要的总时间 单位是毫秒
   * 例如 : animation(box,{width:'1000px',height:'1000px'},5000)
   */
  var startValue = {}
  var changeValue = {}
  var startTime = new Date()
  var eleStart = getStyle(ele)
  for (var key in data) {
    startValue[key] = isNaN(Number.parseFloat(eleStart[key])) ? 0 : Number.parseFloat(eleStart[key])
    changeValue[key] = Number.parseFloat(data[key]) - startValue[key]
  }
  run()
  function run() {
    var nowTime = new Date() - startTime
    var t1 = nowTime / time
    for (var key in changeValue) {
      var val = t1 * changeValue[key] + startValue[key]
      ele.style[key] = val + 'px'
    }
    if (t1 >= 1) {
      cancelAnimationFrame(run)
      cb && cb()
    } else {
      requestAnimationFrame(run)
    }
  }
}