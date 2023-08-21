# HOW TO USE

# Models

### MPT

Data preparation for MPT follows the same guidelines as [OpenAI uses](https://github.com/openai/openai-python/blob/main/chatml.md).

MPT follows the following structure

`<|im_start|>` notates the start of a message

`<|im_start|>user\n` for a user

`<|im_start|>system\n` for a system prompt ex: "you are an AI programmed to help the user in any way possible"

`<|im_start|>assistant\n` for an assistant

`<|im_end|>` to notate the end of a message

an example conversation converted to this format would be:

```
<|im_start|>system
you are an AI programmed to help a user in any way possible<|im_end|>
<|im_start|>user
What is 1 + 1?<|im_end|>
<|im_start|>assistant
The sum of 1 + 1 is 2.<|im_end|>
```

For training MPT they require that the data is prepared as a jsonl. jsonl is a formatted json type that allows for newline and other characters.
The format for the jsonl itself is as follows

```json lines
{
  "prompt" : "above_mpt_formatted_text",
  "response" : "new_assistant_response"
}
```

The response should be the raw message with no formatting/special tokens.
(with custom special tokens I am unsure if the response should/can contain them. More research on this front is required)

Note that for this to work a question/input from a user must be the final part of the prompt as the AI should never be responding to itself.
An important quirk with jsonl is that it does not require an object wrapping of {} or an array wrapping of []. Instead, it follows as {}{}{}{} where inside each {} is a prompt,response object. No seperator required.

For a working python script for conversion reference: [mpt wiz-vic conversion](mpt/wizard-vicuna/convert.py). In this case wiz-vic is a list of conversations. To convert it into an MPT-trainable set it must first be converted by extracting each individual question/answer and stacking them together until the conversation is complete

```json lines
{
  "prompt" : "question_1",
  "response" : "assistant_response_1"
}
{
  "prompt" : "question_1\nassistant_response_1\nquestion_2",
  "response" : "assistant_response_2"
}
{
  "prompt" : "question_1\nassistant_response_1\nquestion_2\nassistant_response_2\nquestion_3",
  "response" : "assistant_response_3"
}
```

This does create an n<sup>1</sup> issue but according to the developers is intended as such.

