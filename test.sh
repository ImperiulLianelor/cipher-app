#!/bin/bash

# Debug script for test discovery

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print project structure
echo -e "${YELLOW}Project Structure:${NC}"
tree -L 2

# Check Python path
echo -e "\n${YELLOW}Python Path:${NC}"
python3 -c "import sys; print('\n'.join(sys.path))"

# Check test discovery
echo -e "\n${YELLOW}Unittest Discovery:${NC}"
python3 -m unittest discover -v

# Detailed test discovery
echo -e "\n${YELLOW}Detailed Test Discovery:${NC}"
python3 -m unittest discover tests -v
