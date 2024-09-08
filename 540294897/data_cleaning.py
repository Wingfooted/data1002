import pandas as pd
file = "C:\\Users\\赵松斌\\Desktop\\data (1).xlsx"
df = pd.read_excel(file, sheet_name=0)
df = df.drop(index=range(4)) 
df['Year'] = df.iloc[:, 0].astype(str).str[:4]  
df['Month'] = df.iloc[:, 0].astype(str).str[4:6]  
month_map = {
    '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
    '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
}
df['Month'] = df['Month'].map(month_map)
df.drop(df.columns[0], axis=1, inplace=True)
df.rename(columns={'Unnamed: 1': 'Temperature(℃)'}, inplace=True)
df['Temperature(℃)'] = df['Temperature(℃)'] + 13.9
df_cleaned = df[['Year', 'Month'] + [col for col in df.columns if col not in ['Year', 'Month']]]
cleaned_file_path = "C:\\Users\\赵松斌\\Desktop\\cleaned data.xlsx"
df_cleaned.to_excel(cleaned_file_path, index=False)

