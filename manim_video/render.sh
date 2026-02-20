#!/bin/bash

# HierLoc Manim Video Renderer
# Usage: ./render.sh scene1 | ./render.sh all

set -e

# Configuration
QUALITY="h"  # h = high_quality (1080p, 60fps)
OUTPUT_DIR="./output"
SCENES_DIR="./scenes"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Function to render a single scene
render_scene() {
    local scene_file=$1
    local scene_class=$2

    echo "Rendering $scene_class from $scene_file..."
    python -m manim -q "$QUALITY" "$scene_file" "$scene_class"
    echo "Completed: $scene_class"
}

# Function to render all scenes
render_all() {
    echo "Rendering all HierLoc Manim scenes..."

    render_scene "${SCENES_DIR}/scene1_hook.py" "Scene1Hook"
    render_scene "${SCENES_DIR}/scene2_problem.py" "Scene2Problem"
    render_scene "${SCENES_DIR}/scene3_insight.py" "Scene3Insight"
    render_scene "${SCENES_DIR}/scene4_solution.py" "Scene4Solution"
    render_scene "${SCENES_DIR}/scene5_results.py" "Scene5Results"

    echo "All scenes rendered successfully!"
    echo "Output files are in: $OUTPUT_DIR"
}

# Main script logic
if [ $# -eq 0 ]; then
    echo "Usage: $0 [scene1|scene2|scene3|scene4|scene5|all]"
    echo ""
    echo "Examples:"
    echo "  $0 scene1          # Render Scene 1 only"
    echo "  $0 all             # Render all scenes"
    exit 1
fi

case "$1" in
    scene1)
        render_scene "${SCENES_DIR}/scene1_hook.py" "Scene1Hook"
        ;;
    scene2)
        render_scene "${SCENES_DIR}/scene2_problem.py" "Scene2Problem"
        ;;
    scene3)
        render_scene "${SCENES_DIR}/scene3_insight.py" "Scene3Insight"
        ;;
    scene4)
        render_scene "${SCENES_DIR}/scene4_solution.py" "Scene4Solution"
        ;;
    scene5)
        render_scene "${SCENES_DIR}/scene5_results.py" "Scene5Results"
        ;;
    all)
        render_all
        ;;
    *)
        echo "Unknown option: $1"
        echo "Usage: $0 [scene1|scene2|scene3|scene4|scene5|all]"
        exit 1
        ;;
esac
