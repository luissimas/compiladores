defmodule AnalyticTableaux.CLI do
  def main(args \\ []) do
    [content | _] = args

    case Tableaux.prove(content) do
      {:valid, []} -> IO.puts("Argumento válido!")
      {:invalid, counterexample} ->
        IO.puts("Argumento inválido, contraexemplo:")
        IO.inspect(counterexample)
    end
  end
end
