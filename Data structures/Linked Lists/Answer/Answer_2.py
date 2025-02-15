def insert_values(self, data_list):  
    if not data_list:  # Edge case: empty input list  
        return  
    for data in data_list:  
        self.insert_at_end(data)  # Add each value to the end  