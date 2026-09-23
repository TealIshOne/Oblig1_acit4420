from sample_data import resting, moderate_activity ,high_activity, recovery, poor_quality
from main import Participant as part
from main import Observation as obs
from main import SessionsStorage as sesSt
from main import sessionMath as sesMat


def testing_individual_classes():
    print("="*65)
    print(" "*20,"TESTING INDIVIDUAL CLASSES")
    print("="*65)

    # test class1: Participant
    profile, data =resting()
    p=part.instanciate_profile(profile)
    print(f"[Participant] ID: {p.ID:<5} | HR: {p.Baseline_HR:<5} | Skin: {p.Baseline_Skin:<5} | Temp: {p.Baseline_Temp:<5}")

    #test Class 2: Observation
    o=obs(data)
    invalid,valid = o.isValid()
    print(f"[Observation] Valid entries: {len(valid)} | Invalid entries: {len(invalid):<25}")
    print(f"[Observation] ValidType check passed: {o.ValidateType():<5}")

    # test Class 3: SessionStorage
    storage=sesSt(data, data, data)
    inv_rec, val_rec=storage.ValidateAll()
    print(f"[SessionStorage] sessions processed. valid sessions {len(val_rec)} | invalid sessions {len(inv_rec)}")

    print("-"*23,"end of base tests", "-"*23)

def run_scenarios(scenario_name, session_type_func):
    print("="*65)
    print(" "*20,f"SCENARIO: {scenario_name.upper()}")
    print("="*65)

    profile, data=session_type_func()

    #creates session math processor using multiple sessions ( from same instansiation) to simulate multiple activety sessions
    session =sesMat(profile, data, data, data)
    session.ValidateAll()

    #track recovrey and metric data
    rec_trac, rec_trac_msg=session.recoveryTracker()
    hr_i=session.hr_info(rec_trac_msg)
    sr_i=session.sr_info(rec_trac_msg)
    temp_i=session.temp_info(rec_trac_msg)
    al_i=session.al_info(rec_trac_msg)
    sig_i=session.signal_info(rec_trac_msg)

    # classify session as activety type, and find mean activety type
    classification =session.SessionClassification()
    majority_result=session.majority_session(classification, rec_trac)

    formated_log=session.SessionLogPrint(
        hr_i, sr_i, temp_i, al_i, majority_result, rec_trac
    )
    if isinstance(formated_log,list):
        print(*formated_log, sep='\n', end="\n")
    else:
        print("printing data summary failed") 


    info_dict=session.data_dict(hr_i, sr_i, temp_i, al_i, majority_result, rec_trac)
    print(info_dict)
    print("\n")  

def analyze_and_print_mixed(case_title, profile, *session_datasets):
    """
    Helper function to process and print any combination of datasets.
    """
    print(f"\n--- {case_title} ---")
    
    # 1. Instantiate & Validate
    session = sesMat(profile, *session_datasets)
    session.ValidateAll()

    # 2. Extract metrics
    rec_trac, rec_trac_msg = session.recoveryTracker()
    hr_i = session.hr_info(rec_trac_msg)
    sr_i = session.sr_info(rec_trac_msg)
    temp_i = session.temp_info(rec_trac_msg)
    al_i = session.al_info(rec_trac_msg)

    # 3. Classify
    classification = session.SessionClassification()
    majority_result = session.majority_session(classification, is_recovery=rec_trac)
    print(f"Result: Classified as '{majority_result}' | Recovery detected: {rec_trac}")

    # 4. Print Log Report
    formatted_log = session.SessionLogPrint(
        hr_i, sr_i, temp_i, al_i, majority_result, rec_trac
    )
    if isinstance(formatted_log, list):
        print(*formatted_log, sep="\n", end="\n")
    else:
        print("printing data summary failed")

    # 5. Print data dictionary
    info_dict = session.data_dict(
        hr_data=hr_i,
        sr_data=sr_i,
        temp_data=temp_i,
        al_data=al_i,
        activety_type=majority_result,
        recover_status=rec_trac,
    )
    print("\n[Structured Dictionary Output]:")
    print(info_dict) 

def mixed_sessions():
    """
    testing preset mixed session datasets
    """
    print("="*65)
    print(" "*20,f"TESTING MIXED SIGNALS")
    print("="*65)

    profile, res_data = resting()
    _, high_data = high_activity()
    _, rec_data = recovery()
    _, mod_data = moderate_activity()
    _, poor_data = poor_quality()

    # Case 1: Resting + High --> Averages out to moderate activety across the data session)
    analyze_and_print_mixed(
        "Case 1: Resting (x2) + High Activity (x2)",
        profile, res_data, res_data, high_data, high_data
    )

    # Case 2: Resting + Recovery + Resting + High --> will return moderate as the average values of 
    # rest+rest+high returns moderate over the multiple sesions
    analyze_and_print_mixed(
        "Case 2: Resting + Recovery + Resting + High Activity",
        profile, res_data, rec_data, res_data, high_data
    )

    # Case 3: Faulty / Corrupt Dataset --> will return moderate activety as activety 
    # type as poor quality will be rejected in the dataset
    analyze_and_print_mixed(
        "Case 3: Moderate Activity + Poor Quality Data",
        profile, mod_data, poor_data
    )

    


"""
INSTANTIATION OF THE TEST CODE
"""
if __name__ == "__main__":
    testing_individual_classes()

    scenarios=[
        ("Resting Session", resting),
        ("Moderate Activity", moderate_activity),
        ("High Activity", high_activity),
        ("Recovery Session", recovery),
        ("Poor Quality / Invalid Data", poor_quality),
    ]

    print("="*65)
    print(" "*20,f"RUNNING 5 REQUIRED SCENARIOS")
    print("="*65)

    for name, func in scenarios:
        run_scenarios(name, func)

    mixed_sessions()