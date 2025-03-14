#!/usr/bin/env python3
"""
Simple test script for face swapping with ComfyUI and ReActor.
This script helps verify that the ReActor extension is working properly
before pushing to Replicate.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

# Configuration
COMFYUI_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ComfyUI")
INPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_inputs")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_outputs")
WORKFLOW_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reactor_faceswap_workflow.json")

def setup_test_directories():
    """Create test directories if they don't exist."""
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Test directories created: {INPUT_DIR} and {OUTPUT_DIR}")

def check_images():
    """Check if source and target images exist in the input directory."""
    source_path = os.path.join(INPUT_DIR, "source_face.png")
    target_path = os.path.join(INPUT_DIR, "target_image.png")
    
    if not os.path.exists(source_path):
        print(f"Error: Source face image not found at {source_path}")
        print("Please place your source face image in the test_inputs directory and name it 'source_face.png'")
        return False
    
    if not os.path.exists(target_path):
        print(f"Error: Target image not found at {target_path}")
        print("Please place your target image in the test_inputs directory and name it 'target_image.png'")
        return False
    
    print("✅ Found both source and target images")
    return True

def check_reactor_extension():
    """Check if the ReActor extension is installed."""
    reactor_path = os.path.join(COMFYUI_DIR, "custom_nodes", "ComfyUI-ReActor")
    
    if not os.path.exists(reactor_path):
        print(f"Error: ReActor extension not found at {reactor_path}")
        print("The ReActor extension is required for face swapping.")
        return False
    
    print("✅ ReActor extension is installed")
    return True

def check_buffalo_model():
    """Check if the buffalo_l model is available."""
    model_path = os.path.join(COMFYUI_DIR, "models", "insightface", "buffalo_l")
    
    if not os.path.exists(model_path):
        print(f"Warning: buffalo_l model not found at {model_path}")
        print("The model will be downloaded automatically when running ComfyUI,")
        print("but this might cause delays on the first run.")
    else:
        print("✅ buffalo_l model is available")
    
    return True

def copy_images_to_comfyui():
    """Copy test images to ComfyUI's input directory."""
    comfyui_input_dir = os.path.join(COMFYUI_DIR, "input")
    os.makedirs(comfyui_input_dir, exist_ok=True)
    
    source_path = os.path.join(INPUT_DIR, "source_face.png")
    target_path = os.path.join(INPUT_DIR, "target_image.png")
    
    shutil.copy(source_path, os.path.join(comfyui_input_dir, "source_face.png"))
    shutil.copy(target_path, os.path.join(comfyui_input_dir, "target_image.png"))
    
    print(f"✅ Copied images to ComfyUI input directory: {comfyui_input_dir}")
    return True

def main():
    """Main function to test the face swap workflow."""
    print("=== ComfyUI Face Swap Test ===")
    
    # Setup test directories
    setup_test_directories()
    
    # Check if images exist
    if not check_images():
        return False
    
    # Check if ReActor extension is installed
    if not check_reactor_extension():
        return False
    
    # Check if buffalo_l model is available
    check_buffalo_model()
    
    # Copy images to ComfyUI input directory
    copy_images_to_comfyui()
    
    print("\nAll checks passed! You can now:")
    print("1. Start ComfyUI server")
    print("2. Import the workflow from reactor_faceswap_workflow.json")
    print("3. Run the workflow to test face swapping")
    print("4. If everything works, push your model to Replicate")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
