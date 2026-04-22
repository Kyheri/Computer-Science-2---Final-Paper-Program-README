#CS Quarter 3 project

#User Defined Function/s
#For CBC results
def check_range(value, low, high):
    if value < low:
        return "LOW"
    elif value > high:
        return "HIGH"
    else:
        return "NORMAL"

#For urinalysis test results
def urinalysis_analysis(color, texture, protein, glucose, ph, nitrites, ketones, bilirubin, urob, lc_es, spec_grav, rbc, wbc, cast, crystal, epth_cell, micro ):
    result = [] #empty list to store findings
    advice = [] #empty list to store advice

    # Naked eye: URINE COLOR
    if color.lower() in ["pale yellow", "light yellow"]:
        result.append("normal urine color")
    elif color.lower() in ["clear"]:
        result.append("overhydration")
        advice.append("consider reducing fluid intake if persistent")
    elif color.lower() in ["dark yellow"]:
        result.append("possible dehydration")
        advice.append("increase water intake")
    elif color.lower() in ["orange", "amber"]:
        result.append("possible dehydration, may also be caused by certain vitamins and medicine")
        advice.append("check supplements or medication")
    elif color.lower() in ["brown", "dark orange"]:
        result.append("possible dehydration, can also indicate liver problems")
        advice.append("seek medical attention if persistent")
    elif color.lower() in ["dark brown", "black"]:
        result.append("sign of medical condition, such as liver disease")
        advice.append("consult a health care provider")
    elif color.lower() in ["red", "pink"]:
        result.append("an indication of blood or result of medications or food")
        advice.append("seek medical advice if unexplained")
    elif color.lower() in ["blue", "green"]:
        result.append("result of eating foods or medications with large amount of dye, green can also indicate UTI")
        advice.append("check supplements/medication; if infection is suspected, consult a doctor")
    elif color.lower() in ["white", "milky"]:
        result.append("an indication of a condition called chyluria")
        advice.append("medical evaluation is recommended")
    else:
        result.append("unusual urine color")

    # Naked eye: URINE TEXTURE
    if texture.lower() in ["cloudy", "turbid"]:
        result.append("possible sign of infection, crystals or protein")
        advice.append("consider urinalysis follow-up")
    elif texture.lower() in ["clear", "transparent"]:
        result.append("normal clarity")
    else:
        result.append("unusual urine texture")

    #Lab values:

    # Protein (mg/dL)
    if protein > 30: 
        result.append("Proteinuria (possible kidney damage)")
        advice.append("Persistent proteinuria requires medical evaluation")
    else:
        result.append("Normal protein level")

    if glucose > 0: 
        result.append("Glucosuria (possible diabetes)")
        advice.append("Check blood sugar levels")
    else:
        result.append("Normal glucose level")

    # Glucose (mg/dL)
    if 4.5 <= ph <= 8.0:
        result.append("Normal pH range")
    else:
        result.append("Abnormal pH (possible metabolic or infection issue)")
        advice.append("Further testing may be needed")

