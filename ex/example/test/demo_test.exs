defmodule DemoTest do
  use ExUnit.Case
  doctest Demo

  test "demo.to_string" do
    demo = %Demo{name: "nanari", id: 1}
    assert "#{demo}" === "<Demo#1 name=nanari>"
  end
end
