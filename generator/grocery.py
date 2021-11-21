from .utils import csvutils, conutils
import logging

LOGGER = logging.getLogger("grocery")

class Generator:

    def __init__(self, csv_filepath, url = None):
        self.csv_filepath = csv_filepath
        self.csv = csvutils.CSVUtils(self.csv_filepath)
        if url:
            self.url = url
        else:
            self.url = None

    '''
    Perform CSV to nested JSON conversion and return resulting JSON.
    '''
    def convert(self):
        json_struct = {}
        try:
            data = self.csv.get_data_rows()
            json_struct = self.populate_structure_with_data(data)
        except Exception as err:
            raise
        return json_struct
        
    '''
    Returns dictionary with given data rows fitted to given structure.
    '''
    def populate_structure_with_data(self, data):
        root = conutils.Node('grocery')
        for row in data:
            row = row[1:]
            if row and all(row):
                num_of_levels = int(len(row)/3)
                if len(row)%3 == 0:
                    child_nodes= []
                    visited = False
                    for i in range(num_of_levels):
                        if not visited:
                            j =i
                            if self.url:
                                row[j+2] = row[j+2].replace('/groceries.abc.com', self.url)
                            child_node = root.add_child(row[j:j+3])
                            visited = True
                        elif visited:
                            j += 3
                            if self.url:
                                row[j+2] = row[j+2].replace('/groceries.abc.com', self.url)
                            child_node = child_node.add_child(row[j:j+3])
                else:
                    LOGGER.error("Required parameters not provided for a level")
                    raise 
        return root




