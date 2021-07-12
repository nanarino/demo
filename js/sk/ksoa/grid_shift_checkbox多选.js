function rangeWithoutStart(a, b, step) {  // rangeAll(5,3)-> Array([4])
    var step = step || 1;
    var x = Math.min(a, b), y = Math.max(a, b), rangeArray = new Array;
    for (var i = x + step; i < y; i += step) {
        rangeArray.push(i);
    }
    return rangeArray
}
var beforeMomentIsShiftKey = 0; //上次单击时是否按下shift
var fromRow = -1; //上次单击的行（行号-1）
function gridClick(grid, dssub, col) {
    document.body.click()//调用单击事件
    if (beforeMomentIsShiftKey) {
        if (fromRow + 1) {//将上次单击的行到现在shift的行选中或取消
            var v = dssub.GetValueAt(fromRow, col);
            var rg = rangeWithoutStart(fromRow, grid.CurrentRow - 1);
            for (var i in rg) {
                dssub.SetValueAt(rg[i], col, v);
            }
            dssub.SetValueAt(grid.CurrentRow - 1, col, +!+v);
        }
        beforeMomentIsShiftKey = 0;//重置beforeMomentIsShiftKey变量
    }
    fromRow = grid.CurrentRow - 1;
}
$(function () {//最好复制进onload钩子
    document.body.attachEvent("onclick", function (e) { beforeMomentIsShiftKey = +e.shiftKey });//注册全局单击事件：修改beforeMomentIsShiftKey值
    dssub1.AttachFieldEvent(0, "onclick", "gridClick(SKBILLgrid1,dssub1,'xuanze')");//注册grid的单击事件：修改beforeMomentIsShiftKey值
})
