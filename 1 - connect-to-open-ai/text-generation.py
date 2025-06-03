from openai import OpenAI

# from dotenv import load_dotenv
# load_dotenv()
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client  = OpenAI()

# # GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# client  = OpenAI(
#     api_key=GOOGLE_API_KEY,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

response = client.responses.create(
    model='gpt-4o-2024-08-06',
    input = [
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "don't talk like a pirate"
        }
    ],
    stream=True
)
print(response)
for event in response:
    if event.type == 'response.output_text.delta':
        # print(event)
        print(event.delta, end='')

