# dummy_data.py

matters = ["Select a Matter", "Matter 1", "Matter 2", "Matter 3"]
elements = {
    "Matter 1": ["Select an Element", "Element A1", "Element B1", "Element C1"],
    "Matter 2": ["Select an Element", "Element A2", "Element B2", "Element C2"],
    "Matter 3": ["Select an Element", "Element A3", "Element B3", "Element C3"],
}
facts = {
    "Matter 1": {"Element A1": "Fact for Matter 1 - Element A1", "Element B1": "Fact for Matter 1 - Element B1"},
    "Matter 2": {"Element A2": "Fact for Matter 2 - Element A2", "Element B2": "Fact for Matter 2 - Element B2"},
    "Matter 3": {"Element A3": "Fact for Matter 3 - Element A3", "Element B3": "Fact for Matter 3 - Element B3"},
}
evidence_documents = {
    "Matter 1": {"Element A1": ["Tweet 1A1", "Tweet 2A1"], "Element B1": ["Tweet 1B1", "Tweet 2B1"]},
    "Matter 2": {"Element A2": ["Tweet 1A2", "Tweet 2A2"], "Element B2": ["Tweet 1B2", "Tweet 2B2"]},
    "Matter 3": {"Element A3": ["Tweet 1A3", "Tweet 2A3"], "Element B3": ["Tweet 1B3", "Tweet 2B3"]},
}
explanations = {
    "Matter 1": {"Element A1": "Explanation for Matter 1 - Element A1", "Element B1": "Explanation for Matter 1 - Element B1"},
    "Matter 2": {"Element A2": "Explanation for Matter 2 - Element A2", "Element B2": "Explanation for Matter 2 - Element B2"},
    "Matter 3": {"Element A3": "Explanation for Matter 3 - Element A3", "Element B3": "Explanation for Matter 3 - Element B3"},
}
