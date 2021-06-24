function rangeAll(a, b, step) {  // rangeAll(5,3)-> Array([3,4,5])
    var step = step || 1;
    var x = Math.min(a, b), y = Math.max(a, b), rangeArray = new Array;
    for (var i = x; i <= y; i += step) {
        rangeArray.push(i);
    }
    return rangeArray
}
var beforeMomentIsShiftKey = 0; //上次单击时是否按下shift
var fromRow = 0; //上次单击的行
function gridClick(grid) {
    document.body.click()//调用单击事件
    if (beforeMomentIsShiftKey) {
        if (fromRow && grid.CurrentRow) {//将上次单击的行到现在shift的行选中或取消
            var v = grid.Marked(fromRow);
            var rg = rangeAll(fromRow, grid.CurrentRow);
            for (var i in rg) {
                grid.Marked(rg[i]) = v;
            }
        }
        beforeMomentIsShiftKey = 0;//重置beforeMomentIsShiftKey变量
    } else {
        grid.Marked(grid.CurrentRow) = !grid.Marked(grid.CurrentRow);//普通单击选中
    }
    fromRow = grid.CurrentRow;
}
$(function () {
    document.body.attachEvent("onclick", function (e) { beforeMomentIsShiftKey = +e.shiftKey });//注册全局单击事件：修改beforeMomentIsShiftKey值
    dssub1.AttachFieldEvent(-1, "onclick", 'gridClick(SKBILLgrid1)');//注册grid的单击事件：修改beforeMomentIsShiftKey值
})