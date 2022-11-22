import json
from quality import get_quality_score


class QUALITY_CHECKER:
    def __init__(self, model_path):
        self.quality_score_limit = 60
        self.quality_model_path = model_path

    def get_quality_score(self, img):
        return get_quality_score(img, self.quality_model_path)

    def is_good_quality(self, img):
        validity = {
            'isvalid' : False,
            'reason' : '',
            'quality_score' : 0
        }

        quality_score = self.get_quality_score(img)
        
        if quality_score > 100:
            quality_score -= 100
            
        reverse_quality_score = 100.0 - quality_score
        validity['quality_score'] = reverse_quality_score
        
        
        if reverse_quality_score < self.quality_score_limit:
            validity['reason'] = 'Poor quality image. Make sure to upload image without blur and in good lighting conditions and no reflections.'
        else:
            validity['reason'] = 'Good quality image'
            validity['isvalid'] = True
        
        print(f'Is Good Quality : {validity["isvalid"]}, Reason : {validity["reason"]}, Quality Score : {reverse_quality_score}')