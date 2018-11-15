HUNNIT = "100.png"
SEVENTY = "75.png"
FITY = "50.png"
TWENTY_FIVE = "25.png"

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

def parse_image_location(image_locatin):
    values = [HUNNIT, SEVENTY, FITY, TWENTY_FIVE]
    for value in values:
        index = image_locatin.find(value)
        if index > 0:
            return value[0:len(value)-4]

    
    