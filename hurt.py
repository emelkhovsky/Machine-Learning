import json
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


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
    if len(dop_list_leads) < 12:
        delete_number = len(leads_list)
        signal_list.remove(signal_list[delete_number])
        patients_list.remove(patients_list[delete_number])
    else:
        leads_list.append(dop_list_leads)

def formating_files(diagnoz_list, names_diagnoz, signal_list, patients_list, leads_list):
    with open('data_2033_1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print('ФАЙЛ 1')
        for j in data.keys():
            patients_list.append(j)
            data_signal = data[j]["Leads"]
            for k in data_signal.keys():
                signal = data[j]["Leads"][k]['Signal']
                dop_signal_list = []
                dop_signal_list.append(signal)
            signal_list.append(dop_signal_list)
            dop_diagnoz_list = []
            print('------')
            for name in names_diagnoz:
                data_diagnoz = data[j]['StructuredDiagnosisDoc'][name]
                index = names_diagnoz.index(name)
                dop_diagnoz_list.append(data_diagnoz)
            diagnoz_list.append(dop_diagnoz_list)
            print(dop_diagnoz_list)
            for_leads(leads_list, data, j)

def CreateNumPyArray():
    np_array = np.array([signal_list, leads_list, diagnoz_list])
    print(np_array)

def Predicting(data):


    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
    dtrain = xgb.DMatrix(X_train, label=y_train)#для нм эрреев
    dtest = xgb.DMatrix(X_test, label=y_test)
    param = {
        'max_depth': 3,  # the maximum depth of each tree
        'eta': 0.3,  # the training step for each iteration
        'silent': 1,  # logging mode - quiet
        'objective': 'multi:softprob',  # error evaluation for multiclass training
        'num_class': 3}  # the number of classes that exist in this datset
    num_round = 20  # the number of training iterations


diagnoz_list = []
for i in range(5):
    diagnoz_list.append([])
names_diagnoz = ['regular_normosystole', 'sinus_tachycardia', 'sinus_bradycardia', 'sinus_arrhythmia', 'irregular_sinus_rhythm']
signal_list = []
patients_list = []
leads_list = []


formating_files(diagnoz_list, names_diagnoz, signal_list, patients_list, leads_list)
CreateNumPyArray()



