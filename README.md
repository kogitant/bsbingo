# BS Bingo Generator

Developed with claude.ai using Claude 3.5 Sonnet. All python code and requirements.txt provided by Claude. 
README.md and .gitignore created manually, mostly.

You can check out the Claude chat session in [Chat_with_Claude.pdf](Chat_with_Claude.pdf) to see what it took. 
The version control history of this repo also has all the relevant stages documented.

```
python3 -mvenv .env
source .env/bin/activate
pip install --upgrade pip setuptools wheel
xcode-select --install
brew install freetype
pip install --only-binary=:all: reportlab
```

Run unit tests
```
python -m unittest test_main.py
```

Use
```
python main.py example_items.txt 5 output.pdf
```

If you don't want a free square:
```
python main.py example_items.txt 5 output.pdf --no-free
```
