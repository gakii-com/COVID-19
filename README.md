📊 COVID-19 Global Data Tracker

A Python-based data analysis project that tracks COVID-19 cases, deaths, and vaccinations across different countries.
The project cleans and analyzes real-world data, generates visualizations, and produces insights that can be presented in reports.

🚀 Project Objectives

✅ Import and clean COVID-19 global data

✅ Analyze time trends (cases, deaths, vaccinations)

✅ Compare metrics across countries/regions

✅ Visualize trends with charts and maps

✅ Communicate findings with insights and narratives

🛠️ Tools & Libraries

Python 3.x

Jupyter Notebook or VS Code (with Python & Jupyter extension)

pandas – Data loading & cleaning

matplotlib & seaborn – Static plots (line, bar, heatmaps)

plotly – Interactive visualizations (choropleth, line charts)

📂 Project Structure
📁 covid19-tracker
│── covid_tracker.py     # Main Python script
│── owid-covid-data.csv  # Dataset (download from Our World in Data)
│── README.md            # Project documentation

📊 Dataset

We use the Our World in Data COVID-19 dataset:

👉 Download here: owid-covid-data.csv

Save it in the same folder as the script.

⚡ Setup & Installation

Clone this repository or copy the project files.

Download owid-covid-data.csv and place it in the project folder.

Install dependencies:

pip install pandas matplotlib seaborn plotly


Run the script in VS Code terminal:

python covid_tracker.py

📈 Features & Visualizations

Line charts: Total cases & deaths over time

Bar charts: Top countries by cases/deaths

Heatmaps: Correlation between variables

Interactive Choropleth Maps (Plotly):

Cases by country

Vaccination rates

📌 Sample Insights

India experienced the highest surge in daily new cases during 2021.

United States had one of the fastest vaccine rollouts but high total deaths.

Kenya showed relatively lower case numbers but slower vaccination uptake.

Death rates varied widely across countries, partly due to differences in reporting.

Vaccination rollout correlates with reduced new cases after mid-2021.

🎯 Deliverables

📒 Well-documented Python script (covid_tracker.py)

📊 Visualizations (matplotlib, seaborn, plotly)

📝 Insights & narrative explanations (console + markdown)

📄 Optional: Export notebook to PDF or create slides with screenshots
