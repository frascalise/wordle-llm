# llama3 Solves Wordle

This project uses some LLMs to try and solve the Wordle of the day.

## How it Works

1. **Initial Guess:** LLMs makes an initial guess based on common English words and letter frequencies.
2. **Feedback Incorporation:** The Wordle game provides feedback on the guess (correct letters in the correct position, correct letters in the wrong position, and incorrect letters).
3. **Iterative Refinement:** LLMs (should) use this feedback to refine their subsequent guesses, narrowing down the possibilities until it (hopefully) solves the puzzle.

## Goal

The primary goal of this project is to explore the capabilities of LLMs in a fun way. I aim to see how effectively a large language model can tackle a popular word puzzle and to identify any interesting patterns or strategies that emerge.

## Findings (So Far!)

*(This section can be updated as the project progresses and more data is collected.)*

# llama3:8b

* llama3:8b refuses to use some rarely used letters.
* llama3:8b gets stuck repeating the same words even though explicitly asked not to.
* After a certain number of attempts llama3:8b "forgets" to respond with only one word as explicitly requested.

# deepseek-r1:8b

* deepseek-r1:8b overthinks, lot of words but no facts.
* At some point deepseek-21:8b called itself ChatGPT (was a funny one)

## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -am 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

I appreciate any contributions, whether it's refining the llama3 prompts or adding new analysis tools!
