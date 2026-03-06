# make24-puzzles

A free, static JSON API serving 404 Make 24 puzzle sets, hosted on GitHub Pages.

**Live API**: https://mrafa3.github.io/make24-puzzles/make24-puzzles.json

## Quick Start

Fetch a random puzzle:

```python
import requests
import random

response = requests.get('https://mrafa3.github.io/make24-puzzles/make24-puzzles.json')
puzzles = response.json()
numbers, solution = random.choice(puzzles)
print(numbers)   # e.g. [1, 1, 1, 8]
```

## Data Format

Each entry is a two-element array: a list of four numbers and a solution expression.

```json
[
  [[1, 1, 1, 8], "(((1 + 1) + 1) * 8)"],
  [[1, 1, 2, 6], "((1 + 1) * (2 * 6))"]
]
```

## Development

To regenerate the puzzle pool from scratch:

```bash
python generate.py
```

## License

MIT
