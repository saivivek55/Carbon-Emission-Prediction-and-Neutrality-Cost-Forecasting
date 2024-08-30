from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Define sample data for costs
costs_data = {
    'China': [1.464974e+11, 1.563664e+11, 1.633603e+11, 1.731546e+11],
    'India': [5.676742e+08, 6.081212e+08, 6.439583e+08, 6.886133e+08],
    'Russia': [1.475506e+10, 1.318263e+10, 1.088951e+10, 8.029967e+09],
    'United States': [1.141095e+09, 1.168953e+09, 1.167791e+09, 1.164584e+09]
}

# Define sample data for emissions
emissions_data = {
    'China': [12067.552856, 12531.528857, 12726.294565, 12887.386095],
    'India': [2723.127324, 2877.580555, 2954.769346, 3014.155150],
    'Russia': [1350.011139, 1293.267057, 1209.748493, 1130.689892],
    'United States': [5239.351029, 5276.914026, 5212.758325, 5132.366530]
}

years = [2023, 2024, 2025, 2026]
costs_df = pd.DataFrame(costs_data, index=years)
emissions_df = pd.DataFrame(emissions_data, index=years)

# Format the costs data with a dollar sign
formatted_costs_df = costs_df.applymap(lambda x: f"${x:,.2f}")

@app.route('/')
def home():
    return render_template('table.html', 
                           costs_table=formatted_costs_df.to_html(classes='table table-striped', escape=False),
                           emissions_table=emissions_df.to_html(classes='table table-striped', escape=False))

if __name__ == '__main__':
    app.run(debug=True)
