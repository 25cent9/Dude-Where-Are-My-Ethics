def read_prompts(prompt_number):
    prompt_text_file = open("app/static/prompts/prompt"+str(prompt_number)+"/text.txt")
    prompt_text_list = []
    for line in prompt_text_file:
        prompt_text_list.append(str(line))
    return prompt_text_list


def gather_images(prompt_number):
    root_folder = "../static/prompts/prompt"+str(prompt_number)+"/"
    images = [root_folder+"100.png", root_folder+"75.png", root_folder+"50.png", root_folder+"25.png"]
    return images