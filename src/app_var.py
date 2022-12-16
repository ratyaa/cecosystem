class AppVariable:
    def __init__(self, name, var_data, default_data, is_numeric):
        self.name = name
        self.is_numeric = is_numeric
        
        if self.is_numeric:
            self.convert_func = float
        else:
            self.convert_func = str
            
        try:
            self.var_data = self.__init_var(var_data)
        except ValueError:
            self.var_data = self.__init_var(default_data)

    def __init_var(self, var_data):
        loaded_data = {}
        
        for key, value in var_data.items():
            loaded_data[key] = self.convert_func(value)
        self.__check_range(loaded_data, loaded_data.get('value'))

        return loaded_data
    
    def __check_range(self, var_data, value):
        if self.is_numeric and (
            var_data.get('max_value') < value or
            var_data.get('min_value') > value
        ):
            err = f"Getting out of range while trying to check `{self.name}` variable."
            raise ValueError(err)

    def set_value(self, value):
        try:
            value = self.convert_func(value, field_name='value')
        except ValueError:
            print("Failed due to inappropriate type of data.")
            return
            
        try:
            self.__check_range()
        except ValueError:
            print(f"Getting out of range while trying to check `{self.name}` variable.")
            return

        self.var_data['value'] = value

    def get_value(self):
        return self.var_data.get('value')
