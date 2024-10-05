import os
import time
import logging
from instagrapi import Client
from dotenv import load_dotenv
from requests.exceptions import HTTPError

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(filename='insta_close_friends.log', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Instagram credentials
USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')

# Instagram API Client Setup
cl = Client()

# Login function with retry mechanism
def login_to_instagram():
    try:
        cl.login(USERNAME, PASSWORD)
        logging.info("Successfully logged in to Instagram.")
    except Exception as e:
        logging.error(f"Login failed: {e}")
        raise

# Fetch followers function with retry and rate-limiting handling
def get_followers(user_id):
    try:
        followers = cl.user_followers(user_id)
        logging.info(f"Successfully retrieved {len(followers)} followers.")
        return followers
    except HTTPError as e:
        logging.error(f"HTTP error occurred while fetching followers: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to fetch followers: {e}")
        raise

# Add followers to close friends list using the correct method
def add_followers_to_close_friends(followers):
    follower_ids = [follower.pk for follower in followers.values()]
    
    # Instagram has API limits, so we do this in batches
    batch_size = 10
    for i in range(0, len(follower_ids), batch_size):
        batch = follower_ids[i:i + batch_size]
        try:
            for follower_id in batch:
                result = cl.close_friend_add(follower_id)  # Correct method from the documentation
                if result:
                    logging.info(f"Successfully added follower {follower_id} to close friends.")
                else:
                    logging.warning(f"Failed to add follower {follower_id} to close friends.")
        except HTTPError as e:
            logging.error(f"HTTP error occurred while adding followers to close friends: {e}")
        except Exception as e:
            logging.error(f"Failed to add follower to close friends: {e}")
        
        time.sleep(2)  # Sleep to avoid rate-limiting

# Main function to run the script
def main():
    try:
        # Log in to Instagram
        login_to_instagram()

        # Get user ID
        user_id = cl.user_id_from_username(USERNAME)

        # Fetch followers
        followers = get_followers(user_id)

        # Add followers to close friends list
        add_followers_to_close_friends(followers)

        logging.info("Successfully added all followers to the close friends list.")
        
    except Exception as e:
        logging.error(f"An error occurred during the execution: {e}")

if __name__ == "__main__":
    main()
