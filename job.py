import pandas as pd
import os

def extract_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
        data = data.replace(',\"\"\n', '\n')

    with open('your_file.csv', 'w') as f:
        f.write(data)

    # Read the CSV file
    df = pd.read_csv('your_file.csv')
    filtered_df = df[df['Method'] == 'Contribute']
    filtered_df = filtered_df[filtered_df["ErrCode"].isna() | filtered_df["Status"].isna()]
    filtered_df = filtered_df.reset_index(drop=True)
    # Create the "extracted" DataFrame

    extracted = filtered_df.groupby("From").agg(
        sum=("Value_IN(BNB)", "sum"),
        # empty text column
        BNB=("Blockno", "first"),
        SL=("Value_IN(BNB)", "count")
        ).reset_index()

    extracted["BNB"] = extracted["sum"].apply(lambda x: '{:.2f}'.format(x))
    extracted["url"] = extracted["From"].apply(lambda x: f"https://bscscan.com/address/{x}")
    extracted = extracted.sort_values(by="sum")

    # Split into two DataFrames based on condition
    # and bigger or equal to 0.1
    df_sum_lt_1 = extracted[extracted['sum'] < 1]
    df_sum_lt_1 = df_sum_lt_1[df_sum_lt_1['sum'] >= 0.1]
    df_sum_gte_1 = extracted[extracted['sum'] >= 1]

    # Calculate sum for each DataFrame
    big_sum_lt_1 = df_sum_lt_1['sum'].sum()
    big_sum_gte_1 = df_sum_gte_1['sum'].sum()
    big_sums_df = pd.DataFrame({'DataFrame': ['Nho hon 1', 'Lon hon 1'], 'BigSum': [big_sum_lt_1, big_sum_gte_1]})

    # {:.2f}
    big_sums_df["BigSum"] = big_sums_df["BigSum"].apply(lambda x: '{:.2f}'.format(x))

    # drop sum column
    df_sum_lt_1 = df_sum_lt_1.drop(columns=["sum"])
    df_sum_gte_1 = df_sum_gte_1.drop(columns=["sum"])

    # Print the two big sums
    print("Big Sum for sum < 1:", big_sum_lt_1)
    print("Big Sum for sum >= 1:", big_sum_gte_1)

    # Create an ExcelWriter object
    writer = pd.ExcelWriter('combined_data.xlsx', engine='xlsxwriter')

    big_sums_df.to_excel(writer, sheet_name='Combined', index=False, startrow=0, startcol=0)
    df_sum_gte_1.to_excel(writer, sheet_name='Combined', index=False, startrow=len(big_sums_df) + 2, startcol=0)
    df_sum_lt_1.to_excel(writer, sheet_name='Combined', index=False, startrow=len(big_sums_df) + len(df_sum_gte_1) + 4, startcol=0)
    
    # Save the Excel file
    writer.close()
    # writer.save()
    
def delete_data():
    if os.path.exists("combined_data.xlsx"):
        os.remove("combined_data.xlsx")
    if os.path.exists("your_file.csv"):
        os.remove("your_file.csv")


if __name__ == '__main__':
    extract_data('you.csv')