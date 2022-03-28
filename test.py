from turtle import clear
from api.firebase import FirebaseCRUD
import csv
# tags are something the user will follow
# keywords are something we will use to categorize that post

## Example
# Job Title: Graphic Designer
#
# Company: Spectrum Brand Solutions PLC
#
# Job Type: Permanent
#
# Description: Join the Spectrum Brand Solutions Team,  a creative communications company that helps businesses grow their brands in the market to reach their audience + spark conversations through Brand Strategy,  Identity, Digital Marketing Print Solutions.
#
# We are Looking For a passionate Graphic designer to join the creative team  on permanent basis who is able to
# • Collaborate and come up with creative artwork.
# • Comfortably operate at least two or three of Adobe creative cloud applications.
# • Create and design various materials for print and digital marketing materials
# •   Able to make revisions as per design specifications and client comments

# tags for the above posts are
# graphic designer, adobe

# keywords are
# designer

# NOTE :  tags are visible to users and are followed, keywords are used only internally
firebase_crud = FirebaseCRUD()
global_config = firebase_crud.get_global_config()
categories = global_config["categories"]

with open('categories.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    cat = []
    for category in categories:
        cat.append(category["name"])

    writer.writerow(cat)

    for category in categories:
        writer.writerow(category["tags"])
