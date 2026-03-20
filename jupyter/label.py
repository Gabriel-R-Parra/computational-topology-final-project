from dataclasses import dataclass
import pandas as pd
from metadata import get_json
from itertools import product
import os

@dataclass
class Label:
    """
        Labels store the parameters of a trial and allow ease of access to the data associated with the trial.
    """
    subject: str
    condition: str
    activity: str
    
    def __repr__(self):
        return f"{self.subject}-{self.condition}-{self.activity}"

    def __hash__(self):
        return hash((self.subject, self.condition, self.activity))

    def __eq__(self, other):
        if not isinstance(other, Label):
            return False
        return (self.subject, self.condition, self.activity) == (other.subject, other.condition, other.activity)

    def __lt__(self, other):
        return (self.subject, self.condition, self.activity) < (other.subject, other.condition, other.activity)        

    @staticmethod
    def from_tuple(label):
        return Label(label[0], label[1], label[2])

    def _data_path(self):
        return f"{get_json('data_path')}/{self}.csv"

    def to_dataframe(self):
        assert os.path.exists(self._data_path()), f"Error parsing data path: {self._data_path()}"
        return pd.read_csv(self._data_path(), index_col="Ros Timestamp (ns)")

        
def label_filter(subject, condition, activity):
    """
        Creates a filter function for a set of labels.

        If 'field = None' then there is no filter applied to the labels on 'field'.

        e.g.
            subject = "01", only labels where subject = "01" will be returned.
            activity = None, no filter applied to activity field on label.
            To get all of subject 01's data in condition 01, (subject="01", condition="01", activity=None).
    """
    filter_label = Label(subject, condition, activity)
    def data_filter(label):
        conditions = [
            lambda cl: filter_label.subject == None or filter_label.subject == cl.subject,
            lambda cl: filter_label.condition == None or filter_label.condition == cl.condition,
            lambda cl: filter_label.activity == None or filter_label.activity == cl.activity,
        ]
        return all([check(label) for check in conditions])
    return data_filter


class LabelDataset:
    """
        Manages groups of labels s.t. it is easier to manage the data that is being observed.
    """
    def __init__(self, data_filter=label_filter(None, None, None)):
        subjects = sorted(get_json("subjects"))
        conditions = sorted(get_json("conditions"))
        activities = sorted(get_json("activities"))
        self.labels = map(Label.from_tuple, product(subjects, conditions, activities))
        self.data_filter = data_filter

    def __iter__(self):
        return self

    def __next__(self):
        for label in self.labels:
            if label.activity == "07" and label.condition == "02" and label.subject == "13":
                continue
            if self.data_filter(label):
                return label
        raise StopIteration


class DataLoader:
    """Quickly loads all data into a multi-indexed dataframe given a label"""
    def __init__(self, data_filter=label_filter(None, None, None)):
        self.trials = sorted([l for l in LabelDataset(data_filter)])
        dataframes = list(map(lambda t: t.to_dataframe(), self.trials)) 
        data = pd.concat(dataframes, keys=self.trials, names=["Trial"]) 
        self.data = data

    def get_trials(self):
        return self.trials

    def get_data(self):
        return self.data






        