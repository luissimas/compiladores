defmodule AnalyticTableaux.CLI do
  def main(args \\ []) do
    [content | _] = args

    case Tableaux.prove(content) do
      {:error, reason} ->
        IO.puts(reason)

      {:valid, []} ->
        IO.puts("valid argument")

      {:invalid, counterexample} ->
        IO.puts("invalid argument, counterexample:")
        IO.inspect(counterexample)
    end
  end
end
