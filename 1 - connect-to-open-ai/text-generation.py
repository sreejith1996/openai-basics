from openai import OpenAI

# from dotenv import load_dotenv
# load_dotenv()
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client  = OpenAI()


response = client.responses.create(
    model='gpt-4o',
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

for event in response:
    if event.type == 'response.output_text.delta':
        # print(event)
        print(event.delta, end='')

