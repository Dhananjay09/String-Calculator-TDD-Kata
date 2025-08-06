# String Calculator TDD Kata

This repository contains the implementation of the String Calculator TDD Kata for the Incubyte assessment.

Requirements

- Python 3.8 or higher
- pip

##  Quick Start

### 1. Create virtual Environment
```bash
python3 -m venv venv
```

### 2. Activate the virtual environment:
```bash
source venv/bin/activate
```

### 3. Set up the environment:
```bash
make setup
```

### 4. Run your first test:
```bash
make test
```
TDD Workflow

This project follows Test-Driven Development principles:

TDD Cycle Commands:
```bash
# Run TDD cycle (test, format, lint)
make tdd-cycle

# Run tests with coverage
make coverage
```

Implementation Steps

The String Calculator should handle:

- [ ] Empty string returns 0
- [ ] Single number returns the same number
- [ ] Two numbers return sum of both numbers
- [ ] Multiple numbers return sum of all teh numbers 
- [ ] Newlines as delimiters
- [ ] Custom delimiters
- [ ] Negative numbers throw exceptions
- [ ] Multiple negative numbers show all in exception in a list 

## Available Commands

```bash
make help          # Show all available commands
make setup         # Set up development environment
make install       # Install dependencies
make test          # Run tests
make test-watch    # Run tests in watch mode
make coverage      # Run tests with coverage
make lint          # Run linting
make format        # Format code
make type-check    # Run type checking
make clean         # Clean up generated files
make tdd-cycle     # Run complete TDD cycle
```