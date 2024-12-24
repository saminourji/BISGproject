from ProxyPredictor_interface import ProxyPredictor 
import surgeo

class BISGPredictor(ProxyPredictor):
    def inference(self, data):
        """
        Parameters: data (pandas.DataFrame)
        Output: pandas.DataFrame with race predicitons using proxy
        """