# Nitrites : Qualitative
    if nitrites.lower() == "positive":
        result.append("Nitrites detected (possible UTI)")
        advice.append("Consult a professional for possible infection")
    else:
        result.append("Nitrites negative")

    # Ketones : mg/dL
    if ketones == 0:
        result.append("No ketones detected (Normal)")
    elif 5 <= ketones <= 20:
        result.append("Trace ketones present (usually benign, monitor)")
        advice.append("Monitor hydration and carbohydrate intake. If persistent, consider checking blood sugar")
    elif 21 <= ketones <= 30:
        result.append("Small ketones present (slightly elevated)")
        advice.append("Ensure adequate carbohydrate intake and hydration; monitor if persistent")
    elif 31 <= ketones <= 40:
        result.append("Moderate ketones present (possible metabolic issue)")
        advice.append("Increase fluid intake, ensure adequate carbohydrate consumption, and consult a healthcare provider if symptoms (nausea, fatigue) occur.")
    elif ketones >= 80:
        result.append("Large ketones present (possible diabetic ketoacidosis)")
        advice.append("Seek urgent medical evaluation. Large ketones with high blood sugar can indicate diabetic ketoacidosis, a medical emergency")
    else:
        result.append("Ketone value falls in borderline range")
        advice.append("Interpret with caution; consider repeat testing or consult a healthcare provider")

    # Bilirubin : Qualitative
    if bilirubin.lower() == "negative":
        result.append("No bilirubin detected (Normal)")
    else:
        result.append("Bilirubin present (possible liver disease or bile duct obstruction)")
        advice.append("Consult a healthcare provider for liver function evaluation")

    # Urobilinogen (Ehrlich units/dL)
    if 0.1 <= urob <= 1.0:
        result.append("Normal urobilinogen level")
    else:
        if urob > 1.0:
            result.append("Elevated urobilinogen (possible liver disease or hemolysis)")
            advice.append("Further liver function testing may be needed")
        elif urob == 0:
            result.append("Absent urobilinogen (possible bile duct obstruction)")
            advice.append("Consult a healthcare provider for evaluation")

    # Leukocyte esterase (qualitative: Positive/Negative)
    if lc_es.lower() == "negative":
        result.append("Leukocyte esterase negative (Normal)")
    else:
        result.append("Leukocyte esterase detected (possible infection)")
        advice.append("Consult a healthcare provider for evaluation of possible urinary tract infection")

    # Specific Gravity
    if 1.005 <= spec_grav <= 1.030:
        result.append("Normal specific gravity")
    else:
        result.append("Abnormal specific gravity (hydration or kidney issue)")
        advice.append("Hydration status or kidney function should be checked")

    # Red blood cell : count per high power field (HPF)
    if rbc <= 2:
        result.append("Normal RBC count")
    else:
        result.append("Hematuria (blood in urine)")
        advice.append("Seek medical evaluation")

    # White blood cell : count per high power field (HPF)
    if wbc <= 4:
        result.append("Normal WBC count")
    else:
        result.append("Pyuria (possible infection)")
        advice.append("Consult a healthcare provider")

    # Casts : Qualitative
    if cast == "absent":
        result.append("No casts detected")
    else:
        result.append("Casts present (possible kidney disease)")
        advice.append("Medical evaluation recommended")

    # Crystal : Qualitative
    if crystal == "absent":
        result.append("No crystals detected")
    else:
        result.append("Crystals present (possible kidney stones or metabolic disorder)")
        advice.append("Further evaluation may be needed")

    # Epithelial Cell : count per high power field (HPF)
    if epth_cell <= 20:
        result.append("Normal epithelial cell count")
    else:
        result.append("High epithelial cells (possible contamination)")
        advice.append("Repeat test may be needed")

    # Microorganisms : Qualitative
    if micro.lower() == "present":
        result.append("Microorganisms detected (possible infection)")
        advice.append("Consult a healthcare provider")
    else:
        result.append("No microorganisms detected")

    return result, advice # returns list of findings

def safe_float(prompt, default=0.0):
    try:
        return float(input(prompt))
    except ValueError:
        print(f"Invalid input. Defaulting to {default}.")
        return default

def safe_string(prompt, valid_choices, default=None):
    value = input(prompt).strip().lower()
    if value in valid_choices:
        return value
    else:
        print(f"Invalid input. Defaulting to '{default}'.")
        return default


def safe_float(prompt, default=0.0):
    try:
        return float(input(prompt))
    except ValueError:
        print(f"Invalid input. Defaulting to {default}.")
        return default

def safe_string(prompt, valid_choices, default=None):
    value = input(prompt).strip().lower()
    if value in valid_choices:
        return value
    else:
        print(f"Invalid input. Defaulting to '{default}'.")
        return default

