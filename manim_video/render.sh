#!/bin/bash

# HierLoc Manim Render Script
# Renders all scenes to manim_video/output directory
# Usage: ./render.sh [scene_number] [quality]
# Examples:
#   ./render.sh              # Render all scenes (high_quality)
#   ./render.sh 1            # Render Scene 1 only
#   ./render.sh 2 low        # Render Scene 2 with low quality

set -e

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Create output directory if it doesn't exist
mkdir -p output

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
QUALITY="high_quality"
SCENE_NUM="${1:-all}"

# Handle quality argument
if [ "$2" != "" ]; then
    QUALITY="$2"
fi

# Manim command - outputs to manim_video/output via config.py
MANIM_CMD="manim -ql --disable_caching"

# Scene mapping
declare -A SCENES=(
    ["1"]="scenes/scene1_hook.py::Scene1Hook"
    ["2"]="scenes/scene2_problem.py::Scene2Problem"
    ["3"]="scenes/scene3_insight.py::Scene3Insight"
    ["4"]="scenes/scene4_solution.py::Scene4Solution"
    ["5"]="scenes/scene5_results.py::Scene5Results"
)

# Function to render a scene
render_scene() {
    local num=$1
    local scene_file=${SCENES[$num]}

    if [ -z "$scene_file" ]; then
        echo "Error: Scene $num not found"
        return 1
    fi

    echo -e "${BLUE}Rendering Scene $num...${NC}"
    $MANIM_CMD "$scene_file"
    echo -e "${GREEN}✓ Scene $num rendered successfully${NC}"
    echo ""
}

# Render scenes based on argument
if [ "$SCENE_NUM" = "all" ]; then
    echo -e "${BLUE}=== Rendering All HierLoc Scenes ===${NC}"
    echo "Quality: $QUALITY"
    echo "Output: $SCRIPT_DIR/output"
    echo ""

    for scene_num in 1 2 3 4 5; do
        render_scene $scene_num
    done

    echo -e "${GREEN}=== All scenes rendered successfully ===${NC}"
    echo -e "Output files in: ${BLUE}$SCRIPT_DIR/output${NC}"
else
    echo -e "${BLUE}=== Rendering Scene $SCENE_NUM ===${NC}"
    echo "Quality: $QUALITY"
    echo "Output: $SCRIPT_DIR/output"
    echo ""

    render_scene "$SCENE_NUM"
fi
