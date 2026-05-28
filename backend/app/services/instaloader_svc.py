import instaloader
import os
from datetime import datetime, timedelta

# Initialize Instaloader
# We disable video downloads and extra metadata to keep things clean and fast
L = instaloader.Instaloader(
    download_videos=False,
    download_video_thumbnails=False,
    save_metadata=False,
    download_comments=False
)

STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "feed")

def sync_daily_feed(profile_names: list, days_limit: int = 7):
    """
    Downloads images and extracts metadata for given profiles.
    You would typically run this once a day via a Cron job or Celery.
    """
    cutoff_date = datetime.now() - timedelta(days=days_limit)
    feed_data = []

    for username in profile_names:
        try:
            profile = instaloader.Profile.from_username(L.context, username)
            
            for post in profile.get_posts():
                # Stop if the post is older than our cutoff
                if post.date_utc < cutoff_date:
                    break
                    
                # Download the post to our static/feed directory
                # Instaloader will save the image locally
                L.download_post(post, target=STATIC_DIR)
                
                # Append to our data structure (later to be saved in DB/Redis)
                feed_data.append({
                    "shortcode": post.shortcode,
                    "author": username,
                    "caption": post.caption,
                    "date": post.date_utc.isoformat(),
                    # Instaloader creates filenames based on date usually, 
                    # but you have to map it based on expected download path
                    "local_image": f"/static/feed/{post.date_utc:%Y-%m-%d_%H-%M-%S}_UTC.jpg"
                })
        except Exception as e:
            print(f"Error fetching {username}: {e}")

    # Here you would save `feed_data` to Postgres/Redis
    return feed_data
