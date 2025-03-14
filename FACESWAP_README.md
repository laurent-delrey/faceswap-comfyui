# High-Quality Face Swap with ComfyUI

This repository contains a modified version of the [cog-comfyui](https://github.com/replicate/cog-comfyui) repository, optimized for high-quality face swapping using the ReActor extension.

## How to Use This Face Swap Workflow

### Step 1: Prepare Your Images
1. Rename your source face image (the person whose face you want to use) to `source_face.png`
2. Rename your target image (the image where you want to swap the face) to `target_image.png`
3. Create a ZIP file containing both images directly (not in a folder)

### Step 2: Run on Replicate
1. Go to [https://replicate.com/your-username/faceswap-comfyui](https://replicate.com/) after you've pushed this model
2. In the workflow field, paste the contents of `reactor_faceswap_workflow.json`
3. Upload your ZIP file containing both images
4. Run the model

### Step 3: Adjust Parameters (Optional)
If you want to fine-tune the face swap results, you can modify these parameters in the workflow JSON:
- `visibility`: Controls how visible the swapped face is (0.0-1.0)
- `face_restore`: Enable/disable face restoration
- `restore_visibility`: Controls the strength of face restoration
- `upscale_factor`: Controls the amount of upscaling
- `upscale_visibility`: Controls the strength of upscaling

## How It Works

This workflow uses the ReActor face swap extension, which leverages InsightFace for high-quality face swapping. The process involves:

1. Loading the source and target images
2. Analyzing faces in both images using the buffalo_l model
3. Swapping the face from the source to the target
4. Applying face restoration to improve quality
5. Upscaling the result for better detail

## Troubleshooting

If you encounter any issues:
- Make sure your images are named exactly `source_face.png` and `target_image.png`
- Ensure your ZIP file doesn't contain any folders
- Check that the face in your source image is clearly visible
- Try different images if the face swap doesn't look good

## Credits

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [ComfyUI-ReActor](https://github.com/Gourieff/ComfyUI-ReActor)
- [InsightFace](https://github.com/deepinsight/insightface)
