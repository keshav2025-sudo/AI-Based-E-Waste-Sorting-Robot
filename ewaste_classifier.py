
"""
AI-assisted E-Waste Classification Prototype
Uses a pretrained zero-shot image classification model.
"""

import argparse
from pathlib import Path

from PIL import Image
from transformers import pipeline

MODEL_NAME = "openai/clip-vit-base-patch32"

CATEGORIES = [
    "a photograph of a printed circuit board",
    "a photograph of electrical cables and wires",
    "a photograph of a battery",
    "a photograph of electronic components",
]

CONFIDENCE_THRESHOLD = 0.50


def classify_image(image_path):
    """Classify an image and return a prediction or review status."""

    path = Path(image_path)

    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {path}")

    with Image.open(path) as image:
        image = image.convert("RGB")

        predictions = classifier(
            image,
            candidate_labels=CATEGORIES
        )

    best = predictions[0]
    score = best["score"]

    print(f"Predicted category: {best['label']}")
    print(f"Model score: {score:.2%}")

    if score < CONFIDENCE_THRESHOLD:
        print("Decision: MANUAL REVIEW REQUIRED")
    else:
        print("Decision: CANDIDATE CATEGORY - VERIFY BEFORE SORTING")

    return best


classifier = pipeline(
    task="zero-shot-image-classification",
    model=MODEL_NAME
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Classify an e-waste image."
    )
    parser.add_argument(
        "image",
        help="Path to the image file"
    )
    args = parser.parse_args()

    try:
        classify_image(args.image)
    except (FileNotFoundError, OSError) as error:
        print(f"Input error: {error}")
