def read_prompts(prompt_number):
    prompt_text_file = open("app/static/prompts/prompt"+str(prompt_number)+"/text.txt")
    prompt_text_list = []
    for line in prompt_text_file:
        prompt_text_list.append(str(line))
    return prompt_text_list
