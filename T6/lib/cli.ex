defmodule AnalyticTableaux.CLI do
  def main([]) do
    IO.read(:stdio, :line) |> run()
  end

  def main(args) do
    [filename | _] = args

    case File.read(filename) do
      {:ok, content} -> run(content)
      {:error, reason} -> IO.puts(:file.format_error(reason))
    end
  end

  def run(content) do
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
