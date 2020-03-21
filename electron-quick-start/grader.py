from PIL import Image
import image_slicer
import glob
import numpy as np
from firebase.firebase import FirebaseApplication
from argument import *

print("HELLO WORLD!")

page_images = ["images/page1.jpg", "images/page2.jpg", "images/page3.jpg"]

page_scores = []

page = 0

def grading_page(page_image, page_number):
    correct = 0
    num_of_questions = 4

    def get_average_RGB(image):
        # get image as numpy array
        im = Image.open(image, "r")
        # Generates of list of image RGB values
        pixel_values = list(im.getdata())
        # Cacluates the average of all RGB values for each image
        pixel_values = np.mean(pixel_values)
        # Return average RGB value for each image
        return pixel_values

    # defines first page answer key
    answer_key1 = d1
    # defines second page answer key
    answer_key2 = d2
    # defines third page answer key 
    answer_key3 = d3

    image_list = []
    row_rgb_list = []

    # slices the image into 16 pieces
    initial_tiles1 = image_slicer.slice(page_image, 16, save = False)
    # saves slices into respective files
    image_slicer.save_tiles(initial_tiles1, directory='images/page{}answers'.format(str(int(page_number) + 1)), prefix='slice', format='JPEG')

    for num in range(1, 5):
        # Creates a list of all images that are in each file
        image_list.append(glob.glob("images/page{}answers/slice_0{}_*.jpg".format(str(int(page_number) + 1), str(num))))

    r = 0
    new = []
    for row in image_list:
        for image in row:
            pixel = get_average_RGB(image)
            new.append(pixel)
            r += 1
            if r % 4 == 0:
                row_rgb_list.append(new)
                new = []

    x = 1
    question = 1
    for r in row_rgb_list:
        if question >= 1 and question < 5:
            if r.index(min(r)) == int(answer_key1[str(x)]):
                print("Question {} on this page was answered correctly!".format((str(int(row_rgb_list.index(r)) + 1))))
                correct += 1
            else:
                print("Question {} on this page was answered incorrectly!".format((str(int(row_rgb_list.index(r)) + 1))))
            x += 1
            question +=1 
        elif question == 5:
            correct = 0
            x = 1
            if r.index(min(r)) == int(answer_key2[str(x)]):
                print("Question {} on this page was answered correctly!".format((str(int(row_rgb_list.index(r)) + 1))))
                correct += 1
            else:
                print("Question {} on this page was answered incorrectly!".format((str(int(row_rgb_list.index(r)) + 1))))
            x += 1
            question +=1 
        elif question > 5 and question < 9:
            if r.index(min(r)) == int(answer_key2[str(x)]):
                print("Question {} on this page was answered correctly!".format((str(int(row_rgb_list.index(r)) + 1))))
                correct += 1
            else:
                print("Question {} on this page was answered incorrectly!".format((str(int(row_rgb_list.index(r)) + 1))))
            x += 1
            question +=1 
        elif question == 9:
            correct = 0
            x = 1
            if r.index(min(r)) == int(answer_key3[str(x)]):
                print("Question {} on this page was answered correctly!".format((str(int(row_rgb_list.index(r)) + 1))))
                correct += 1
            else:
                print("Question {} on this page was answered incorrectly!".format((str(int(row_rgb_list.index(r)) + 1))))
            x += 1
            question +=1 
        elif question > 9 and question < 13:
            if r.index(min(r)) == int(answer_key3[str(x)]):
                print("Question {} on this page was answered correctly!".format((str(int(row_rgb_list.index(r)) + 1))))
                correct += 1
            else:
                print("Question {} on this page was answered incorrectly!".format((str(int(row_rgb_list.index(r)) + 1))))
            x += 1
            question +=1 


    score = (correct / int(num_of_questions)) * 100
    
    return score


def result_from_assessment(x):
    return int(sum(x) / len(x))


for page_image in page_images:
    page_scores.append(grading_page(page_image, page))
    page += 1


print(name)
print(quiz)
print(result_from_assessment(page_scores))


app = FirebaseApplication("https://assistant-tomoya.firebaseio.com/", None)
data = {
    "Name": name,
    "Score": result_from_assessment(page_scores)
}
result = app.post("/Grades/Quiz2", data)

print("This student achieved a score of {}% on {}".format(result_from_assessment(page_scores), quiz))
