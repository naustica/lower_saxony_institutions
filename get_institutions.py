import pandas as pd
import requests

inst_df = pd.DataFrame(columns=['inst_name', 'plz', 'ror_id', 'dfg_inst_id', 'federal_state'])

df = pd.read_excel('data/institutionen_gerit.xlsx')

for index, row in df.iterrows():
    plz = row['Postleitzahl vor Ort']
    r = requests.get(url=f'https://openplzapi.org/de/Localities?postalCode={plz}')
    data = r.json()

    inst_name = row['Name deutsch']
    ror_id = row['ROR-ID']
    dfg_inst_id = row['DFG-Inst-ID']
    federal_state = None

    if len(data) != 0:
        federal_state = data[0].get('federalState').get('name')

    inst = dict(
        inst_name=[inst_name],
        plz=[plz],
        ror_id=[ror_id],
        dfg_inst_id=[dfg_inst_id],
        federal_state=[federal_state],
    )

    df2 = pd.DataFrame.from_dict(inst)

    inst_df = pd.concat(objs=[inst_df, df2], ignore_index=True)

inst_df.to_csv(path_or_buf='data/inst_with_federal_state.csv', index=False)




