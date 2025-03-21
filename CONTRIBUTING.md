# 🤝 Contributing to User Agent Generator

Thank you for your interest in contributing to User Agent Generator! This document provides guidelines and steps for contributing to the project.

## 📋 Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct.

## 🚀 How to Contribute

### 1. Fork the Repository

1. Go to the [User Agent Generator repository](https://github.com/1Developpeur/UserAgent-Generator)
2. Click the "Fork" button in the top right corner
3. Clone your fork locally:
   ```bash
   git clone https://github.com/[YourUsername]/user-agent-generator.git
   cd user-agent-generator
   ```

### 2. Set Up Development Environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Create a Branch

Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 4. Make Your Changes

- Write clear, concise code
- Add comments where necessary
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed

### 5. Commit Your Changes

```bash
git add .
git commit -m "Description of your changes"
```

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select the main branch as the base
4. Add a clear description of your changes
5. Submit the pull request

## 📝 Pull Request Guidelines

- Use a clear and descriptive title
- Provide a detailed description of your changes
- Include any relevant issue numbers
- Add screenshots or GIFs for UI changes
- Ensure all tests pass
- Update documentation as needed

## 🧪 Testing

Before submitting a pull request, ensure all tests pass:
```bash
python -m pytest
```

## 📚 Documentation

- Update the README.md if needed
- Add docstrings to new functions
- Update API documentation
- Add comments for complex logic

## 🔍 Code Review Process

1. Your pull request will be reviewed by maintainers
2. Address any feedback or requested changes
3. Once approved, your changes will be merged

## 📦 Release Process

1. Update version number in setup.py
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Tag the release

## ❓ Questions?

If you have any questions, feel free to:
- Open an issue
- Contact the maintainers
- Join our community discussions

Thank you for contributing to User Agent Generator! 🎉 
