from django import template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import cv2
from scipy.stats import entropy
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from scipy import fft
import warnings
warnings.filterwarnings('ignore')

register = template.Library()

class AIImageDetector:
    def __init__(self):
        # Initialize ResNet model for feature extraction
        self.model = ResNet50(weights='imagenet', include_top=False)
        
    def load_and_preprocess_image(self, img_array):
        """Preprocess the image for feature extraction."""
        img_array = cv2.resize(img_array, (224, 224))
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        return img_array

    def extract_deep_features(self, img_array):
        """Extract deep features using ResNet."""
        img_array = self.load_and_preprocess_image(img_array)
        features = self.model.predict(img_array)
        return np.mean(features)

    def analyze_color_distribution(self, img_array):
        """Analyze color distribution patterns."""
        channels = cv2.split(img_array)
        color_entropy = []
        
        for channel in channels:
            hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
            hist = hist.flatten() / hist.sum()
            color_entropy.append(entropy(hist))
            
        return np.mean(color_entropy)

    def analyze_noise_patterns(self, img_array):
        """Analyze noise patterns in the image."""
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY) if len(img_array.shape) == 3 else img_array
        dft = fft.fft2(gray)
        dft_shift = fft.fftshift(dft)
        magnitude_spectrum = np.abs(dft_shift)
        freq_dist = np.mean(magnitude_spectrum)
        return freq_dist

    def detect_artifacts(self, img_array):
        """Detect common AI generation artifacts."""
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edge_coherence = np.mean(edges) / 255.0
        return edge_coherence

    def check_metadata_consistency(self, img):
        """Check image metadata for inconsistencies."""
        try:
            exif = img._getexif()
            if exif is None:
                return False  # No EXIF data often indicates AI generation
            
            # Check for common EXIF fields that real photos typically have
            essential_tags = [271, 272, 274, 305, 306]  # Common EXIF tags
            present_tags = sum(1 for tag in essential_tags if tag in exif)
            
            return present_tags >= 2  # At least 2 essential tags should be present
            
        except Exception:
            return False

    def classify_image(self, img_array):
        """Classify the image based on various signals."""
        signals = {
            'metadata': self.check_metadata_consistency(img_array),
            'deep_features': self.extract_deep_features(img_array),
            'color': self.analyze_color_distribution(img_array),
            'noise': self.analyze_noise_patterns(img_array),
            'artifacts': self.detect_artifacts(img_array)
        }

        # Print signal values for debugging
        print("Signal Values:")
        for key, value in signals.items():
            print(f"{key}: {value}")

        # Decision making based on multiple signals
        score = 0
        
        # Adjust thresholds based on empirical testing
        if signals['metadata']:
            score += 1
            
        if 500 <= signals['noise'] <= 5000:  # Adjusted range for real photos
            score += 1
            
        if signals['color'] > 4.5:  # Higher entropy indicates more natural distribution
            score += 1
            
        if signals['artifacts'] < 0.1:  # Lower values indicate more natural edges
            score += 1
            
        if signals['deep_features'] < 0.5:  # Threshold based on empirical testing
            score += 1
            
        # Final decision
        is_real = score >= 3  # Require at least 3 positive signals to classify as real
        
        return 'real' if is_real else 'AI-generated'

def load_and_preprocess_image(image_data):
    """Load and preprocess image from bytes"""
    img = Image.open(io.BytesIO(image_data))
    img_array = np.array(img)
    
    # Ensure image is in RGB format
    if len(img_array.shape) == 2:  # Grayscale
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2RGB)
    elif img_array.shape[2] == 4:  # RGBA
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
    
    return img, img_array

@register.simple_tag
def detect_ai_image(image_data):
    try: 
        detector = AIImageDetector()
        img, img_array = load_and_preprocess_image(image_data)
        
        # Collect various detection signals
        signals = {
            'metadata': detector.check_metadata_consistency(img),
            'deep_features': detector.extract_deep_features(img_array),
            'color': detector.analyze_color_distribution(img_array),
            'noise': detector.analyze_noise_patterns(img_array),
            'artifacts': detector.detect_artifacts(img_array)
        }
        
        # Decision making based on multiple signals
        score = 0
        
        # Metadata check (real photos usually have consistent metadata)
        if signals['metadata']:
            score += 1
            
        # Noise pattern analysis (AI images often have different noise patterns)
        if 500 <= signals['noise'] <= 5000:  # Typical range for real photos
            score += 1
            
        # Color distribution (AI images often have more uniform distributions)
        if signals['color'] > 4.5:  # Higher entropy indicates more natural distribution
            score += 1
            
        # Artifact detection (AI images often have specific artifacts)
        if signals['artifacts'] > 0.1:  # Real photos tend to have more natural edges
            score += 1
            
        # Deep features analysis
        if signals['deep_features'] < 0.5:  # Threshold based on empirical testing
            score += 1
            
        # Final decision
        # Require at least 3 positive signals to classify as real
        is_real = score >= 3
        
        return 'real' if is_real else 'AI-generated'
        
    except Exception as e:
        return f'Error: {str(e)}' 

