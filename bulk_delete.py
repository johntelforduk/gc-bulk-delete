from beautiful_date import Jan
from gcsa.google_calendar import GoogleCalendar

calendar = GoogleCalendar('myemail@gmail.com')

start = (22/Jan/2023)[12:00]

# Count the number of copies of each event (1 means no copy).
event_dict = {}                 # key=event as string, value=number of copies.
for event in calendar.get_events(time_min=start):
    event_str = str(event)

    if event_str in event_dict:
        event_dict[event_str] = event_dict[event_str] + 1
    else:
        event_dict[event_str] = 1

# Make a dictionary of duplicate events.
duplicate_dict = {}
for key in event_dict:
    value = event_dict[key]

    # The 'None - None' event seems to be some kind of dummy, and doesn't need to be deleted.
    if value > 1 and key != 'None - None':
        duplicate_dict[key] = value

print(duplicate_dict)

# Delete duplicate events.
event_count = 0
for event in calendar.get_events(time_min=start):
    if str(event) in duplicate_dict:
        event_count += 1
        print(event_count, event)
        GoogleCalendar.delete_event(calendar, event)
