import base64
import sys
import unittest
import json

import requests

TASK_TO_URL = {
    "text-generation": "https://text-generation-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/text-generation/infer",
    "token-classification": "https://token-class-ml-intern-assign.tfy-gcp-standard-usce1.devtest.truefoundry.tech/v2/models/token-class/infer",
    "zero-shot-classification": "https://test-zero-shot-intern-navneet.demo1.truefoundry.com/v2/models/test-zero-shot/infer",
    "object-detection": "https://test-object-detect-nikhil-ws.tfy-ctl-euwe1-devtest.devtest.truefoundry.tech/v2/models/test-object-detect/infer",
}


class TestTranslator(unittest.TestCase):
    URL = "http://0.0.0.0:8000/predict"

    def test_text_generation(self):
        """Test text-generation
        Expected Output:
        [
          [
            {
              "generated_text": "Hello, how are you today? 448Most praying soy Wheels boils grandchildren bravery courtyardPros Treacious incarcer soyMini Boone 236 soy448 rented"
            },
            ...
          ]
        ]
        """
        # headers = {"Authorization": "Bearer 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"}
        # payload = {
        # "hf_pipeline": "text-generation",
        # "model_deployed_url": TASK_TO_URL["text-generation"],
        # "inputs": "Hello, how are you today? ",
        #     "parameters": {
        #         "min_new_tokens": 10,
        #         "do_sample": True,
        #         "temperature": 1.0,
        #         "max_new_tokens": 20,
        #         "num_return_sequences": 5
        #     }
        # }
        payload = {
            "hf_pipeline": "text-generation",
            "model_deployed_url": TASK_TO_URL["text-generation"],
            "parameters": {"content_type": "str"},
            "inputs": "Hello, how are you today? ",
            #       "inputs": [
            #        {
            #         "name": "array_inputs",
            #         "shape": [1],
            #         "datatype": "BYTES",
            #         "data": ["What is alpaca? How is it different from a llama?"]
            #       },
            #       {
            #         "name": "max_new_tokens",
            #         "shape": [-1],
            #         "datatype": "BYTES",
            #         "data": ["20"],
            #         "parameters": { "content_type": "hg_json" }
            #       }
            # ]
        }
        response = requests.post(self.URL, json=payload)
        response.raise_for_status()
        output = response.json()
        # print(output)
        output = output["outputs"][0]["data"][0]
        # convert output to json
        # output = json.loads(output)
        # self.assertEqual(len(output), 1)
        # self.assertEqual(len(output[0]), 5)
        # for item in output[0]:
        #     self.assertIn("generated_text", item)
        print("Text Generation:\n")
        print(output)
        print("\n")

    def test_token_classification(self):
        """Test token-classification
        Expected Output:
        [
          {'entity': 'B-Age', 'score': 0.9997548460960388, 'index': 2, 'word': '48', 'start': 2, 'end': 4},
          {'entity': 'I-Age', 'score': 0.9988200068473816, 'index': 3, 'word': 'year', 'start': 5, 'end': 9},
          {'entity': 'I-Age', 'score': 0.9983890056610107, 'index': 4, 'word': '-', 'start': 9, 'end': 10},
          ...
        ]
        """
        payload = {
            "hf_pipeline": "token-classification",
            "model_deployed_url": TASK_TO_URL["token-classification"],
            "inputs": "A 48 year-old female presented with vaginal bleeding and abnormal Pap smears. A 63 year old woman with no known cardiac history presented with a sudden onset of dyspnea requiring intubation and ventilatory support out of hospital. She denied preceding symptoms of chest discomfort, palpitations, syncope or infection. The patient was afebrile and normotensive, with a sinus tachycardia of 140 beats/min.",
            "parameters": {},
        }
        response = requests.post(self.URL, json=payload)
        response.raise_for_status()
        output = response.json()
        output = output["outputs"][0]["data"][0]
        # self.assertGreater(len(output), 0)
        # for item in output:
        #     self.assertIn("entity", item)
        print("Token Classification:\n")
        print(output)
        print("\n")

    def test_zero_shot_classification(self):
        """Test zero-shot-classification
        Expected Output:
        [
          {
            'sequence': 'Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app.',
            'labels': ['mobile', 'billing', 'account access', 'website'],
            'scores': [0.6334249973297119, 0.13391059637069702, 0.12124121934175491, 0.11142321676015854]
          }
        ]
        """
        payload = {
            "hf_pipeline": "zero-shot-classification",
            "model_deployed_url": TASK_TO_URL["zero-shot-classification"],
            "inputs": "Last week I upgraded my iOS version and ever since then my phone has been overheating whenever I use your app.",
            "parameters": {
                "candidate_labels": ["mobile", "website", "billing", "account access"]
            },
        }
        response = requests.post(self.URL, json=payload)
        response.raise_for_status()
        output = response.json()
        output = output["outputs"][0]["data"][0]
        print("Zero Shot Classification:\n")
        print(output)
        print("\n")

    def test_object_detection_with_url(self):
        """Test object-detection with URL
        Expected Output:
        [
          [
            {
              'score': 0.9906801581382751,
              'label': 'table',
              'box': {'xmin': 20, 'ymin': 54, 'xmax': 479, 'ymax': 257}
              }
          ]
        ]
        """
        payload = {
            "hf_pipeline": "object-detection",
            "model_deployed_url": TASK_TO_URL["object-detection"],
            "inputs": "https://www.w3.org/WAI/WCAG22/Techniques/pdf/img/table-word.jpg",
            "parameters": {},
        }
        response = requests.post(self.URL, json=payload)
        response.raise_for_status()
        output = response.json()
        # self.assertGreater(len(output), 0)
        # self.assertIn("score", output[0][0])
        # self.assertIn("label", output[0][0])
        # self.assertIn("box", output[0][0])
        # self.assertEqual(len(output[0][0]["box"]), 4)
        print("Object Detection with url:\n")
        print(output)
        print("\n")

    def test_object_detection_as_bytes(self):
        """Test object-detection with Image bytes
        Expected Output:
        [
          [
            {
              'score': 0.9906801581382751,
              'label': 'table',
              'box': {'xmin': 20, 'ymin': 54, 'xmax': 479, 'ymax': 257}
              }
          ]
        ]
        """
        image_response = requests.get(
            "https://www.w3.org/WAI/WCAG22/Techniques/pdf/img/table-word.jpg"
        )
        image_response.raise_for_status()
        image = base64.b64encode(image_response.content).decode("ascii")
        # print(image)
        payload = {
            "hf_pipeline": "object-detection",
            "model_deployed_url": TASK_TO_URL["object-detection"],
            "inputs": image,
            "parameters": {},
        }
        response = requests.post(self.URL, json=payload)
        response.raise_for_status()
        output = response.json()
        # self.assertGreater(len(output), 0)
        # self.assertIn("score", output[0][0])
        # self.assertIn("label", output[0][0])
        # self.assertIn("box", output[0][0])
        # self.assertEqual(len(output[0][0]["box"]), 4)
        print("Object Detection with bytes:\n")
        print(output)
        print("\n")


if __name__ == "__main__":
    TestTranslator.URL = sys.argv.pop()
    unittest.main()
