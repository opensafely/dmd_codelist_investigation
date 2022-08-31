from cohortextractor import codelist_from_csv
dict_codelists = {
'opensafely_asthma_inhaler_steroid_medication': codelist_from_csv(
        'codelists/opensafely-asthma-inhaler-steroid-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_asthma_inhaler_steroid_medication_new': codelist_from_csv(
        'codelists/opensafely-asthma-inhaler-steroid-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_first_generation_antipsychotics_excluding_long_acting_depots_dmd': codelist_from_csv(
        'codelists/opensafely-first-generation-antipsychotics-excluding-long-acting-depots-dmd.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_first_generation_antipsychotics_excluding_long_acting_depots_dmd_new': codelist_from_csv(
        'codelists/opensafely-first-generation-antipsychotics-excluding-long-acting-depots-dmd_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_indometacin': codelist_from_csv(
        'codelists/opensafely-indometacin.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_indometacin_new': codelist_from_csv(
        'codelists/opensafely-indometacin_new.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_azithromycin_medication': codelist_from_csv(
        'codelists/opensafely-azithromycin-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_azithromycin_medication_new': codelist_from_csv(
        'codelists/opensafely-azithromycin-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_angiotensin_ii_receptor_blockers_arbs': codelist_from_csv(
        'codelists/opensafely-angiotensin-ii-receptor-blockers-arbs.csv',
        system='snomed',
        column='id'
        ),
'opensafely_angiotensin_ii_receptor_blockers_arbs_new': codelist_from_csv(
        'codelists/opensafely-angiotensin-ii-receptor-blockers-arbs_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_alpha_adrenoceptor_blocking_drugs': codelist_from_csv(
        'codelists/opensafely-alpha-adrenoceptor-blocking-drugs.csv',
        system='snomed',
        column='id'
        ),
'opensafely_alpha_adrenoceptor_blocking_drugs_new': codelist_from_csv(
        'codelists/opensafely-alpha-adrenoceptor-blocking-drugs_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_thiazide_type_diuretic_medication': codelist_from_csv(
        'codelists/opensafely-thiazide-type-diuretic-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_thiazide_type_diuretic_medication_new': codelist_from_csv(
        'codelists/opensafely-thiazide-type-diuretic-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_selective_serotonin_reuptake_inhibitors_dmd': codelist_from_csv(
        'codelists/opensafely-selective-serotonin-reuptake-inhibitors-dmd.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_selective_serotonin_reuptake_inhibitors_dmd_new': codelist_from_csv(
        'codelists/opensafely-selective-serotonin-reuptake-inhibitors-dmd_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_combination_blood_pressure_medication': codelist_from_csv(
        'codelists/opensafely-combination-blood-pressure-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_combination_blood_pressure_medication_new': codelist_from_csv(
        'codelists/opensafely-combination-blood-pressure-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_second_generation_antipsychotics_excluding_long_acting_injections': codelist_from_csv(
        'codelists/opensafely-second-generation-antipsychotics-excluding-long-acting-injections.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_second_generation_antipsychotics_excluding_long_acting_injections_new': codelist_from_csv(
        'codelists/opensafely-second-generation-antipsychotics-excluding-long-acting-injections_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_insulin_medication': codelist_from_csv(
        'codelists/opensafely-insulin-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_insulin_medication_new': codelist_from_csv(
        'codelists/opensafely-insulin-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_high_dose_multiple_ingredient_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-high-dose-multiple-ingredient-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_high_dose_multiple_ingredient_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-high-dose-multiple-ingredient-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_laba_ics_combination_inhaler': codelist_from_csv(
        'codelists/opensafely-laba-ics-combination-inhaler.csv',
        system='snomed',
        column='id'
        ),
'opensafely_laba_ics_combination_inhaler_new': codelist_from_csv(
        'codelists/opensafely-laba-ics-combination-inhaler_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_proton_pump_inhibitors_ppi_oral': codelist_from_csv(
        'codelists/opensafely-proton-pump-inhibitors-ppi-oral.csv',
        system='snomed',
        column='id'
        ),
'opensafely_proton_pump_inhibitors_ppi_oral_new': codelist_from_csv(
        'codelists/opensafely-proton-pump-inhibitors-ppi-oral_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_ibuprofen_oral': codelist_from_csv(
        'codelists/opensafely-ibuprofen-oral.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_ibuprofen_oral_new': codelist_from_csv(
        'codelists/opensafely-ibuprofen-oral_new.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_nebulised_asthma_and_copd_medications': codelist_from_csv(
        'codelists/opensafely-nebulised-asthma-and-copd-medications.csv',
        system='snomed',
        column='id'
        ),
'opensafely_nebulised_asthma_and_copd_medications_new': codelist_from_csv(
        'codelists/opensafely-nebulised-asthma-and-copd-medications_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_influenza_vaccination': codelist_from_csv(
        'codelists/opensafely-influenza-vaccination.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_influenza_vaccination_new': codelist_from_csv(
        'codelists/opensafely-influenza-vaccination_new.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_high_dose_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-high-dose-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_high_dose_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-high-dose-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_aspirin': codelist_from_csv(
        'codelists/opensafely-aspirin.csv',
        system='snomed',
        column='id'
        ),
'opensafely_aspirin_new': codelist_from_csv(
        'codelists/opensafely-aspirin_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_calcium_channel_blockers': codelist_from_csv(
        'codelists/opensafely-calcium-channel-blockers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_calcium_channel_blockers_new': codelist_from_csv(
        'codelists/opensafely-calcium-channel-blockers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_antidiabetic_drugs': codelist_from_csv(
        'codelists/opensafely-antidiabetic-drugs.csv',
        system='snomed',
        column='id'
        ),
'opensafely_antidiabetic_drugs_new': codelist_from_csv(
        'codelists/opensafely-antidiabetic-drugs_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_beta_blocker_medications': codelist_from_csv(
        'codelists/opensafely-beta-blocker-medications.csv',
        system='snomed',
        column='id'
        ),
'opensafely_beta_blocker_medications_new': codelist_from_csv(
        'codelists/opensafely-beta-blocker-medications_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_asthma_inhaler_salbutamol_medication': codelist_from_csv(
        'codelists/opensafely-asthma-inhaler-salbutamol-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_asthma_inhaler_salbutamol_medication_new': codelist_from_csv(
        'codelists/opensafely-asthma-inhaler-salbutamol-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_ace_inhibitor_medications': codelist_from_csv(
        'codelists/opensafely-ace-inhibitor-medications.csv',
        system='snomed',
        column='id'
        ),
'opensafely_ace_inhibitor_medications_new': codelist_from_csv(
        'codelists/opensafely-ace-inhibitor-medications_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_sama_medication': codelist_from_csv(
        'codelists/opensafely-sama-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_sama_medication_new': codelist_from_csv(
        'codelists/opensafely-sama-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_single_ingredient_laba_inhalers': codelist_from_csv(
        'codelists/opensafely-single-ingredient-laba-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_single_ingredient_laba_inhalers_new': codelist_from_csv(
        'codelists/opensafely-single-ingredient-laba-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_levothyroxine': codelist_from_csv(
        'codelists/opensafely-levothyroxine.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_levothyroxine_new': codelist_from_csv(
        'codelists/opensafely-levothyroxine_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_antihistamines_oral': codelist_from_csv(
        'codelists/opensafely-antihistamines-oral.csv',
        system='snomed',
        column='id'
        ),
'opensafely_antihistamines_oral_new': codelist_from_csv(
        'codelists/opensafely-antihistamines-oral_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_antiplatelets': codelist_from_csv(
        'codelists/opensafely-antiplatelets.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_antiplatelets_new': codelist_from_csv(
        'codelists/opensafely-antiplatelets_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_oestrogen_and_oestrogen_like_drugs': codelist_from_csv(
        'codelists/opensafely-oestrogen-and-oestrogen-like-drugs.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_oestrogen_and_oestrogen_like_drugs_new': codelist_from_csv(
        'codelists/opensafely-oestrogen-and-oestrogen-like-drugs_new.csv',
        system='snomed',
        column='dmd_id'
        ),
'opensafely_nsaids_oral': codelist_from_csv(
        'codelists/opensafely-nsaids-oral.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_nsaids_oral_new': codelist_from_csv(
        'codelists/opensafely-nsaids-oral_new.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_high_dose_single_ingredient_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-high-dose-single-ingredient-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_high_dose_single_ingredient_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-high-dose-single-ingredient-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_statin_medication': codelist_from_csv(
        'codelists/opensafely-statin-medication.csv',
        system='snomed',
        column='id'
        ),
'opensafely_statin_medication_new': codelist_from_csv(
        'codelists/opensafely-statin-medication_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_dmards': codelist_from_csv(
        'codelists/opensafely-dmards.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_dmards_new': codelist_from_csv(
        'codelists/opensafely-dmards_new.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_single_ingredient_ics': codelist_from_csv(
        'codelists/opensafely-single-ingredient-ics.csv',
        system='snomed',
        column='id'
        ),
'opensafely_single_ingredient_ics_new': codelist_from_csv(
        'codelists/opensafely-single-ingredient-ics_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_single_ingredient_lama_inhalers': codelist_from_csv(
        'codelists/opensafely-single-ingredient-lama-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_single_ingredient_lama_inhalers_new': codelist_from_csv(
        'codelists/opensafely-single-ingredient-lama-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_single_ingredient_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-single-ingredient-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_single_ingredient_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-single-ingredient-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_multiple_ingredient_ics_inhalers': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-multiple-ingredient-ics-inhalers.csv',
        system='snomed',
        column='id'
        ),
'opensafely_low_and_medium_dose_multiple_ingredient_ics_inhalers_new': codelist_from_csv(
        'codelists/opensafely-low-and-medium-dose-multiple-ingredient-ics-inhalers_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_saba_inhaler_medications': codelist_from_csv(
        'codelists/opensafely-saba-inhaler-medications.csv',
        system='snomed',
        column='id'
        ),
'opensafely_saba_inhaler_medications_new': codelist_from_csv(
        'codelists/opensafely-saba-inhaler-medications_new.csv',
        system='snomed',
        column='id'
        ),
'opensafely_asthma_oral_prednisolone_medication': codelist_from_csv(
        'codelists/opensafely-asthma-oral-prednisolone-medication.csv',
        system='snomed',
        column='snomed_id'
        ),
'opensafely_asthma_oral_prednisolone_medication_new': codelist_from_csv(
        'codelists/opensafely-asthma-oral-prednisolone-medication_new.csv',
        system='snomed',
        column='snomed_id'
        ),
}
