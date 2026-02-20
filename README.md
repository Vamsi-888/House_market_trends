**Housing Market Trends – Interactive Dashboard**

Hey there! This is my project where I combined Tableau and Flask to build a clean, interactive dashboard that explores housing market data. I wanted to make it easy for anyone – real estate folks, data enthusiasts, or just curious minds – to dig into what affects house prices. The whole thing is live on my GitHub, so feel free to poke around!

**What’s This All About?**

The idea was simple: take a bunch of housing data (sale prices, renovation years, number of bedrooms, bathrooms, etc.) and turn it into something visual and useful. I used Tableau to create the charts and dashboards, then wrapped them in a Flask web app so everything feels smooth and professional.

**You can explore:**

Overall stats – how many houses, average price, total basement area.

Sales vs. years since renovation – a histogram showing if recently renovated homes sell for more.

House age & renovation – pie chart breaking down age groups and whether they’ve been renovated.

Age vs. features – bar charts that show how house age relates to bathrooms, bedrooms, and floors.

All the visualizations are embedded directly from Tableau Public, so they’re live and interactive.

**What Makes It Cool:**

Full‑screen home page with a nice housing‑themed background – gives it that “wow” factor when you first land.

Smooth “Get Started” button – click it, see a little spinner, then jump to the dashboard. Just a tiny detail, but it feels polished.

Clean navigation – HOME, ABOUT, DASHBOARD, STORY. No clutter.

Responsive – works on desktop and mobile (though Tableau embeds are best on bigger screens).

Easy to customize – swap out the Tableau URLs in app.py and you’re good to go.

**Built With:**

Python + Flask – for the backend and routing.

Tableau Public – all the charts and dashboards were made here, then embedded.

HTML/CSS/JavaScript – frontend with a custom stylesheet.

Font Awesome – for the little house icon on the home page.

Unsplash – background images (feel free to replace them).

**Project Structure (the quick version):**

text
housing_project/
├── app.py                 # Flask app with routes
├── static/
│   └── style.css          # all the custom styling
├── templates/
│   ├── layout.html        # base template with navbar
│   ├── index.html         # home page
│   ├── about.html         # project description
│   ├── dashboard.html     # embeds the Tableau dashboard
│   └── story.html         # embeds the Tableau story
├── .gitignore
└── README.md

**How to Run It Locally:**

Clone the repo

git clone https://github.com/yourusername/housing-market-trends.git

Create a virtual environment (optional but smart)

python -m venv venv then activate it.

Install Flask

pip install flask

Add your own Tableau Public links

Open app.py.

Replace the two placeholder URLs with your dashboard and story links (more on that below).

**Run it**

python app.py

Then open http://127.0.0.1:5000/ in your browser.

Embedding Your Own Tableau Stuff

If you want to use your own Tableau workbooks:

Publish your workbook to Tableau Public.

Go to your published workbook, click Share, and copy the Link (not the embed code).

Change the link to the embed format:

https://public.tableau.com/views/YourWorkbookName/DashboardName?:embed=y&:showVizHome=no&:toolbar=no

Paste that into app.py where you see TABLEAU_DASHBOARD_URL and TABLEAU_STORY_URL.

Easy peasy.

A Sneak Peek
(Add some actual screenshots here – I’d upload a few of the home page, dashboard, and story so people see what it looks like.)

Wanna Contribute?
If you have ideas, find a bug, or just want to chat about the project, feel free to open an issue or send a pull request. I’m always happy to collaborate.

License
This project is under the MIT License – basically, do whatever you want with it, just give credit where it’s due.

**Major Highlights:**

Dataset : https://www.kaggle.com/datasets/rituparnaghosh18/transformed-housing-data-2

Icons by Font Awesome

Background images from Unsplash.

**outputs of dashboard:**

<img width="1911" height="1011" alt="Screenshot 2026-02-20 160203" src="https://github.com/user-attachments/assets/82927fab-d115-4f62-9b2b-bafc84bb886f" />

<img width="1919" height="1012" alt="Screenshot 2026-02-20 160248" src="https://github.com/user-attachments/assets/2ca7b5f8-05bf-45f6-a7c8-c62dcff08fa3" />

<img width="1918" height="1010" alt="Screenshot 2026-02-20 160323" src="https://github.com/user-attachments/assets/080dd4f8-8293-4c68-93d3-fb604fe6240a" />



