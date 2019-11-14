#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#                                                                           
# PROGRAMMER: Sammy Murray
# DATE CREATED: 5/15/2019                                 
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = time()
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)
    
    # Function that converts the filename into a dictionary of pet labels
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)
    
    # Function that uses a given model to classify the name and breed of the images
    classify_images(in_arg.dir, results,in_arg.arch)

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)
    
    # Function that compares the image label and classifer labels to a dog breed list to determine which images are dogs
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)
    
    # Function that calcuates count and percentage of correct identified objectives using results
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # Function that prints the count and percent of correctly identified results using results_stats
    # Function can print out incorrectly identified dogs if fourth argument is true
    # Function can print out incorrectly identified breeds if fifth argument is true
    print_results(results, results_stats, in_arg.arch, True, True)    
    
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    end_time = time()
    tot_time = end_time-start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
