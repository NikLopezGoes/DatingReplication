import pandas as pd

df = pd.read_csv("user_data.csv")

# Display the first few rows
print(df.head())

df.info()

# Summary statistics
print(df.describe())


#TODO
'''
We need to determine what categories are relevant for our system
Below I have listed all of the categories in the dataset. Some of the names are not clear tho
'''
Categories (columns) in the dataset (there are 141 columns):
['Unnamed: 0', 'caseid_new', 'weight1', 'weight2',
 'ppage', 'ppagecat', 'ppagect4', 'ppeduc', 'ppeducat', 'ppethm', 
 'ppgender', 'pphhhead', 'pphouseholdsize', 'pphouse', 'ppincimp', 
 'hhinc', 'ppmarit', 'ppmsacat', 'ppreg4', 'ppreg9', 'pprent', 'ppt01', 
 'ppt1317', 'ppt18ov', 'ppt25', 'ppt612', 'children_in_hh', 'ppwork', 'ppnet', 
 'ppq14arace', 'pphispan', 'pprace_white', 'pprace_black', 'pprace_nativeamerican', 
 'pprace_asianindian', 'pprace_chinese', 'pprace_filipino', 'pprace_japanese', 'pprace_korean', 
 'pprace_vietnamese', 'pprace_otherasian', 'pprace_hawaiian', 'pprace_guamanian', 'pprace_samoan',
  'pprace_otherpacificislander', 'pprace_someotherrace', 'papglb_friend', 'pppartyid3', 'papevangelical', 
  'papreligion', 'ppppcmdate_yrmo', 'pppadate_yrmo', 'pphhcomp11_member2_age', 'pphhcomp11_member3_age', 
  'pphhcomp11_member4_age', 'pphhcomp11_member5_age', 'pphhcomp11_member6_age', 'pphhcomp11_member7_age', 
  'pphhcomp11_member8_age', 'pphhcomp11_member9_age', 'pphhcomp11_member10_age', 'pphhcomp11_member11_age', 'pphhcomp11_member12_age',
   'pphhcomp11_member13_age', 'pphhcomp11_member14_age', 'pphhcomp11_member15_age', 'pphhcomp11_member2_gender', 
   'pphhcomp11_member3_gender', 'pphhcomp11_member4_gender', 'pphhcomp11_member5_gender', 'pphhcomp11_member6_gender', 
   'pphhcomp11_member7_gender', 'pphhcomp11_member8_gender', 'pphhcomp11_member9_gender', 'pphhcomp11_member10_gender', 
   'pphhcomp11_member11_gender', 'pphhcomp11_member12_gender', 'pphhcomp11_member13_gender', 'pphhcomp11_member14_gender', 
   'pphhcomp11_member15_gender', 'pphhcomp11_member2_relationship', 'pphhcomp11_member3_relationship', 'pphhcomp11_member4_relationship', 
   'pphhcomp11_member5_relationship', 'pphhcomp11_member6_relationship', 'pphhcomp11_member7_relationship', 
   'pphhcomp11_member8_relationship', 'pphhcomp11_member9_relationship', 'pphhcomp11_member10_relationship', 
   'pphhcomp11_member11_relationship', 'pphhcomp11_member12_relationship', 'pphhcomp11_member13_relationship', 
   'pphhcomp11_member14_relationship', 'pphhcomp11_member15_relationship', 'irb_consent', 'weight3', 'weight4',
    'weight5', 'weight6', 'weight7', 'weight_couples_coresident', 'HCMST_main_interview_yrmo', 'duration', 'qflag', 
    'glbstatus', 'papglb_status', 'recsource', 's1', 's1a', 's2', 'q3_codes', 'q4', 'q5', 'q6a', 'q6b', 'q7a', 'q7b', 
    'q8a', 'q8b', 'q9', 'q10', 'q11', 'q12', 'q13a', 'q13b', 'q14', 'q15a1_compressed', 'q16', 'q17a', 'q17b', 'q17c',
     'q17d', 'gender_attraction', 'q18a_1', 'q18a_2', 'q18a_3', 'q18a_refused', 'q18b_codes', 'q18c_codes', 'q19', 'q20', 
     'q21a', 'q21a_refusal', 'q21b', 'q21b_refusal', 'q21c', 'q21c_refusal', 'q21d', 'q21d_refusal', 'q21e', 'q21e_refusal', 
     'q22', 'q23', 'q24_codes', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31_1', 'q31_2', 'q31_3', 'q31_4', 'q31_5', 'q31_6', 
     'q31_7', 'q31_8', 'q31_9', 'q31_other_text_entered', 'q32', 'q33_1', 'q33_2', 'q33_3', 'q33_4', 'q33_5', 'q33_6', 'q33_7', 
     'q33_other_text_entered', 'q34', 'q35_codes', 'q35_text_entered', 'q24_met_online', 'summary_q24_total', 'q24_R_cowork', 
     'q24_R_friend', 'q24_R_family', 'q24_R_sig_other', 'q24_R_neighbor', 'q24_P_cowork', 'q24_P_friend', 'q24_P_family', 
     'q24_P_sig_other', 'q24_P_neighbor', 'q24_btwn_I_cowork', 'q24_btwn_I_friend', 'q24_btwn_I_family', 'q24_btwn_I_sig_other',
     'q24_btwn_I_neighbor', 'q24_school', 'q24_college', 'q24_military', 'q24_church', 'q24_vol_org', 'q24_customer',
      'q24_bar_restaurant', 'q24_internet_dating', 'q24_internet_social_networking', 'q24_internet_game', 'q24_internet_chat', 
      'q24_internet_community', 'q24_internet_other', 'q24_public', 'q24_private_party', 'q24_blind_date', 'q24_vacation', 
      'q24_singles_service_non_internet', 'q24_business_trip', 'q24_work_neighbor', 'q24_fam_sister_active', 'q24_fam_brother_active',
       'q24_fam_mother_active', 'q24_fam_father_active', 'q24_fam_other_active', 'q24_fam_cousins_active', 'q24_fam_aunt_niece_active', 
       'q24_fam_uncle_nephew_active', 'q24_fam_grandmother_active', 'q24_fam_grandfather_active', 'q24_fam_sister_passive',
        'q24_fam_brother_passive', 'q24_fam_mother_passive', 'q24_fam_father_passive', 'q24_fam_other_passive',
         'q24_fam_cousins_passive', 'q24_fam_aunt_niece_passive', 'q24_fam_uncle_nephew_passive', 'q24_fam_grandmother_passive', 
         'q24_fam_grandfather_passive', 'q24_fam_female', 'q24_fam_male', 'distancemoved_10mi', 'marrynotreally', 'marrycountry',
          'civilnotreally', 'partner_deceased', 'partner_religion_reclassified', 'partner_religion_child_reclass', 
          'own_religion_child_reclass', 'q32_internet', 'how_met_online', 'either_internet', 'either_internet_adjusted', 
          'same_sex_couple', 'potential_partner_gender_recodes', 'alt_partner_gender', 'how_long_ago_first_met', 
          'how_long_ago_first_romantic', 'how_long_ago_first_cohab', 'how_long_ago_first_met_cat', 'how_long_ad', 'pp3_pphhsize',
           'pp3_pphouse', 'pp3_ppincimp', 'pp3_ppmarit', 'pp3_ppmsacat', 'pp3_pprent', 'pp3_ppreg4', 'pp3_ppreg9', 
           'interstate_mover_pp1_pp2', 'interstate_mover_pp2_pp3', 'interstate_mover_pp1_pp3', 'pp3_ppt01', 'pp3_ppt1317',
            'pp3_ppt18ov', 'pp3_ppt25', 'pp3_ppt612', 'pp3_ppwork', 'pp3_ppnet', 'pp3_ppcmdate_yrmo', 'pp3_ppeduc', 'pp3_ppeducat', 
            'pp3_respondent_yrsed', 'pp3_ppethm', 'pp3_newer', 'w2w3_combo_breakup', 'w3_broke_up', 'w3_xpartnered', 'w3_xdeceased',
             'w3_multiname', 'w3_xss', 'w3_xlast', 'w3_xyear', 'w3_xmonth', 'w3_xqualified', 'w3_status', 'w3_complete', 'w3_source', 
             'w3_HCMST_interview_fin_yrmo', 'w3_days_elapsed', 'w3_duration', 'w3_xmarry', 'w3_xtype', 'w3_q1', 'w3_q2', 'w3_q3',
              'w3_q4', 'w3_mbtiming_year', 'w3_mbtiming_month', 'w3_q5', 'w3_q6', 'w3_q7', 'w3_q8', 'w3_q9', 'w3_q10',
              'w3_nonmbtiming_year', 'w3_nonmbtiming_month']
'''
print("Categories (columns) in the dataset:")
print(df.columns.tolist())