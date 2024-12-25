import sys
import os

# Add the current directory to the sys.path to ensure Python can find ProxyPredictor_interface
sys.path.append(os.getcwd())

# Import ProxyPredictor class
from ProxyPredictor_interface import ProxyPredictor
import surgeo

class BISGPredictor(ProxyPredictor):
    def __init__(self):
        super().__init__()
        self.sg = surgeo.SurgeoModel()

    def inference(self, data):
        """
        Parameters: data (pandas.DataFrame) with columns "last_name" and "zip_code"
        Output: pandas.DataFrame with race predicitons using proxy
        """
        surnames = data["last_name"].as_type(str)
        zctas = data["zip_code"].as_type(str)
        return self.sg.get_probabilities(surnames, zctas)