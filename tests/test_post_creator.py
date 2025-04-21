import os
import sys

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from automation.linkedin_automation import create_driver, load_credentials, login_linkedin
from automation.post_creator import create_linkedin_post

if __name__ == "__main__":
    creds = load_credentials()
    driver = create_driver()

    if login_linkedin(driver, creds["username"], creds["password"]):
        mode = input("📝 Post type?\n1. Caption Only\n2. Caption + Image\nEnter 1 or 2: ").strip()

        caption = input("🧾 Enter your post caption:\n")

        image_path = None
        if mode == "2":
            image_path = input("🖼️ Enter full image path:\n").strip()

        # 🔁 New prompt for smart hashtag detection
        smart_input = input("🤖 Use smart topic + hashtag detection? [y/n]: ").strip().lower()
        smart_mode = smart_input == "y"

        create_linkedin_post(driver, caption, image_path, smart=smart_mode)
    else:
        print("❌ Login failed. Cannot proceed.")

    driver.quit()
