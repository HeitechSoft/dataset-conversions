import json

# Load data from dataset.json
with open('dataset.json', 'r') as file:
    data = json.load(file)

# Convert to the desired JSONL format
with open('goat_mpt.jsonl', 'w') as file:
    for item in data:
        new_item = {
            "prompt": "<|im_start|>user\n" + item["instruction"] + "<|im_end|>\n",
            "response": item["output"]
        }
        file.write(json.dumps(new_item) + '\n')

print("Conversion completed!")