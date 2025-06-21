# Shirt Categorizer Using K-Nearest Neighbors (KNN)

This project implements a simple K-Nearest Neighbors (KNN) classifier in Python to categorize shirts based on their size and quality.

## Overview

The program reads shirt data from a CSV file (`shirt_data.csv`) containing shirt attributes:

- **Size** (integer)
- **Quality** (integer)
- **Category** (string label)

Given a new shirt's size and quality, the program calculates the Euclidean distance between this new shirt and each shirt in the dataset. It then selects the top *k* (default 5) nearest neighbors and predicts the category based on majority voting among those neighbors.

## How It Works

1. Load data from the CSV file.
2. Take user input for a new shirt's size and quality.
3. Calculate distances between the new shirt and all dataset entries.
4. Sort the distances to find the closest neighbors.
5. Use majority voting of the nearest neighbors’ categories to predict the category of the new shirt.
6. Output the predicted category.

## Usage

1. Ensure you have `shirt_data.csv` in the same folder as the script.
2. Run the Python script:
3. Result


![Screenshot 2025-06-21 232548](https://github.com/user-attachments/assets/c78cf5b2-52c1-4941-9b9d-f73c2a76ba09)

```bash
python shirt_categorizer.py
