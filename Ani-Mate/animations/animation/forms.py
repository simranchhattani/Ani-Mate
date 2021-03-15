from django import forms
from .models import Feedback, Video

class FeedbackForm (forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_name', 'feedback_email','feedback_content']

class VideoForm (forms.ModelForm):
    class Meta:
        model=Video
        fields = ['video_user_name','video_email', 'video_title','video_file','video_article' ]
