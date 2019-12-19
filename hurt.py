import json
import numpy as np

def for_leads(leads_list, data, j):
    dop_list_leads = []
    data_leads = data[j]["Message"]
    number_symbol = data_leads.find('V5 = ')
    number_symbol_copy = number_symbol
    while data_leads[number_symbol_copy] + data_leads[number_symbol_copy + 1] != '->':
        number_symbol_copy = number_symbol_copy + 1
    lead_str = data_leads[number_symbol:(number_symbol_copy - 3)]
    lead_after_split = lead_str.split(',')
    for f in lead_after_split:
        dop_list_leads.append(int(f.split(' = ')[1]))
    print(dop_list_leads)
    if len(dop_list_leads) < 12:
        index_patients = patients_list.index(dop_list_leads)
        patients_list.remove(index_patients)
        index_sign = signal_list.index(dop_list_leads)
        patients_list.remove(index_sign)
    else:
        leads_list.append(dop_list_leads)


def formating_files(diagnoz_list, names_diagnoz, signal_list, patients_list, leads_list):
    with open('data_2033_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('ФАЙЛ 1')
        for j in data.keys():
            patients_list.append(j)
            for_leads(leads_list, data, j)
            data_signal = data[j]["Leads"]
            for k in data_signal.keys():
                signal = data[j]["Leads"][k]['Signal']
                signal_list.append(signal)
            for name in names_diagnoz:
                data_diagnoz = data[j]['StructuredDiagnosisDoc'][name]
                index = names_diagnoz.index(name)
                diagnoz_list[index].append(data_diagnoz)

diagnoz_list = []
for i in range(5):
    diagnoz_list.append([])
names_diagnoz = ['regular_normosystole', 'sinus_tachycardia', 'sinus_bradycardia', 'sinus_arrhythmia', 'irregular_sinus_rhythm']
signal_list = []
patients_list = []
leads_list = []


formating_files(diagnoz_list, names_diagnoz, signal_list, patients_list, leads_list)
print(leads_list)



