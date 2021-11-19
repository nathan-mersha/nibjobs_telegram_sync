import os

# todo : change this to production when pushing
os.environ["MODE"] = "prod"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./cred/nib-job-finder-firebase-adminsdk-9y8l0-aca148cd64.json"
from lib.scheduler import ShopScheduler


def main():
    print("starting sync script")
    ShopScheduler.sync_job_channels()
    print("done running sync script")

    # to populate mobile cards
    # mobile_cards_populate = MobileCardPopulate()
    # mobile_cards_populate.populate()

    os._exit(0)


if __name__ == "__main__": main()
