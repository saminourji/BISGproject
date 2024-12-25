from predictors.ProxyPredictor_interface import ProxyPredictor
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
        surnames = data["last_name"].astype(str)
        zctas = data["zip_code"].astype(str)
        return self.sg.get_probabilities(surnames, zctas)