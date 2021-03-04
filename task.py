# Inpuut JSON data
json_Data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]

output_List = []

# Function to calculate BMI
def calc_BMI():
    bmi_List = []
    for i in range(0,len(json_Data)):
        w = json_Data[i]['WeightKg']
        h = json_Data[i]['HeightCm']/100
        temp_BMI = round(w/(pow(h,2)),1)
        bmi_List.append(temp_BMI)

    for i in range(0,len(bmi_List)):
        output_Dict = dict()
        if (bmi_List[i]<=18.5):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Underweight"
            output_Dict["Health risk"] = "Malnutrition risk"
            output_List.append(output_Dict)
        if (bmi_List[i]>=18.5 and bmi_List[i]<=24.9):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Normal weight"
            output_Dict["Health risk"] = "Low risk"
            output_List.append(output_Dict)
        if (bmi_List[i]>=25 and bmi_List[i]<=29.9):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Overweight"
            output_Dict["Health risk"] = "Enhanced risk"
            output_List.append(output_Dict)
        if (bmi_List[i]>=30 and bmi_List[i]<=34.9):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Moderately obese"
            output_Dict["Health risk"] = "Medium risk"
            output_List.append(output_Dict)
        if (bmi_List[i]>=35 and bmi_List[i]<=39.9):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Severely obese"
            output_Dict["Health risk"] = "High risk"
            output_List.append(output_Dict)
        if (bmi_List[i]>=40):
            output_Dict["BMI"] = bmi_List[i]
            output_Dict["BMI Category"] = "Very Severely obese"
            output_Dict["Health risk"] = "Very High risk"
            output_List.append(output_Dict)

    print(output_List)

    # Calculating count of total number of overweight people 
    overweight_count = 0
    for i in range(0, len(output_List)):
        if output_List[i]["BMI"] >= 25:
            overweight_count+=1
    print(overweight_count)
    return overweight_count
total_overweight_count = calc_BMI()