#For lipid panel test results
def lipid_panel_analysis(ttl_c, ldl, hdl, trig, sex="male"): 
    result = []
    advice = []
    # Total Cholesterol
    if ttl_c < 200:
        result.append("Normal total cholesterol")
    elif 200 <= ttl_c <= 239:
        result.append("Borderline high total cholesterol")
        advice.append("Reduce saturated fat intake and monitor cholesterol regularly")
    else:
        result.append("High total cholesterol")
        advice.append("Consult a healthcare provider for management")

    # LDL
    if ldl < 100:
        result.append("Optimal LDL cholesterol")
    elif 100 <= ldl < 130:
        result.append("Near optimal LDL cholesterol")
    elif 130 <= ldl < 160:
        result.append("Borderline high LDL cholesterol")
        advice.append("Adopt a heart-healthy diet to lower LDL")
    elif 160 <= ldl < 190:
        result.append("High LDL cholesterol")
        advice.append("Medical evaluation recommended")
    else:
        result.append("Very high LDL cholesterol")
        advice.append("Seek medical advice promptly")

    # Triglyceride
    if trig < 150:
        result.append("Normal triglycerides")
    elif 150 <= trig <= 199:
        result.append("Borderline elevated triglycerides")
        advice.append("Reduce intake of added sugars and refined carbohydrates")
    elif 200 <= trig <= 499:
        result.append("High triglycerides")
        advice.append("Increase physical activity, avoid trans fats and minimize saturated fats. Consult a professional to monitor cardiovascular risk")
    else:  # trig >= 500
        result.append("Very high triglycerides")
        advice.append("Seek medical evaluation promptly due to risk of pancreatitis")

        

    # HDL (sex-specific)
    if sex.lower() == "female":
        if hdl < 50:
            result.append("Low HDL cholesterol (risk factor for women)")
            advice.append("Increase exercise and healthy fats to raise HDL")
        elif 50 <= hdl < 60:
            result.append("Acceptable HDL cholesterol")
        else:
            result.append("High HDL cholesterol (protective)")
    else:  # male
        if hdl < 40:
            result.append("Low HDL cholesterol (risk factor for men)")
            advice.append("Increase exercise and healthy fats to raise HDL")
        elif 40 <= hdl < 60:
            result.append("Acceptable HDL cholesterol")
        else:
            result.append("High HDL cholesterol (protective)")

    return result, advice #return list of findings & advice

def safe_float(prompt, default=0.0):
    try:
        return float(input(prompt))
    except ValueError:
        print(f"Invalid input. Defaulting to {default}.")
        return default

def safe_string(prompt, valid_choices, default=None):
    value = input(prompt).strip().lower()
    if value in valid_choices:
        return value
    else:
        print(f"Invalid input. Defaulting to '{default}'.")
        return default

#For GFR KIDNEY 
def get_reference_gfr(age):
    if 18 <= age <= 29:
        return (90, 120)
    elif 30 <= age <= 39:
        return (85, 110)
    elif 40 <= age <= 49:
        return (80, 105)
    elif 50 <= age <= 59:
        return (75, 100)
    elif 60 <= age <= 69:
        return (70, 95)
    else:
        return (60, 90)

print("Before accessing our program, please read the TOS (Terms of Service) of our program.")
#Terms of Service of our program
print("""===TERMS OF SERVICE===

Acknowledgement
These are the Terms of Service governing the use of this program and the agreement that operates between you and the Company. These Terms of Service set out the rights and obligations of all users regarding the use of the program.
By accessing or using the program, you agree to be bound by these Terms of Service. If You disagree with
any part of these Terms of Service then You may not access the program.
- - - - - - -
USER INFORMATION
By using our program you consent to the legal use of your data to be processed and used to give you advice and results about your information.
When entering any personal information, ensure it is of atmost accuracy, failure to do so will give you inaccurate results.

CONTENT
You are allowed to post content related to our program, but you are responsible and will be held accountable for any content that you upload, such as its legality, reliability and appropriateness.
When uploading content related or featuring our program you give us the right to access, modify, publicly display, recreate and distribute such content online.

INTELLECTUAL PROPERTY
The original source code of this program such as its features and functionality shall only be accessible by its Company and licensors.

CONTACT US
Any questions regarding our Terms of Service you can contact us:
-By sending us an email: abreyes@cbzrc.pshs.edu.ph""")


determiner = 0

#Confirms if the user has acknowledged and agreed to our TOS

