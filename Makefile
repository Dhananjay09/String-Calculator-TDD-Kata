.PHONY: help install test test-watch coverage lint format type-check clean setup

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Set up the development environment
	python -m venv venv
	. venv/bin/activate && pip install -e .[dev]
	pre-commit install

install: ## Install dependencies
	pip install -e .[dev]

test: ## Run tests
	pytest

test-watch: ## Run tests in watch mode
	ptw

coverage: ## Run tests with coverage report
	pytest --cov=src --cov-report=html --cov-report=term-missing

lint: ## Run linting
	flake8 src/ tests/
	black --check src/ tests/
	isort --check-only src/ tests/

format: ## Format code
	black src/ tests/
	isort src/ tests/

type-check: ## Run type checking
	mypy src/

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/

tdd-cycle: ## Run TDD cycle (test, format, lint)
	@echo "�� Running tests..."
	@pytest -v
	@echo "🎨 Formatting code..."
	@black src/ tests/
	@echo "�� Linting code..."
	@flake8 src/ tests/
	@echo "✅ TDD cycle complete!" 