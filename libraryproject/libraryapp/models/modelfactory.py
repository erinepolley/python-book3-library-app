import sqlite3

# Higher order function to create instances of models
# when performing single table queries
def model_factory(model_type):
    def create(cursor, row):
        #makes empty instance of Class(ex. Book)
        instance = model_type()
        smart_row = sqlite3.Row(cursor, row)
        for col in smart_row.keys():
            # Like saying book, title, whatever value is coming from database
            setattr(instance, col, smart_row[col])
        return instance
    return create