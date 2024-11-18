defmodule StructTest do
  use ExUnit.Case
  doctest Demo

  test "实现协议" do
    demo = %Demo{name: "nanari", id: 1}
    assert "#{demo}" === "<Demo#1 name=nanari>"
  end
end
