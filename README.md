# Screen Time vs Battery Usage — Linear Regression

My  Machine Learning project: using **Simple Linear Regression** to explore the relationship between screen time and battery usage.

## Project goal

This project trains a Linear Regression model to predict battery usage from screen time. It uses a small, manually entered **sample dataset** for learning and practice.

> **Important limitation:** These values are illustrative sample data, not measurements collected from a real phone. The model demonstrates the workflow; it should not be treated as a reliable real-world battery estimator.

## Tools used

- Python
- pandas is not required for this version
- Scikit-learn — train the regression model and calculate Mean Squared Error (MSE)
- Matplotlib — visualize the sample data and regression line

## Dataset

| Screen time (minutes) | Battery used (%) |
|---:|---:|
| 15 | 3 |
| 30 | 6 |
| 45 | 9 |
| 60 | 13 |
| 75 | 16 |
| 90 | 20 |
| 105 | 23 |
| 120 | 27 |
| 135 | 30 |
| 150 | 34 |

## What the code does

1. Stores screen time as the input feature (`X`) and battery usage as the target (`y`).
2. Splits the data into training (80%) and testing (20%) subsets.
3. Trains a `LinearRegression` model on the training subset.
4. Predicts battery usage for the test subset.
5. Prints actual values, predictions, and Mean Squared Error.
6. Plots the sample observations and the fitted regression line.

## How to run

### 1. Install Python

Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed.

### 2. Download or clone this repository

If Git is installed, run:

```bash
git clone YOUR_REPOSITORY_URL
cd screen-time-battery-regression
```

Or download the repository ZIP from GitHub and extract it.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If your system uses the `py` launcher on Windows, you can use:

```bash
py -m pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

On Windows, this may also work:

```bash
py main.py
```

The program prints the test predictions and MSE, then opens a graph.

## Key concepts I practiced

- Supervised learning
- Simple Linear Regression
- Training and testing data
- Model predictions
- Mean Squared Error (MSE)
- Data visualization

## What I learned

This project helped me practice the basic Machine Learning workflow: preparing data, splitting it into training and testing sets, fitting a model, evaluating predictions, and plotting the result.

## Possible next improvements

- Collect real battery usage data from a phone.
- Compare predictions with a baseline model.
- Try other regression metrics, such as Mean Absolute Error (MAE).
- Test how well the model performs on more data.

## Project status

Beginner learning project — built for practice and continued improvement.
