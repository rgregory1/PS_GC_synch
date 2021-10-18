import pathlib, datetime
from file_grabber import grab_files
from getmac import get_mac_address as gma

cwd = pathlib.Path.cwd()


timestamp = datetime.datetime.now()
print("\n\n" + str(timestamp))
# home mac address is a4:83:e7:72:41:a3
print(gma())
mac_address = str(gma())

today = str(datetime.datetime.now().strftime("%Y-%m-%d"))
print(today)

pre_file_list = [
    "schedule_middle_school.tsv",
    "sections_middle_school.tsv",
    "schedule_high_school.tsv",
    "sections_high_school.tsv",
]

file_list = [today + "-" + file_name for file_name in pre_file_list]


grab_files(
    file_list,
    cwd,
)

# move files
for file in file_list:
    my_file = cwd / "data_files" / file
    if mac_address == "a4:83:e7:72:41:a3":
        to_file = "/Users/rgregory/Documents/trial/" + file
        my_file.rename(to_file)
    else:
        to_file = "/Users/admin/Documents/PS_GC_synch/" + file
        my_file.rename(to_file)

# hello
