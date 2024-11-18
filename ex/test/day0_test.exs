defmodule Day0Test do
  use ExUnit.Case
  doctest Day0

  test "你好世界" do
    assert Day0.hello() === "world"
  end

  test "输出乘法表" do
    assert Day0.print99() === 0
  end

  test "返回匿名函数" do
    assert Day0.is_atom().("world") === false
  end
end
