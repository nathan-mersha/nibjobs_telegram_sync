from api.firebase import FirebaseCRUD

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

categories = [
    {
        "icon": "some icon",
        "name": "architecture and engineering",
        "tags": [
            "mechanical",
            "Technician",
            "biomedical",
            "Electrical",
            "architecture",
            "network",
            "Revit",
            "AutoCAD",
            "industrial",
            "garment engineering",
            "textile engineering",
            "hardware engineering"
        ],

    },

    {
        "icon": "some icon",
        "name": "graphics",
        "tags": [
            "adobe",
            "illustrator",
            "after effect",
            "davinci resolve",
            "photoshop",
            "photographer",
            "designer",
            "creative_design",
            "production manager"
        ],

    },

    {
        "icon": "some icon",
        "name": "business & administration",
        "tags": [
            "manager",
            "distribution manager",
            "human resource manager",
            "Marketing",
            "customer relation",
            "administrator",
            "Accountant",
            "Director",
            "Purchaser",
            "finance",
            "Assistant",
            "Driver Supervisor",
            "Secretary",
            "business_services",
            "store keeper",
            "project management"
        ],
    },

    {
        "icon": "some icon",
        "name": "education",
        "tags": [
            "tutor",
            "Dean",
            "Teacher",
            "instructor",
            "education officer"
        ],
    },

    {
        "icon": "some icon",
        "name": "service & maintenance",
        "tags": [
            "Waiter",
            "Cashier",
            "Coach",
            "Driver",
            "Receptionist",
            "Chef",
            "Agent",
            "Translator",
            "Content writer",
            "writer",
            "trainer",
            "Interpreter",
            "Office Manager",
            "coordinator",
            "promoter",
            "Customer Support",
            "transcriptionist",
            "social media booster",
            "cook",
            "guard"
        ],

    },

    {
        "icon": "some icon",
        "name": "health & medicine",
        "tags": [
            "Nurse",
        ],
    },

    {
        "icon": "some icon",
        "name": "sales",
        "tags": [
            "sales",
            "business_services",
            "customer support"
        ],
    },

    {
        "icon": "some icon",
        "name": "Software Engineering",
        "tags": [
            "seo",
            "html",
            "Java",
            "Python",
            "C++",
            "C#",
            "Assembly language",
            "ios",
            "Groovy",
            "Angular",
            "React",
            "Data analyst",
            "Vue.js",
            "Ember.js",
            "Front-end",
            "AWS",
            "Boto3",
            "Full stack",
            "back-end",
            "WordPress",
            "Flutter",
            "dart",
            "Scss/Sass",
            "Meteor",
            "Node.js",
            "next.js",
            "Backbone.js",
            "SQL",
            "PHP",
            "Visual Basic",
            "css",
            "onion",
            "Oracle",
            "APEX",
            "javascript",
            "bootstrap",
            "Blockchain",
            "php",
            "MERN",
            "hacker",
            "Laravel",
            "IT Support",
            "ethereum",
            "solana",
            "avalanche",
            "cardano"
        ],

    },

]

# clean up
for category in categories:
    category["name"] = category["name"].lower()
    for t in category["tags"]:
        index = category["tags"].index(t)
        category["tags"][index] = t.lower().replace("-"," ").replace("_", " ")
    category["tags"] = list(set(category["tags"]))

global_config["categories"] = categories
firebase_crud.update_global_config(global_config=global_config)
