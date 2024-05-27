defmodule FooTest do
  use ExUnit.Case
  doctest Foo

  test "foo.bar" do
    assert ("world" |> Foo.bar().()) === :false
  end
end
