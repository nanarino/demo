defmodule KokonoTest do
  use ExUnit.Case
  doctest Kokono

  test "Kokono.print99" do
    assert Kokono.print99 === 0
  end
end
