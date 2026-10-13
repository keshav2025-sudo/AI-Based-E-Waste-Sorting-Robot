# QA Test Cases – AI-Based E-Waste Sorting Robot

## Objective
To define test cases for evaluating image classification, prediction confidence, processing performance, and sorting-control logic.

## Test Case TC-01: Circuit Board Classification
- **Input:** Image of a printed circuit board.
- **Expected result:** The model identifies the circuit-board category.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## Test Case TC-02: Cable Classification
- **Input:** Image of electrical cables or wires.
- **Expected result:** The model identifies the cable category.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## Test Case TC-03: Battery Classification
- **Input:** Image of a battery.
- **Expected result:** The model identifies the battery category.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## Test Case TC-04: Low-Confidence Prediction
- **Input:** An ambiguous or unfamiliar electronic-waste image.
- **Expected result:** Predictions below the configured confidence threshold are sent for manual review.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## Test Case TC-05: Invalid Image Path
- **Input:** A nonexistent image file.
- **Expected result:** The program reports an input error rather than crashing without an explanation.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## Test Case TC-06: Sorting Position Validation
- **Input:** A valid category passed to the embedded control logic.
- **Expected result:** The corresponding sorting position is selected.
- **Actual result:** To be recorded during simulation or hardware testing.
- **Status:** Not tested.

## Test Case TC-07: Classification Performance
- **Input:** A representative set of test images.
- **Expected result:** Classification processing time is measured and documented.
- **Actual result:** To be recorded during testing.
- **Status:** Not tested.

## QA Notes
AI-generated test scenarios are suggestions. Record actual outputs and measured results before marking a test as passed. The classification model and physical sorting mechanism must be tested separately.
