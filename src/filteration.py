import os
import pandas as pd

# Set the path and filenames
path = "C://Users//akhil//Desktop//MINE//Forage//quantium-task-1-model-answer//data"
files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]
output_file = os.path.join(path, "combined_data.csv")
header_written = False
for file in files:
    csv_path = os.path.join(path, file)
    data = pd.read_csv(csv_path)
    data['price'] = data["price"].replace({r"[$,]": ''}, regex=True).astype(float)
    data['sales'] = data['price'] * data['quantity']
    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    filtered_data = data[['sales', 'date', 'region']]
    if not header_written:
        filtered_data.to_csv(output_file, mode='w', header=True, index=False)
        header_written = True  
    else:
        filtered_data.to_csv(output_file, mode='a', header=False, index=False)


