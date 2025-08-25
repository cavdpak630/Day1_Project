# Day1_Project

A simple cross-platform Python project to practice virtual environments, Git/GitHub, and Linux workflows.  
The script generates random numbers, computes statistics, and saves them into a CSV file.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/<your-username>/Day1_Project.git
cd Day1_Project
```

## Set up Virtual Environment & Install Dependencies
### On Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### On Windows (PowerShell):
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```
python analyze.py     (On windows)
./run.sh              (On Linux)
```

## Example Output
Mean: 0.4823
Max: 0.9741
Min: 0.0317

A CSV file (data.csv) will be generated in the project directory.
