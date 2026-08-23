from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.ai/openai/v1"
)



def create_response(user_input):
    response = client.responses.create(
        model="openai/gpt-oss-20b",
        tools=[
            {}
            ],
        input=user_input
    )
    return response