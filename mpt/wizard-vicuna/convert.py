import json

# Load conversations from JSON file
with open('wizard_vicuna_dataset_unfiltered.json', 'r') as file:
    data = json.load(file)

dataset = []

start = "<|im_start|>"
end = "<|im_end|>"

# Extract conversations and print each sub-object
for item in data:
    conversation_list = item["conversations"]
    previous_human = ""
    full_history = ""
    for conversation in conversation_list:
        if conversation["from"] == "human":
            previous_human = conversation["value"]
            continue
        gpt_response = conversation["value"]
        gpt_response_appended = start + "assistant\n" + gpt_response + end + "\n"
        full_history += start + "user\n" + previous_human + end
        new_object = {"prompt": full_history, "response": gpt_response}
        full_history += gpt_response_appended
        dataset.append(new_object)

with open('wizard_vicuna_mpt.jsonl', 'w') as file:
    i = 0
    for entry in dataset:
        i += 1
        file.write(json.dumps(entry) + '\n')
    print("total values: " + str(i))
