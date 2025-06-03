import json
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI()


load_dotenv()

problem = """
How to solve - 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Let's say the input is 
Input: nums = [2,7,11,15], target = 9

"""

response = client.responses.create(
    model="gpt-4o-2024-08-06",
    input=[
        {"role": "system", "content": "You are a helpful Leetcode tutor. Guide the user through the solution step by step. The output will have the code and the explanation section will have the explanation for that code."},
        {"role": "user", "content": problem}
    ],
    text = {
        "format": {
            "type": "json_schema",
            "name": "leetcode-cot",
            "schema": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "explanation": { "type": "string"},
                                "output": { "type": "string" }
                            },
                            "required": ["explanation", "output"],
                            "additionalProperties": False
                        },
                    },
                    "final_answer": { "type" : "string"},
                },
                "required": ["steps", "final_answer"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
)

if response.output[0].content[0].type == 'refusal':
    print("Oops the model seems to have refused your request")
else: 
    leetcode_reasoning = json.loads(response.output_text)

    # print(leetcode_reasoning)

    for step in leetcode_reasoning["steps"]:
        print("Output: " + step["output"])
        print("-------------------")
        print("Explanation: " + step["explanation"])
        

        print("\n")
    
    print("Final Answer : " + leetcode_reasoning["final_answer"])






