defmodule ListTest do
  use ExUnit.Case
  doctest LinkedList

  @arr [7, 1, 1, 1, 3, 2, 5]

  # 编译 Integer.is_even/1 宏；也可以import
  require Integer

  test "链表长度" do
    assert LinkedList.len(@arr) === 7
  end

  test "链表筛选" do
    assert LinkedList.filter(@arr, &Integer.is_even/1) == [2]
  end

  test "链表排序" do
    assert LinkedList.sorted(@arr) === [7, 5, 3, 2, 1, 1, 1]
  end
end
