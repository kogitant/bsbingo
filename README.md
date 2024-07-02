# BS Bingo Generator
Developed with claude.ai using Claude 3.5 Sonnet
```
python3 -mvenv .env
source .env/bin/activate
pip install --upgrade pip setuptools wheel
xcode-select --install
brew install freetype
pip install --only-binary=:all: reportlab
```

Use
```
python main.py items.txt 5 output.pdf
```
