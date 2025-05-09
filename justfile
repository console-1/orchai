# Justfile for Orchai project

# Task to build the project
build:
    echo "Building the project..."
    # Add build commands here

# Task to deploy the project
deploy:
    echo "Deploying the project..."
    # Add deployment commands here

# Task to generate documentation
generate-docs:
    echo "Generating documentation..."
    # Add commands to generate documentation here

# Task to run tests
test:
    echo "Running tests..."
    pytest

# Task to run linting
lint:
    echo "Running linting..."
    ruff .
