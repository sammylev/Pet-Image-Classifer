#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Sammy Murray
# DATE CREATED: 5/16/19                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    filename_list = listdir(image_dir);
    results_dic = dict()
    parsed_list = list()
    
    for filename in filename_list:
        if (not(filename.startswith("."))):
            name = ""
            filename_without_ext = filename.split(".")[0]
            all_words = filename_without_ext.split("_")
            for word in all_words:
                if (word.isalpha()):
                    name += word + " "
        final_name = [name.lower().strip()]
        results_dic[filename] = final_name
            
    """
    for filename in filename_list:
        parsed_list = filename.split("_")
        name = str()
        for x in range(len(parsed_list)-1):
            name += str(parsed_list[x]).lower() + " "
        final_list = [name.strip()]
        results_dic[filename] = final_list
    """
    return results_dic