while determiner == 0:
    
    response = input("""
Do you agree to the Terms of Service of our program? |Y/N|: """).title()
    
    #Start of main program.
    if response == "Y":
        determiner = determiner + 1
        
        print("""
Thank you for using our service, before you start you first have to enter basic information to ensure accurate results.""")
        
        #User Profile Prompt, asks for users basic information
        print(""" =====User Profile Prompt=====
(Enter the following prompts.)
""")
        while True:
            #Yet to have Error handling
            try:
                age=int(input("Age: "))
                if age>=1 and age<=122:
                    break
                else:
                    print("Invalid input, try again.")
                    continue
            except ValueError: 
                print("Please enter a number, try again..")

        while True:
            gender=input("Gender |M/F|: ").title()
            if gender == 'M' or gender == 'F':
                break
            else:
                print("Invalid input, try again.")
                continue

        illness=input("Current illnesses or diseases: ")

        #Main interface of the program, has several analyzers for the user.
        while True:
            response_1 = input("""
 (Select a number.)
========MENU========
1. Glucose Tests
2. CBC
3. Urinalysis
4. Lipid Panel
5. Coagulation tests
6. Thyroid Tests
7. Kidney Functions
8. EXIT

Response: """)
            
            #Numbers 1,2,3,4,5,6 are yet to be done.
            #Some programs yet to implement the consideration of gender and illnesses.
            match response_1 == "1":
                case _ if (response_1) == '1':
                    print("""
=====Glucose Tests=====
""")
                    while True:
                        try: 
                            # Ask for glucose level
                            glucose = float(input("Enter the user's glucose level (mg/dL): "))
                            break
                        except ValueError:
                            print("Numeric value only")
                        
                    # Ask for most recent food type
                    print("""
What type of food did you eat most recently?""")
                    print("""Options: sugary, salty, protein, fiber
                    """)
                    food = input("Enter the type of food: ").lower()

                    # Determine glucose category
                    if glucose < 70:
                        status = "Low blood sugar (Hypoglycemia)"
                    elif 70 <= glucose <= 99:
                        status = "Normal"
                    elif 100 <= glucose <= 125:
                        status = "Slightly high (Prediabetes range)"
                    else:
                        status = "High blood sugar (Possible Diabetes)"

                    # Explain effect of food
                    if food == "sugary":
                        food_effect = "Sugary foods can cause a rapid spike in blood glucose levels."
                    elif food == "salty":
                        food_effect = "Salty foods do not directly raise glucose but may affect blood pressure."
                    elif food == "protein":
                        food_effect = "Protein slows glucose absorption, helping stabilize blood sugar."
                    elif food == "fiber":
                        food_effect = "Fiber-rich foods help reduce glucose spikes after meals."
                    else:
                        food_effect = "Food effect not recognized. Try to enter sugary, salty, protein, or fiber."

                    print("""
======GLUCOSE TESTS RESULTS======
                    """)
                    # Print glucose analysis
                    print(f"""Your glucose level is {glucose} mg/dL. This level is considered {status}.

Most recent food eaten: {food.capitalize()}. {food_effect}""")
                                        
                    continue
                
                case _ if (response_1) == '2':
                    print("""
=====CBC=====
""")
                    while True:
                        try:
                            # User inputs
                            rbc=float(input("RBC (Red blood cells) in M/uL: "))
                            wbc=float(input("WBC (White blood cells) in K/uL: "))
                            mch=float(input("MCH (Mean corpuscular hemoglobin) in pg: "))
                            mchc=float(input("MCHC (Mean corpuscular hemoglobin concentration) in g/dL: "))
                            mpv=float(input("MPV (Mean platelet volume)in fL: "))
                            rdw=float(input("RDW (Red cell distribution width) in %: "))
                            mcv=float(input("MCV (Mean corpuscular volume)in fL: "))
                            htc=float(input("Htc (Hematocrit) in %: "))
                            hgb=float(input("Hgb (Hemoglobin)in g/dL: "))
                            pc=float(input("Platelet count in McL: "))
                            break
                        except ValueError:
                            print(f"Numeric value only")
                        
                    # Gender-based ranges
                    if gender == 'M':
                        rbc_low = 4.7
                        rbc_high = 6.1
                        hgb_low = 13.5
                        hgb_high = 17.5
                        htc_low = 41
                        htc_high = 53
                    # Females
                    else:
                        rbc_low = 4.2
                        rbc_high = 5.4
                        hgb_low = 12.0
                        hgb_high = 15.5
                        htc_low = 36
                        htc_high = 46

                    print("""
======CBC TESTS RESULTS======
                    """)
                    count_cbc=0
                    print(f"RBC: {check_range(rbc, rbc_low, rbc_high)}")
                    if rbc>=rbc_high or rbc<=rbc_low:
                        count_cbc=count_cbc+1
                    print(f"WBC: {check_range(wbc, 4.0, 10.0)}")
                    if wbc>=10 or wbc<=4:
                        count_cbc=count_cbc+1
                    print(f"MCH: {check_range(mch, 27, 31)}")
                    if mch>=31 or mch<=27:
                        count_cbc=count_cbc+1
                    print(f"MCHC: {check_range(mchc, 32, 36)}")
                    if mchc>=36 or mchc<=32:
                        count_cbc=count_cbc+1
                    print(f"MPV: {check_range(mpv, 7, 10)}")
                    if mpv>=10 or mpv<=7:
                        count_cbc=count_cbc+1
                    print(f"RDW: {check_range(rdw, 11.5, 14.5)}")
                    if rdw>=14.5 or rdw<=11.5:
                        count_cbc=count_cbc+1
                    print(f"MCV: {check_range(mcv, 80, 100)}")
                    if mcv>=100 or mcv<=80:
                        count_cbc=count_cbc+1
                    print(f"Hematocrit: {check_range(htc, htc_low, htc_high)}")
                    if htc>=htc_high or rbc<=htc_low:
                        count_cbc=count_cbc+1
                    print(f"Hemoglobin: {check_range(hgb, hgb_low, hgb_high)}")
                    if hgb>=hgb_high or hgb<=hgb_low:
                        count_cbc=count_cbc+1
                    print(f"Platelet Count: {check_range(pc, 150, 400)}")
                    if pc>=400 or pc<=150:
                        count_cbc=count_cbc+1
                    
                    if count_cbc>=3:
                        print("""
Consult a doctor!!
Note: If all RBC, WBC, and platelets are low, then there is a likely chance that you have a bone marrow problem.
Note: If you have a high WBC, then there's a likely chance you have an infection or imflammation.
Note: If you have a low Hemoglobin and an abnormal MCV, this can indicate nutrional defficiency.
Note: If all RBC, Hemoglobin, and Hematocrit are low, it can indicate anemia, defficiency, or chronic diseases.
                        """)
                       
                    continue

                    
                
                case _ if (response_1) == '3':
                    print("""
=====Urinalysis=====
""")

                    # Main program execution
                    color = input("Enter urine color (e.g., pale yellow, red): ").strip().lower()
                    texture = input("Enter urine texture/clarity (e.g., clear, cloudy): ").strip().lower()

                    protein = safe_float("Enter protein (mg/dL): ", default=0.0)
                    glucose = safe_float("Enter glucose (mg/dL): ", default=0.0)
                    ph = safe_float("Enter pH level: ", default=7.0)
                    ketones = safe_float("Enter ketones (mg/dL): ", default=0.0)
                    urob = safe_float("Enter urobilinogen (Ehrlich units/dL): ", default=0.2)
                    spec_grav = safe_float("Enter specific gravity: ", default=1.015)
                    rbc = safe_float("Enter red blood cell count (per HPF): ", default=0)
                    wbc = safe_float("Enter white blood cell count (per HPF): ", default=0)
                    epth_cell = safe_float("Enter epithelial cell count (per HPF): ", default=0)

                    nitrites = safe_string("Enter nitrites (Positive/Negative): ", valid_choices=["positive", "negative"], default="negative")
                    bilirubin = safe_string("Enter bilirubin (Positive/Negative): ", valid_choices=["positive", "negative"], default="negative")
                    lc_es = safe_string("Enter leukocyte esterase (Positive/Negative): ", valid_choices=["positive", "negative"], default="negative")
                    cast = safe_string("Enter casts (Present/Absent): ", valid_choices=["present", "absent"], default="absent")
                    crystal = safe_string("Enter crystals (Present/Absent): ", valid_choices=["present", "absent"], default="absent")
                    micro = safe_string("Enter microorganisms (Present/Absent): ", valid_choices=["present", "absent"], default="absent")

                    # Run analysis
                    finds, advice = urinalysis_analysis(
                        color, texture, protein, glucose, ph, nitrites, ketones,
                        bilirubin, urob, lc_es, spec_grav, rbc, wbc, cast, crystal, epth_cell, micro
                    )
                    
                    print("""
======URINALYSIS RESULTS======
                    """)
                    # Print results
                    print("Urinalysis Findings:")
                    for f in finds:
                        print("-", f)

                    print("\nAdvice:")
                    for a in advice:
                        print("-", a)

                    print("\nAnalysis given is not 100% accurate; always consider consultation with a healthcare provider.")

                    continue
                
                case _ if (response_1) == '4':
                    print("""
=====Lipid Panel=====
""")

                    #Main program execution
                    #User input values
                    ttl_c = safe_float("Enter your Total Cholesterol (mg/dL): ", default=0.0)
                    ldl = safe_float("Enter LDL (mg/dL): ", default=0.0)
                    hdl = safe_float("Enter HDL (mg/dL): ", default=0.0)
                    trig = safe_float("Enter Triglycerides (mg/dL): ", default=0.0)

                    sex = safe_string("Enter sex (Male/Female): ", valid_choices=["male", "female"], default="male")

                    #call for the function with user inputs
                    finds, advice = lipid_panel_analysis(ttl_c, ldl, hdl, trig, sex)

                    print("""
======LIPID PANEL RESULTS======
                    """)
                    #Print results
                    print("Lipid Panel Findings: ")
                    for r in finds:
                        print("-", r)

                    print("\nAdvice:")
                    for a in advice:
                        print("-", a)
                    print(" ")
                    print("analysis given is not 100% accurate, always consider consultation of a healthcare provider")

                    
                    continue
                
                case _ if (response_1) == '5':
                    print("""
=====Coagulation tests=====
""")
                    # Has Error handling
                    while True:
                        try:
                            inr = float(input("Enter INR (1 decimal): "))
                            if inr <= 0 or inr > 5: 
                                print("Enter a valid INR value")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only")

                    while True:
                        try:
                            pt = float(input("Enter PT (s): "))
                            if pt <= 0 or pt > 100:  
                                print("Enter a valid PT value")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only")

                    while True:
                        try:
                            ddimer = float(input("Enter D-Dimer (ng/ml): "))
                            if ddimer < 0 or ddimer > 60000:
                                print("Enter a valid D-Dimer value")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only")

                    choice = ""
                    choice = input("Press 0 to analyze: ")
                    if choice == "0":
                        
                        print("""
======COAGULATION TESTS RESULTS======
                    """)

                        #checking of INRs and adding necessary advice.
                        if 0.8 <= inr <= 1.2:
                            print("INR: Normal. Keep consistent!")
                        elif inr < 0.8:
                            print("INR: Low. Risk of clotting.")
                            print('Advice: Don’t miss your medication and reduce Vitamin K-rich foods.')
                        else:
                            print("INR: High. Risk of bleeding.")
                            print("Advice: Consult from a doctor and increase Vitamin K-rich foods.")

                        #checking of PTs and adding necessary advice.
                        if 11 <= pt <= 13.5:
                            print("PT: Normal. Keep consistent!")
                        elif pt < 11:
                            print("PT: Low. Risk of Clotting.")
                            print("Advice: Avoid large amount of Vitamin K foods, be careful with natural supplements, and try to have your blood drawn at the same time of day for each test.")
                        else:
                            print("PT: High. Risk of Bleeding.")
                            print("Advice: Clotting too slowly; Use soft-bristled tooth brush, limit alcohol intake, and consult prescribed antibiotics.")

                        #checking Ddimers and adding necessary advice.
                        if ddimer <= 500:
                            print("D-Dimer: Normal. Keep consistent!")
                        else:
                            print("D-Dimer - Abnormal")
                            print("Advice: Ask your doctor about compression stockings, and drink plenty of water.")
                    else: 
                        print("Analysis has been Cancelled..")


                
                case _ if (response_1) == '6':
                    print("""
=====Thyroid Tests=====
""")
                    

                    print("Starting test..")

                    #Error handling for proper numerical inputs
                    while True:
                        try:
                            tsh = float(input("Enter TSH (mIU/L): "))
                            if tsh <= 0 or tsh > 100: 
                                print("Enter a valid TSH value!")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only!")

                    while True:
                        try:
                            ft4 = float(input("Enter Free T4 (ng/dL): "))
                            if ft4 <= 0 or ft4 > 10:
                                print("Please enter a valid Free T4 value!")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only!")

                    while True:
                        try:
                            ft3 = float(input("Enter Free T3 (pg/mL): "))
                            if ft3 <= 0 or ft3 > 20:
                                print("Please enter a valid Free T3 value!")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only!")

                    while True:
                        try:
                            tpo = float(input("Enter TPO Antibodies (IU/ml): "))
                            if tpo < 0 or tpo > 100:
                                print("Enter a valid TPO Antibodies value!")
                            else:
                                break
                        except ValueError:
                            print("Numeric value only!")
                            
                    choice = ""
                    choice = input("Press 0 to analyze: ")
                    if choice == "0":
                        
                        print("""
======THYROID TESTS RESULTS======
                    """)

                        #checking TSH
                        if gender == "M":
                            if 0.4 <= tsh <= 4.0:
                                print("TSH: Normal")
                            elif tsh < 0.4:
                                print("TSH: Low. ")
                                print("Advice: limit Iodine food which fuels the thyroid fire.")
                            else:
                                print("TSH: High. ")
                                print("Advice: focus on Selenium and Zinc to help the thyroid produce hormone.")
                        else:
                            if 0.4 <= tsh <= 4.5:
                                print("TSH: Normal")
                            elif tsh < 0.4:
                                print("TSH: Low. ")
                                print("Advice: limit Iodine food which fuels the thyroid fire.")
                            else:
                                print("TSH: High. ")
                                print("Advice: focus on Selenium and Zinc to help the thyroid produce hormone.")
                            
                        #checking Free T4
                        if 0.8 <= ft4 <= 1.8:
                            print("Free T4: Normal")
                        elif ft4 > 3.0:
                            print("Free T4: High. ")
                            print("Advice: Relax.")
                        else:
                            print("Free T4: Low. ")
                            print("Advice: wait a minute before eating or drinking coffee.")

                        #checking Free T3
                        if 2.0 <= ft3 <= 4.4:
                            print("Free T3: Normal")
                        elif ft3 > 8.0:
                            print("Free T3: High")
                            print("Advice: Avoid too much caffeine. ")
                        else:
                            print("Free T3: Low.")
                            print("Advice: Focus on gut health.")

                        # Checking TPO Antibodies
                        if tpo <= 35:
                            print("TPO Antibodies: Normal")
                        else:
                            print("TPO Antibodies: High")
                            print("Advice:  Focus on Anti-Inflammatory Diet.")
                    else:
                        print("Analysis has been Cancelled..")

                    continue
                
                case _ if (response_1) == '7':
                    case _ if (response_1) == '7':
                    print("""=====Kidney Functions=====""")

                    while True:
                        try:
                            gfr = float(input("Enter your GFR (mL/min/1.73 m²): "))
                            if gfr <= 0 or gfr > 200:
                                print("Please enter a realistic GFR value (1–200).")
                                continue
                            break
                        except ValueError:
                            print("Numeric value only. Try again.")

                    # Get reference range
                    low, high = get_reference_gfr(age)

                    print("""
======KIDNEY FUNCTIONS RESULTS======
                    """)
                    print("Your GFR:", gfr)
                    print(f"Reference GFR for your age: {low} - {high}")

                    # Correct comparison
                    if low <= gfr <= high:
                        print("\nResult: Normal")
                        print("Your kidney filtration rate is within the expected range.")
                    else:
                        print("\nResult: Not Normal")

                        if gfr < low:
                            print("Your GFR is LOWER than expected.")
                        else:
                            print("Your GFR is HIGHER than expected.")

                        print("\nPossible Causes:")
                        print("- Dehydration")
                        print("- Diabetes")
                        print("- High blood pressure")
                        print("- Kidney disease")

                        print("\nTips to Improve Kidney Health:")
                        print("- Drink enough water")
                        print("- Maintain a healthy diet")
                        print("- Control blood sugar and blood pressure")
                        print("- Exercise regularly")
                        print("- Consult a doctor if symptoms persist")

                    continue


                case _ if (response_1) == '8':
                    #Breaks all loops, leading user to the end of the program.
                    break
                #The following two cases are for error
                case _ if (response_1) > '8':
                    print("Invalid")
                    continue
                case _ if not response_1.isnumeric():
                    print("Invalid")
                    continue

        
    elif response == "N":
        break
    else:
        determiner = 0
        print("""
Your response is invalid, try again.""")
        
print("======EXIT======")
input("""
Closing program. . .
""")
