import openai
import os

# Set your API key (or use env variable)
openai.api_key = "your-openai-api-key"

def generate_response(objects, prompt):
    object_list = ', '.join([obj['label'] for obj in objects]) if objects else "no recognizable objects"
    input_text = f"The image contains: {object_list}. User prompt: {prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an assistant that describes and explains image contents."},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content.strip()
