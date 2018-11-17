HUNNIT = "100.png"
SEVENTY = "75.png"
FITY = "50.png"
TWENTY_FIVE = "25.png"

_MG = "MG"
_MB = "MB"
_N = "N"

def read_prompts(prompt_number):
    if prompt_number == 0:
        prompt_number = 1
    prompt_text_file = open("app/static/prompts/prompt"+str(prompt_number)+"/text.txt")
    prompt_text_list = []
    for line in prompt_text_file:
        prompt_text_list.append(str(line))
    return prompt_text_list

def find_moral_results(moral_score=25):
    average_moral_score = int(moral_score/15)
    average_moral_state = None
    if average_moral_score >= 75:
        average_moral_state = _MG
    elif average_moral_score >= 50:
        average_moral_state = _N
    else:
        average_moral_state = _MB
    result_image = "../static/img/"+average_moral_state+".png"
    if average_moral_state is _MB:
        average_moral_state = "Morally Bad"
    elif average_moral_state is _MG:
        average_moral_state = "Morally Good"
    else:
        average_moral_state = "Neutral"
    return average_moral_score, average_moral_state, result_image


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

    
    