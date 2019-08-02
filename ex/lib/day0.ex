defmodule Day0 do
  # 你好世界
  def hello, do: "world"

  # 输出乘法表
  def print99(), do: print1(1, 1)
  defp print1(_, i) when i > 9, do: 0

  defp print1(i, i) do
    IO.puts("#{i} * #{i} = #{i * i}")
    print1(1, i + 1)
  end

  defp print1(i, j) do
    IO.write("#{i} * #{j} = #{i * j}\t")
    print1(i + 1, j)
  end

  # 返回匿名函数
  def is_atom do
    &is_atom/1
  end
end
