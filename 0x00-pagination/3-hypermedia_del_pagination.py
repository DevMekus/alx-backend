#!/usr/bin/env python3
"""Module: Deletion-resilient
"""
import csv
from typing import Dict, List


class Server:
    """Function Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor Initializes a new Server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Function to Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Function to Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Function that Retrieves info about a page from a given index and with a
        specified size.
        """
        data = self.indexed_dataset()
        assert index is not None and index >= 0 and index <= max(data.keys())
        pageData = []
        counter = 0
        nextIndex = None
        start = index if index else 0
        for i, item in data.items():
            if i >= start and counter < page_size:
                pageData.append(item)
                counter += 1
                continue
            if counter == page_size:
                nextIndex = i
                break
        page_info = {
            'index': index,
            'nextIndex': nextIndex,
            'page_size': len(pageData),
            'data': pageData,
        }
        return page_info
