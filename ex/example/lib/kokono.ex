defmodule Kokono do
  def print99(), do: print(1, 1)
  defp print(_, i) when i > 9, do: 0

  defp print(i, i) do
    IO.puts("#{i} * #{i} = #{i * i}")
    print(1, i + 1)
  end

  defp print(i, j) do
    IO.write("#{i} * #{j} = #{i * j}\t")
    print(i + 1, j)
  end
end
