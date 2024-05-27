defmodule Day0Test do
  use ExUnit.Case
  doctest Day0

  test "greets the world" do
    assert Day0.hello() == "world"
  end
end
