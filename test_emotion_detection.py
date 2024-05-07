import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    A test class to verify the functionality of the emotion_detector function.
    """
    
    def test_emotion_detector(self):
        """
        A test method to verify if emotion_detector returns the correct dominant emotion label.
        """
        # Test joy emotion
        test_res1 = emotion_detector("I am glad this happened")
        self.assertEqual(test_res1["dominant_emotion"], "joy")

        # Test anger emotion
        test_res2 = emotion_detector("I am really mad about this")
        self.assertEqual(test_res2["dominant_emotion"], "anger")

        # Test sadness emotion
        test_res3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_res3["dominant_emotion"], "disgust")

        # Test sadness emotion
        test_res4 = emotion_detector("I am so sad about this")
        self.assertEqual(test_res4["dominant_emotion"], "sadness")

        # Test fear emotion
        test_res5 = emotion_detector("I am really afraid that this will happen	")
        self.assertEqual(test_res5["dominant_emotion"], "fear")

if __name__ == '__main__':
    unittest.main()