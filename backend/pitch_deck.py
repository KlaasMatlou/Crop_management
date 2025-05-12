from fpdf import FPDF
from PIL import Image
import os

class PitchDeckPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Crop Monitoring System Pitch Deck", ln=True, align='C')
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", '', 12)
        self.multi_cell(0, 10, content)
        self.ln(5)

    def add_image_section(self, title, image_path, w=180):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.image(image_path, w=w)
        self.ln(5)

# Set user info
user_name = "Klaas"
user_email = "tshupianematlou@gmail.com"
user_github = "github.com/KlaasMatlou"

# Use relative paths to the parent directory
img1_path = "backend/Screenshot 2025-05-11 205942.png"
img2_path = "backend/Screenshot 2025-05-11 210354.png"


# Create PDF
pdf = PitchDeckPDF()
pdf.add_page()

pdf.add_section("Project Overview", 
    "- A web-based Crop Monitoring System that supports farmers with real-time data on soil conditions, pest detection, and weather forecasts."
)

pdf.add_section("Key Features", 
    "- Real-time Sensor Data Simulation\n"
    "- Weather Forecast Integration using OpenWeatherMap API\n"
    "- Pest Image Upload & Dummy Detection\n"
    "- Crop Health Visualization (Simulated Index Graph)"
)

pdf.add_section("Technology Stack", 
    "- Frontend: HTML, CSS, JavaScript\n"
    "- Backend: Python (Flask)\n"
    "- API: OpenWeatherMap\n"
    "- Database: SQLite (via SQLAlchemy)"
)

pdf.add_section("How it Works", 
    "- User opens the dashboard to view simulated sensor data.\n"
    "- Enters a city name to retrieve the current weather forecast.\n"
    "- Uploads pest images to simulate detection.\n"
    "- All logs are saved in the backend database."
)

pdf.add_section("Developer Info", 
    f"- Name: {user_name}\n- Email: {user_email}\n- GitHub: {user_github}"
)

pdf.add_image_section("Dashboard Overview", img1_path)
pdf.add_image_section("Weather & Pest Detection Example", img2_path)

# Save the PDF to backend folder
output_path = os.path.join(os.getcwd(), "Crop_Monitoring_Pitch_Deck_Klaas.pdf")
pdf.output(output_path)
print("PDF created at:", output_path)
