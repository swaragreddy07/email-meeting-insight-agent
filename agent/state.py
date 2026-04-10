from typing import TypedDict, List, Dict

class State(TypedDict):
    emails:List[str]
    entities: Dict[str, str]
    summary:str 
    memory:List[str]