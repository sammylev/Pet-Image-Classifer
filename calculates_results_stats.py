#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    results_stats_dic = dict()
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0

    results_stats_dic['n_images'] = len(results_dic)
    
    for key,image in results_dic.items():
        #Count how many times image and classifer labels match
        if image[2] == 1:
            results_stats_dic['n_match'] += 1
            #Count how often dog image and classifer labels match
            if image[3] == 1:
                results_stats_dic['n_correct_breed'] += 1
        
        #Count number of dogs
        if image[3] ==1:
            results_stats_dic['n_dogs_img'] += 1
            if image[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        
        #Count the number of not dogs
        if image[3] ==0:
            results_stats_dic['n_notdogs_img'] += 1
            if image[4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
            
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_match'] = calculate_percent(results_stats_dic['n_match'],results_stats_dic['n_images'])
    results_stats_dic['pct_correct_dogs'] = calculate_percent(results_stats_dic['n_correct_dogs'],results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_breed'] = calculate_percent(results_stats_dic['n_correct_breed'], results_stats_dic['n_dogs_img'])
    results_stats_dic['pct_correct_notdogs'] = calculate_percent(results_stats_dic['n_correct_notdogs'],results_stats_dic['n_notdogs_img'])

    return results_stats_dic

def calculate_percent(value, total):
    """
    Calculates the percentage - What % is X of Y
    Parameters:
        Value - Part - X (What % is X of Y)
        Total - Whole - Y (What % is X of Y)
    Returns:
        (float) Percent of value by total
        If total is 0, returns 0
    """
    if total > 0:
        percent = (value / total ) * 100.0
    else:
        percent = 0.0
    
    return percent
