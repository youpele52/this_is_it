#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:45:24 2021

@author: michaely
"""


from datetime import datetime
import os
join = os.path.join





def create_prostate_cfgs(main_dir, export_dir, search_term  ):

    todays_date = datetime.now().strftime('%d%m20%y')
    dir_name = main_dir.split('/')[-1]
    
    GtLabels = []
    Channels_t2grase = [] 
    RoiMasks = []
    Channels_t2tse = []
    NamesOfPredictions = []
    Channels_adc = []
    
    
    for patient in os.listdir(main_dir):
        if patient[0] == 'P':
            # print(patient)
            NamesOfPredictions.append('pred_' + patient + '.nii.gz')
            patient_dir = join(main_dir, patient)
            
            for content in os.listdir(patient_dir):
                if search_term in content:
                    if 'Gtlabels_T2TSE' in content:
                        GtLabels.append( join(patient_dir, content)  )   
                    elif 'T2GraSe' in content:
                        Channels_t2grase.append( join(patient_dir, content)  )
                    elif 'ROI_T2TSE' in content:
                        RoiMasks.append( join(patient_dir, content)  )
                    elif 'T2TSE' in content:
                        Channels_t2tse.append( join(patient_dir, content)  )
                    elif content[0] == 'A':
                        Channels_adc.append(  join(patient_dir, content) )
                        
                    
    with open( join(export_dir, dir_name + 'GtLabels'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in GtLabels)       
    
    with open( join(export_dir, dir_name + 'Channels_t2grase'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in Channels_t2grase)    
                    
    with open( join(export_dir, dir_name + 'RoiMasks'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in RoiMasks)                     
    
    with open( join(export_dir, dir_name + 'Channels_t2tse'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in Channels_t2tse)                     
    
    with open( join(export_dir, dir_name + 'NamesOfPredictions'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in NamesOfPredictions)                     
                    
    with open( join(export_dir, dir_name + 'Channels_adc'   + todays_date+ '.cfg' ), 'w' ) as f:
        f.writelines("%s\n" % line for line in Channels_adc)                     
    
    



# Testing

# main_dir = '/home/lenzmi/deepmedic/prostate_risk/data/withoutPIRADS/res_to_T2/test'
# export_dir = '/home/lenzmi/deepmedic/prostate_risk/configFiles/deepMedic/noP_T2TSE+ADC_T2_03032021/test'
# search_term = '03032021'

# create_prostate_cfgs(main_dir, export_dir, search_term )


# # training 
# create_prostate_cfgs(main_dir = '/home/lenzmi/deepmedic/prostate_risk/data/withoutPIRADS/res_to_T2/train', 
#                      export_dir = '/home/lenzmi/deepmedic/prostate_risk/configFiles/deepMedic/noP_T2TSE+ADC_T2_03032021/train', 
#                      search_term  = '03032021')

# # validation
# create_prostate_cfgs(main_dir = '/home/lenzmi/deepmedic/prostate_risk/data/withoutPIRADS/res_to_T2/train/validation', 
#                      export_dir = '/home/lenzmi/deepmedic/prostate_risk/configFiles/deepMedic/noP_T2TSE+ADC_T2_03032021/train/validation', 
#                      search_term  = '03032021')


