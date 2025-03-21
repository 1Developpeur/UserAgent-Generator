# 🎭 User Agent Generator

A powerful Python library that generates realistic User-Agent strings for different browsers and operating systems. This tool helps you simulate various browser environments for testing and development purposes.

## 🌟 Features

- 🔄 Generates realistic User-Agent strings for multiple browsers:
  - Chrome
  - Firefox
  - Edge
- 💻 Supports multiple operating systems:
  - Windows
  - macOS
  - Linux
- 📦 Automatic version detection for latest browser releases
- 💾 Caching system to store browser versions
- 🎲 Random User-Agent generation
- ⚡ Fast and efficient

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## 📋 Requirements

- Python 3.x

## 💡 Usage

```python
from ua import UserAgent

# Initialize the UserAgent generator
ua_generator = UserAgent()

# Generate a single random User-Agent
ua = ua_generator.genUA(amount=1)
print(ua)

# Generate multiple User-Agents
uas = ua_generator.genUA(amount=5)
for ua in uas:
    print(ua)

# Generate User-Agent for specific browser and OS
ua = ua_generator.genUA(amount=1, os='win', browser='chrome')
print(ua)
```

## 🛠️ API Reference

### `genUA(amount=1, os='random', browser='random', version='0')`

Generates User-Agent strings with the following parameters:

- `amount`: Number of User-Agents to generate (default: 1)
- `os`: Operating system ('win', 'mac', 'linux', or 'random')
- `browser`: Browser type ('chrome', 'firefox', 'edge', or 'random')
- `version`: Specific browser version (default: '0' for random)

## 🔄 Browser Version Updates

The library automatically fetches and caches the latest browser versions every 24 hours. The cached versions are stored in `ua_versions.json`.

## ⚠️ Limitations

- Edge browser is not supported on Linux
- Version history for Edge is limited to the latest version
- Requires internet connection for initial setup and version updates

## 🤝 Contributing

Contributions are welcome!

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Browser version data from:
  - Chrome: Google Version History API
  - Firefox: Mozilla Product Details API
  - Edge: Microsoft Edge Updates API

---
Made with ❤️ by [1Developpeur](https://github.com/1Developpeur)
