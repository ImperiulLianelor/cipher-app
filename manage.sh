#!/bin/bash

# Cipher CLI Project Management Script

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print help
print_help() {
    echo -e "${YELLOW}Cipher CLI Management Script${NC}"
    echo "Usage:"
    echo "  ./manage.sh [command]"
    echo ""
    echo "Commands:"
    echo "  setup       - Create virtual environment and install dependencies"
    echo "  test        - Run all unit tests"
    echo "  demo        - Run demonstration script"
    echo "  clean       - Remove build and cache files"
    echo "  help        - Show this help message"
}

# Create virtual environment and install dependencies
setup() {
    echo -e "${GREEN}Setting up virtual environment...${NC}"
    python3 -m venv venv
    source venv/bin/activate
    pip install -e .
    pip install pytest
    echo -e "${GREEN}Setup complete!${NC}"
}

# Run tests
run_tests() {
    echo -e "${GREEN}Running unit tests...${NC}"
    python3 -m pytest tests/
}

# Run demo script
run_demo() {
    echo -e "${GREEN}Running demonstration script...${NC}"
    python3 samples/demo.py
}

# Clean up build files
clean() {
    echo -e "${GREEN}Cleaning up...${NC}"
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete
    find . -type f -name "*.pyd" -delete
    rm -rf build/
    rm -rf dist/
    rm -rf *.egg-info
    echo -e "${GREEN}Cleanup complete!${NC}"
}

# Main script logic
case "$1" in
    setup)
        setup
        ;;
    test)
        run_tests
        ;;
    demo)
        run_demo
        ;;
    clean)
        clean
        ;;
    help)
        print_help
        ;;
    *)
        echo -e "${YELLOW}Invalid command. Use 'help' to see available commands.${NC}"
        exit 1
        ;;
esac

exit 0

