import json
import matplotlib.pyplot as plt
import pandas as pd

def formating_files():
    with open('data_2033_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('ФАЙЛ 1')
        for j in data.keys():
            print(j)
            data_signal = data[j]["Leads"]
            for k in data_signal.keys():
                signal = data[j]["Leads"][k]['Signal']
                #graphics(signal)
                signal_list.append(signal)
            data_regular_normosystole = data[j]['StructuredDiagnosisDoc']['regular_normosystole']
            one_list.append(data_regular_normosystole)
            data_sinus_tachycardia = data[j]['StructuredDiagnosisDoc']['sinus_tachycardia']
            two_list.append(data_sinus_tachycardia)
            data_sinus_bradycardia = data[j]['StructuredDiagnosisDoc']['sinus_bradycardia']
            three_list.append(data_sinus_bradycardia)
            data_sinus_arrhythmia = data[j]['StructuredDiagnosisDoc']['sinus_arrhythmia']
            four_list.append(data_sinus_arrhythmia)
            data_irregular_sinus_rhythm = data[j]['StructuredDiagnosisDoc']['irregular_sinus_rhythm']
            five_list.append(data_irregular_sinus_rhythm)


def create_pandas(one_list,two_list,three_list,four_list,five_list):
    df = pd.DataFrame({
        'signal': signal_list[:21:],
        '1st_in_sin': one_list[:21:],
        '2nd_in_sin': two_list[:21:],
        '3d_in_sin': three_list[:21:],
        '4th_in_sin': four_list[:21:]
    })
    return df

def graphics(data):
    plt.plot(data)
    plt.show()

signal_list = []
one_list = []
two_list = []
three_list = []
four_list = []
five_list = []
results_list = []
formating_files()
print(one_list)
print(two_list)
print(three_list)
print(four_list)
print(five_list)
#print(signal_list)
df = create_pandas(one_list,two_list,three_list,four_list,five_list)
print(df['1st_in_sin'])
for i in range(21):
    if 'True' in pd.iterrows(i):
        print('СИНУСОВЫЙ')
    else:
        print('НЕТ')
