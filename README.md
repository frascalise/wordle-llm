# llama3 Solves Wordle

This project uses llama3:8b to try and solve the Wordle of the day.

## How it Works

The project leverages the power of llama3, a large language model, to play Wordle. Here's a simplified overview of the process:

1. **Initial Guess:** llama3 makes an initial guess based on common English words and letter frequencies.
2. **Feedback Incorporation:** The Wordle game provides feedback on the guess (correct letters in the correct position, correct letters in the wrong position, and incorrect letters).
3. **Iterative Refinement:** llama3 uses this feedback to refine its subsequent guesses, narrowing down the possibilities until it (hopefully) solves the puzzle.

## Goal

The primary goal of this project is to explore the capabilities of llama3 in a fun way. I aim to see how effectively a large language model can tackle a popular word puzzle and to identify any interesting patterns or strategies that emerge.

## Findings (So Far!)

*(This section can be updated as the project progresses and more data is collected.)*

* llama3 refuses to use some rarely used letters.
* llama3 gets stuck repeating the same words even though explicitly asked not to.
* After a certain number of attempts llama3 "forgets" to respond with only one word as explicitly requested.

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -am 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

I appreciate any contributions, whether it's refining the llama3 prompts or adding new analysis tools!
