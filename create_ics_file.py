import ics

example1 = {
    "Title": "Korean 2",
    "Events": {
        "HW1": "2023-2-15 00:00:00",
        "HW2": "2023-3-15 00:00:00",
        "Exam 1": "2023-2-27 00:00:00",
        "Exam 2": "2023-4-13 00:00:00",
        "Final Exam": "2023-5-10 00:00:00"
    }
}

def create_calendar(pdf_dates: dict):

    name = pdf_dates["Title"]
    events = pdf_dates["Events"]

    c = ics.Calendar()

    for event in events:
        e = ics.Event(name=event, begin=events[event])
        e.make_all_day()
        c.events.add(e)


    with open(name+'.ics', 'w') as f:
        f.writelines(c.serialize_iter())
