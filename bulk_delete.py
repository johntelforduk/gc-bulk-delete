from beautiful_date import Jan
from gcsa.google_calendar import GoogleCalendar

CALENDAR_ID = 'youremail AT gmail.com'
START = (1/Jan/2023)[12:00]
TEST = False

calendar = GoogleCalendar(CALENDAR_ID)

found_events = []
event_count = 0

for event in calendar.get_events(time_min=START):
    event_str = str(event)

    if event_str in found_events:
        event_count += 1
        if TEST:
            message = "Test mode. Would have deleted: "
        else:
            message = "Live mode. Event deleted: "
            GoogleCalendar.delete_event(calendar, event)

        message += event_str + ". Total events: " + str(event_count)
        print(message)

    else:
        found_events.append(event_str)
