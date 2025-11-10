# ai_agents/auto_posting.py
class AutoPostingAgent:
    def __init__(self):
        self.platforms = {
            'tiktok': TikTokAPI(),
            'facebook': FacebookAPI(),
            'instagram': InstagramAPI(),
            'linkedin': LinkedInAPI(),
            'twitter': TwitterAPI(),
            'youtube': YouTubeAPI()
        }
        self.content_queue = []
        self.posting_schedule = self.load_posting_schedule()
        
    def auto_post_content(self):
        """Automatically post content to all platforms according to schedule"""
        current_time = datetime.now()
        
        for platform, schedule in self.posting_schedule.items():
            if self.should_post_now(platform, current_time):
                content = self.get_content_for_platform(platform)
                if content:
                    self.post_to_platform(platform, content)
                    
    def post_to_platform(self, platform, content):
        """Post content to specific platform"""
        try:
            if platform == 'tiktok':
                self.platforms[platform].upload_video(
                    video_path=content['video_path'],
                    caption=content['caption'],
                    hashtags=content['hashtags']
                )
            elif platform in ['facebook', 'instagram', 'linkedin']:
                if content['type'] == 'image':
                    self.platforms[platform].upload_photo(
                        image_path=content['image_path'],
                        caption=content['caption']
                    )
                else:  # video
                    self.platforms[platform].upload_video(
                        video_path=content['video_path'],
                        caption=content['caption']
                    )
            elif platform == 'youtube':
                self.platforms[platform].upload_video(
                    video_path=content['video_path'],
                    title=content['title'],
                    description=content['description'],
                    tags=content['tags']
                )
                    
            print(f"Successfully posted to {platform}")
            self.log_post(platform, content)
            
        except Exception as e:
            print(f"Error posting to {platform}: {e}")
            self.handle_posting_error(platform, content, e)
