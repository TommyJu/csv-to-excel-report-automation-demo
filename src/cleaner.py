def clean_sales(data):
    data.drop_duplicates()
    data.dropna()
    print("Sales data cleaned...")