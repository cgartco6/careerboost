# utils/media_generator.py
class MediaGenerator:
    def __init__(self):
        self.ffmpeg_path = os.getenv('FFMPEG_PATH', 'ffmpeg')
        self.temp_dir = 'temp_media'
        
    def generate_voiceover(self, text, voice_type='professional'):
        """Generate professional voiceover from text"""
        try:
            # Use text-to-speech service
            tts_service = TextToSpeechService()
            audio_file = tts_service.convert_text_to_speech(
                text=text,
                voice=voice_type,
                output_format='mp3'
            )
            
            return audio_file
        except Exception as e:
            logging.error(f"Voiceover generation failed: {e}")
            return self.get_fallback_audio()
    
    def create_video_with_voiceover(self, visuals, audio, output_path):
        """Create video by combining visuals with voiceover"""
        try:
            # Combine images/video with audio
            subprocess.run([
                self.ffmpeg_path,
                '-i', visuals,
                '-i', audio,
                '-c:v', 'libx264',
                '-c:a', 'aac',
                '-strict', 'experimental',
                output_path
            ], check=True)
            
            return output_path
        except Exception as e:
            logging.error(f"Video creation failed: {e}")
            return None
    
    def generate_province_specific_visuals(self, province, content_type):
        """Generate visuals specific to a province"""
        # Get province-specific images and footage
        province_assets = self.get_province_assets(province)
        
        if content_type == 'short_video':
            return self.create_short_video_sequence(province_assets)
        elif content_type == 'reel':
            return self.create_reel_sequence(province_assets)
        elif content_type == 'photo_carousel':
            return self.create_photo_carousel_sequence(province_assets)
            
    def get_province_assets(self, province):
        """Get visual assets for a specific province"""
        assets = {
            'landmarks': self.get_province_landmarks(province),
            'scenery': self.get_province_scenery(province),
            'urban_areas': self.get_urban_areas(province),
            'work_environments': self.get_work_environments(province)
        }
        
        return assets
