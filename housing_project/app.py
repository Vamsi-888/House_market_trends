from flask import Flask, render_template

app = Flask(__name__)

# Replace these with your actual Tableau Public URLs
TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/Housing_Market_Trends_dashboard/Dashboard1?:embed=y&:showVizHome=no&:toolbar=no"
TABLEAU_STORY_URL = "https://public.tableau.com/views/Housing_market_Trends1_Story/Story1?:embed=y&:showVizHome=no&:toolbar=no"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', tableau_url=TABLEAU_DASHBOARD_URL)

@app.route('/story')
def story():
    return render_template('story.html', tableau_url=TABLEAU_STORY_URL)

if __name__ == '__main__':
    app.run(debug=True)