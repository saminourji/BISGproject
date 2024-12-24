from abc import ABC, abstractmethod

class ProxyPredictor(ABC):
    @abstractmethod
    def inference(self, data):
        """
        Parameters: data (pandas.DataFrame)
        Output: pandas.DataFrame with race predicitons using proxy
        """
        pass