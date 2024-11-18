defmodule LinkedList do
  # 链表长度
  def len([]), do: 0
  def len([_ | tail]), do: 1 + len(tail)

  # 链表筛选
  def filter([], _), do: []

  def filter([head | tail], f) do
    if f.(head) do
      [head] ++ filter(tail, f)
    else
      filter(tail, f)
    end
  end

  # 链表排序
  def sorted([]), do: []

  def sorted([head | tail]) do
    left = filter(tail, fn n -> n >= head end)
    right = filter(tail, fn n -> n < head end)
    sorted(left) ++ [head] ++ sorted(right)
  end
end
