import pydicom as dicom
import os
from glob import glob
import pandas as pd

df = pd.DataFrame(columns=['Path after changes'])
df.index.name = "Original path"
count = 1
for file_name in glob('./img/*.dcm'):
    x = dicom.dcmread(file_name)
    x.PatientName = ""
    if not os.path.exists(f"result/{x.StudyInstanceUID}/{x.SeriesInstanceUID}/"):
        os.makedirs(f"result/{x.StudyInstanceUID}/{x.SeriesInstanceUID}/")
    x.save_as(f"result/{x.StudyInstanceUID}/{x.SeriesInstanceUID}/{x.SOPInstanceUID}.dcm")
    # new_row = pd.Series([20, 30])
    # pd.concat([])
    df.loc[file_name] = [f"result/{x.StudyInstanceUID}/{x.SeriesInstanceUID}/{x.SOPInstanceUID}.dcm", ]
    count += 1
    # df = df.append({'Path to changes': 20 , 'Path after changes': 30}, ignore_index=True)
    ratio = open("ratio.txt", "a+")
    ratio.write (f"{file_name} == result/{x.StudyInstanceUID}/{x.SeriesInstanceUID}/{x.SOPInstanceUID}.dcm" "\n")
ratio.close()
df.to_excel("somebody.xlsx")