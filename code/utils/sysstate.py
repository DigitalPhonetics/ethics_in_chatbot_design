from utils.transmittable import Transmittable
from utils.sysact import SysAct

class SysState(Transmittable):

    def __init__(self, last_act: SysAct = None, last_offer: str = None, last_request_slot: str = None, lastInformedPrimKeyVal: str = None):
        self.last_act = last_act
        self.last_offer = last_offer
        self.last_request_slot = last_request_slot
        self.lastInformedPrimKeyVal = lastInformedPrimKeyVal

    def serialize(self):
        return {
            'last_act': self.last_act.serialize(),
            'last_offer': self.last_offer,
            'last_request_slot': self.last_request_slot,
            'lastInformedPrimKeyVal': self.lastInformedPrimKeyVal
        }

    @staticmethod
    def deserialize(obj: dict):
        serialized_last_act = obj['last_act']
        last_act = SysAct.deserialize(serialized_last_act) if serialized_last_act else None
        return SysState(last_act=last_act, last_offer=obj['last_offer'], last_request_slot=obj['last_request_slot'], lastInformedPrimKeyVal=obj['lastInformedPrimKeyVal'])