# How To Run

First create a `.env` file with a `GEMINI_API_KEY`.
You can get a key from [Google AI Studio](https://aistudio.google.com/)

```bash
uv run main.py "[your prompt here]"
```

## Extending the Project

You've completed the required steps, but have some fun with it! (Carefully, though... be very cautious about giving an LLM access to your filesystem and Python interpreter.) See if you can get it to:

- Fix harder and more complex bugs
- Refactor sections of code
- Add entirely new features
- Improve this README.md

You can also try:

- Other LLM providers
- Other Gemini models
- Giving it more functions to call
- Other codebases (commit your changes before running the agent on a codebase, so you can always revert)

> _Remember, what we've built is a toy version of something like Cursor/Zed's Agentic Mode, or Claude Code. Even their tools aren't perfectly secure, so be careful what you give them access to. And don't encourage anyone to use this toy agent as-is!_
