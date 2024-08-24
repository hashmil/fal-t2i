import gradio as gr
import fal_client
from PIL import Image
import requests
from io import BytesIO
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
fal_key = os.getenv("FAL_KEY")
if not fal_key:
    raise ValueError("FAL_KEY not found in environment variables. Please check your .env file.")

def generate_image(model, prompt, image_size, num_inference_steps, seed, guidance_scale, num_images, enable_safety_checker):
    handler = fal_client.submit(
        model,
        arguments={
            "prompt": prompt,
            "image_size": image_size,
            "num_inference_steps": num_inference_steps,
            "seed": seed if seed != -1 else None,  # Use None if seed is -1 (random)
            "guidance_scale": guidance_scale,
            "num_images": num_images,
            "enable_safety_checker": enable_safety_checker
        },
    )
    
    result = handler.get()
    
    # Get the URL of the first generated image
    image_url = result['images'][0]['url']
    
    # Download the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    return image, f"Image generated successfully. Seed: {result.get('seed', 'N/A')}"

with gr.Blocks() as demo:
    gr.Markdown("# Text-to-Image Generator")
    with gr.Row():
        with gr.Column():
            model_choice = gr.Dropdown([
                "fal-ai/flux-realism",
                "fal-ai/aura-flow",
                "fal-ai/flux/dev",
                "fal-ai/flux/schnell",
                "fal-ai/flux-pro",
                "fal-ai/fast-sdxl",
                "fal-ai/stable-diffusion-v3-medium"
            ], label="Model", value="fal-ai/flux-realism")
            prompt_input = gr.Textbox(label="Enter your prompt", lines=5)
            image_size = gr.Dropdown(["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"], 
                                     label="Image Size", value="landscape_4_3")
            num_inference_steps = gr.Slider(minimum=1, maximum=50, value=28, step=1, label="Number of Inference Steps")
            seed = gr.Number(label="Seed (-1 for random)", value=-1)
            guidance_scale = gr.Slider(minimum=1, maximum=20, value=3.5, step=0.1, label="Guidance Scale")
            num_images = gr.Slider(minimum=1, maximum=4, value=1, step=1, label="Number of Images")
            enable_safety_checker = gr.Checkbox(label="Enable Safety Checker", value=True)
            submit_button = gr.Button("Generate Image")
        with gr.Column():
            image_output = gr.Image(label="Generated Image")
            log_output = gr.Textbox(label="Status", lines=2)
    
    submit_button.click(
        fn=generate_image,
        inputs=[model_choice, prompt_input, image_size, num_inference_steps, seed, guidance_scale, num_images, enable_safety_checker],
        outputs=[image_output, log_output],
    )

if __name__ == "__main__":
    demo.launch()