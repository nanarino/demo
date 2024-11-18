defmodule Demo do
  defstruct name: nil, id: nil
  # 实现协议
  defimpl String.Chars do
    def to_string(term), do: "<Demo##{term.id} name=#{term.name}>"
  end
end
