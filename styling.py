import streamlit as st

def apply_base_styles(dark_mode: bool = True):
    """
    Applies custom CSS to the Streamlit application for a professional look,
    with a toggle for dark/light mode.
    """
    # Define color variables for dark and light themes
    if dark_mode:
        # Dark theme colors (current defaults)
        bg_primary = "#0E1117" # Streamlit's default dark theme background
        bg_secondary = "#1a202c" # Card/input background, header
        text_light = "#FAFAFA"
        text_medium = "#a0aec0"
        accent_blue_light = "#63b3ed"
        accent_blue_dark = "#4299e1"
        success_color = "#4CAF50"
        danger_color = "#EF4444"
        warning_color = "#FBBF24"
        info_color = "#3B82F6"
        border_color = "#4a5568"
        code_bg = "#1a202c" # For code blocks
        code_text = "#FFD700" # Gold for code
    else:
        # Light theme colors
        bg_primary = "#FFFFFF" # White background
        bg_secondary = "#F0F2F6" # Light gray for cards/inputs
        text_light = "#333333"
        text_medium = "#666666"
        accent_blue_light = "#007BFF" # Brighter blue
        accent_blue_dark = "#0056b3" # Darker blue
        success_color = "#28A745"
        danger_color = "#DC3545"
        warning_color = "#FFC107"
        info_color = "#17A2B8"
        border_color = "#CCCCCC"
        code_bg = "#E8E8E8" # Light grey for code blocks
        code_text = "#333333" # Dark text for code


    # Inject CSS with dynamic variables
    st.markdown(f"""
    <style>
        /* Import Inter font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        /* Import Font Awesome for Icons */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');


        /* Color Variables based on selected theme */
        :root {{
            --bg-primary: {bg_primary};
            --bg-secondary: {bg_secondary};
            --text-light: {text_light};
            --text-medium: {text_medium};

            --accent-blue-light: {accent_blue_light};
            --accent-blue-dark: {accent_blue_dark};

            --success-color: {success_color};
            --danger-color: {danger_color};
            --warning-color: {warning_color};
            --info-color: {info_color};

            --border-color: {border_color};
            --code-bg: {code_bg};
            --code-text: {code_text};

            --shadow-light: rgba(0, 0, 0, 0.2);
            --shadow-medium: rgba(0, 0, 0, 0.4);
            --border-radius-lg: 12px;
            --border-radius-md: 8px;
            --border-radius-sm: 4px;
        }}

        /* General Body & Typography */
        html, body {{
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: var(--text-light);
            background-color: var(--bg-primary);
            scroll-behavior: smooth; /* Smooth scrolling for anchor links */
        }}

        /* Streamlit App Overrides */
        .stApp {{
            background-color: var(--bg-primary);
            color: var(--text-light);
        }}
        .stApp > header {{
            background-color: var(--bg-secondary);
            padding: 1.5rem 2rem;
            box-shadow: 0 4px 8px var(--shadow-medium);
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid var(--border-color);
            transition: all 0.3s ease; /* Smooth transition for header background/shadow */
        }}
        
        /* Hero Section Styling */
        .hero-section {{
            background: linear-gradient(135deg, var(--bg-secondary) 0%, #1a273b 100%); /* Adjust for light mode */
            padding: 4rem 2rem;
            text-align: center;
            color: var(--text-light);
            box-shadow: 0 10px 30px var(--shadow-medium);
            border-bottom: 2px solid var(--accent-blue-dark);
            position: relative;
            overflow: hidden;
        }}
        /* Remove pseudo-element for simplicity in this general styling file, or define light/dark specific ones */
        /* .hero-section::before {{ ... }} */

        .hero-title {{
            font-size: 3.8rem;
            color: var(--accent-blue-light);
            margin-bottom: 0.8rem;
            font-weight: 800;
            letter-spacing: -0.06em;
            text-shadow: 0px 4px 10px var(--shadow-medium);
            position: relative;
            z-index: 1;
        }}
        .hero-title i {{
            margin-right: 1rem;
            color: var(--accent-blue-dark);
        }}

        .hero-subtitle {{
            font-size: 1.8rem;
            color: var(--text-medium);
            margin-bottom: 1.5rem;
            font-weight: 400;
            opacity: 0.95;
            line-height: 1.4;
            position: relative;
            z-index: 1;
        }}

        .hero-tagline {{
            font-size: 1.4rem;
            color: var(--accent-blue-light);
            font-weight: 600;
            margin-top: 2rem;
            text-shadow: 0px 1px 3px rgba(0,0,0,0.2);
            position: relative;
            z-index: 1;
        }}

        /* Main Content Container */
        .main .block-container {{
            max-width: 1200px;
            padding: 2.5rem 3rem;
            background-color: var(--bg-secondary);
            border-radius: var(--border-radius-lg);
            box-shadow: 0 10px 25px var(--shadow-medium);
            margin: 3rem auto;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease; /* Smooth transition for main content area */
        }}

        /* Section Headers */
        .stMarkdown h2 {{
            font-size: 2.2rem;
            color: var(--text-light);
            margin-top: 2.5rem;
            margin-bottom: 1.8rem;
            border-bottom: 2px solid var(--accent-blue-light);
            padding-bottom: 0.8rem;
            font-weight: 700;
            position: relative;
            transition: color 0.3s ease; /* Smooth transition for header color */
        }}
        .stMarkdown h2::after {{
            content: '';
            display: block;
            width: 70px;
            height: 5px;
            background: linear-gradient(90deg, var(--accent-blue-light), transparent);
            position: absolute;
            bottom: -2px;
            left: 0;
            border-radius: var(--border-radius-sm);
        }}

        .stMarkdown h3 {{
            font-size: 1.8rem;
            color: var(--accent-blue-light);
            margin-top: 2rem;
            margin-bottom: 1.2rem;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 0.6rem;
            font-weight: 600;
            transition: color 0.3s ease;
        }}
        .stMarkdown h4 {{
            font-size: 1.4rem;
            color: var(--accent-blue-dark);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 600;
            transition: color 0.3s ease;
        }}

        /* Textareas and Input Fields */
        textarea, .stTextInput > div > div > input, .stCodeEditor {{
            background-color: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            color: var(--text-light);
            font-size: 1.05rem;
            padding: 12px 18px;
            box-shadow: inset 0 2px 5px var(--shadow-light);
            transition: all 0.3s ease;
        }}
        textarea:focus, .stTextInput > div > div > input:focus, .stCodeEditor:focus-within {{
            border-color: var(--accent-blue-light);
            box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5), inset 0 2px 5px var(--shadow-light);
            outline: none;
        }}
        textarea::placeholder {{
            color: var(--text-medium);
            opacity: 0.6;
        }}

        /* Buttons */
        .stButton > button {{
            padding: 1rem 2rem;
            border: none;
            border-radius: var(--border-radius-md);
            font-size: 1.1rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 1.8rem;
            box-shadow: 0 8px 15px var(--shadow-medium);
            letter-spacing: 0.03em;
        }}
        .stButton > button:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 20px var(--shadow-medium);
        }}
        .stButton > button:active {{
            transform: translateY(0);
            box-shadow: 0 4px 8px var(--shadow-light);
        }}

        .stButton > button.primary {{
            background: linear-gradient(45deg, var(--accent-blue-dark), var(--accent-blue-light));
            color: #ffffff;
            border: 1px solid var(--accent-blue-light);
        }}
        .stButton > button.primary:hover {{
            background: linear-gradient(45deg, #3182ce, var(--accent-blue-light));
        }}

        .stButton > button.secondary {{
            background-color: var(--bg-primary);
            color: var(--accent-blue-light);
            border: 2px solid var(--accent-blue-dark);
        }}
        .stButton > button.secondary:hover {{
            background-color: var(--accent-blue-dark);
            color: #ffffff;
            border-color: var(--accent-blue-dark);
        }}
        .stButton > button i {{
            margin-right: 0.7rem;
            font-size: 1.2em;
        }}

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {{
            border-bottom: 2px solid var(--border-color);
            margin-bottom: 1.8rem;
        }}
        .stTabs [data-baseweb="tab-list"] button {{
            background-color: transparent;
            color: var(--text-medium);
            border: none;
            padding: 1.2rem 1.8rem;
            font-size: 1.15rem;
            font-weight: 600;
            transition: all 0.3s ease;
            border-bottom: 3px solid transparent;
            position: relative;
            overflow: hidden;
        }}
        .stTabs [data-baseweb="tab-list"] button:hover:not([aria-selected="true"]) {{
            color: var(--text-light);
            background-color: var(--border-color);
            border-radius: var(--border-radius-md) var(--border-radius-md) 0 0;
            transform: translateY(-3px);
        }}
        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
            color: var(--accent-blue-light) !important;
            border-bottom: 4px solid var(--accent-blue-light) !important;
            background-color: var(--bg-primary) !important;
            transform: translateY(-2px);
        }}
        .stTabs [data-baseweb="tab-list"] button i {{
            margin-right: 0.8rem;
            font-size: 1.2em;
            color: inherit;
        }}

        /* Markdown output styling (for AI explanations) */
        .stMarkdown p, .stMarkdown ul, .stMarkdown ol, .stMarkdown li {{
            color: var(--text-light);
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }}
        .stMarkdown ul {{
            list-style-type: '👉 ';
            margin-left: 30px;
            padding-left: 10px;
        }}
        .stMarkdown ol {{
            margin-left: 30px;
            padding-left: 10px;
        }}
        .stMarkdown strong {{
            color: var(--accent-blue-light);
            font-weight: 700;
        }}
        .stMarkdown em {{
            color: var(--text-medium);
            font-style: italic;
        }}
        .stMarkdown code {{
            background-color: var(--border-color); /* Use border color as code background for consistency */
            padding: 0.3em 0.5em;
            border-radius: var(--border-radius-sm);
            font-family: 'Fira Code', 'Cascadia Code', monospace;
            font-size: 0.95em;
            color: var(--code-text); /* Use dynamic code text color */
        }}
        .stMarkdown pre code {{ /* Code blocks */
            background-color: var(--code-bg); /* Use dynamic code block background */
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            padding: 1.5em;
            overflow-x: auto;
            margin-bottom: 2rem;
            display: block;
            box-shadow: inset 0 0 10px var(--shadow-light);
            color: var(--text-light); /* Main text color for pre blocks */
            font-size: 1em;
            line-height: 1.5;
        }}

        /* Alerts and Info Boxes */
        .stAlert {{
            border-radius: var(--border-radius-md);
            margin-top: 1.5rem;
            padding: 1.2rem 1.8rem;
            font-weight: 600;
            font-size: 1.05rem;
        }}
        /* Specific alert types now use the dynamic color variables */
        .stAlert.st-emotion-cache-1fcpknu {{ /* Success */
            border-left: 8px solid var(--success-color) !important;
            background-color: rgba(var(--success-color-rgb), 0.15) !important;
            color: var(--success-color) !important;
        }}
        .stAlert.st-emotion-cache-1wdd6qg {{ /* Warning */
            border-left: 8px solid var(--warning-color) !important;
            background-color: rgba(var(--warning-color-rgb), 0.15) !important;
            color: var(--warning-color) !important;
        }}
        .stAlert.st-emotion-cache-1215i5j {{ /* Error */
            border-left: 8px solid var(--danger-color) !important;
            background-color: rgba(var(--danger-color-rgb), 0.15) !important;
            color: var(--danger-color) !important;
        }}
        .stInfo {{ /* Info */
            border-left: 8px solid var(--info-color);
            background-color: rgba(var(--info-color-rgb), 0.15);
            border-radius: var(--border-radius-md);
            padding: 1.5rem;
            margin-top: 1.5rem;
            color: var(--info-color);
            font-size: 1.1rem;
        }}
        /* Helper to get RGB values for rgba backgrounds */
        .stApp {{
            --success-color-rgb: {int(success_color[1:3], 16)}, {int(success_color[3:5], 16)}, {int(success_color[5:7], 16)};
            --warning-color-rgb: {int(warning_color[1:3], 16)}, {int(warning_color[3:5], 16)}, {int(warning_color[5:7], 16)};
            --danger-color-rgb: {int(danger_color[1:3], 16)}, {int(danger_color[3:5], 16)}, {int(danger_color[5:7], 16)};
            --info-color-rgb: {int(info_color[1:3], 16)}, {int(info_color[3:5], 16)}, {int(info_color[5:7], 16)};
        }}


        /* Expander Styling */
        .streamlit-expanderHeader {{
            background-color: var(--border-color);
            color: var(--text-light);
            font-weight: 600;
            border-radius: var(--border-radius-md);
            padding: 1rem 1.5rem;
            margin-bottom: 1rem;
            transition: background-color 0.3s ease;
            box-shadow: 0 3px 8px var(--shadow-light);
            font-size: 1.1rem;
        }}
        .streamlit-expanderHeader:hover {{
            background-color: #5b6980; /* Specific hover for expander header */
        }}
        .streamlit-expanderContent {{
            background-color: var(--bg-primary);
            border: 1px solid var(--border-color);
            border-top: none;
            border-radius: 0 0 var(--border-radius-md) var(--border-radius-md);
            padding: 1.8rem;
            box-shadow: inset 0 0 10px var(--shadow-light);
        }}

        /* Horizontal rule */
        hr {{
            border-top: 1px solid var(--border-color);
            margin: 3.5rem 0;
            opacity: 0.6;
        }}

        /* --- Custom Metric Card and Grid Styling --- */
        /* Target the Streamlit columns div and make it a grid container */
        div[data-testid="stColumns"]:has(.custom-metric-card) {{
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
            gap: 1.5rem !important;
            margin-top: 1.5rem !important;
            margin-bottom: 2rem !important;
            padding: 1rem !important;
            background-color: var(--bg-primary) !important;
            border-radius: var(--border-radius-lg) !important;
            box-shadow: inset 0 0 15px var(--shadow-light) !important;
            align-items: stretch !important;
        }}
        div[data-testid="stColumns"]:has(.custom-metric-card) > div {{
            padding: 0 !important;
            margin: 0 !important;
            min-width: unset !important;
        }}


        .custom-metric-card {{
            background-color: var(--bg-secondary);
            border-radius: var(--border-radius-md);
            padding: 1.5rem;
            box-shadow: 0 6px 15px var(--shadow-medium);
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            min-height: 140px;
            border: 1px solid var(--border-color);
            height: 100%;
        }}
        .custom-metric-card:hover {{
            transform: translateY(-7px);
            box-shadow: 0 10px 25px var(--shadow-medium);
        }}

        .custom-metric-content {{
            flex-grow: 1;
        }}

        .custom-metric-value {{
            font-size: 3.2em;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 0.3rem;
            color: var(--accent-blue-light);
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }}

        .custom-metric-label {{
            font-size: 1.1em;
            color: var(--text-medium);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.5rem;
        }}
        .custom-metric-label i {{
            margin-right: 0.8rem;
            color: var(--accent-blue-dark);
        }}

        .custom-metric-delta {{
            font-size: 1.3em;
            font-weight: 700;
            margin-top: 1rem;
            align-self: flex-end;
            padding: 0.3em 0.7em;
            border-radius: var(--border-radius-sm);
            background-color: rgba(255,255,255,0.08);
        }}

        /* Specific card types and their colors */
        .custom-metric-card-info {{
            background: linear-gradient(135deg, {bg_secondary}, {bg_primary});
            border-left: 6px solid var(--info-color);
            color: var(--text-light);
        }}
        .custom-metric-card-info .custom-metric-value {{
            color: var(--info-color);
        }}

        .custom-metric-card-added {{
            background: linear-gradient(135deg, {bg_secondary}, {bg_primary});
            border-left: 6px solid var(--success-color);
            color: var(--text-light);
        }}
        .custom-metric-card-added .custom-metric-value {{
            color: var(--success_color);
        }}
        
        .custom-metric-card-deleted {{
            background: linear-gradient(135deg, {bg_secondary}, {bg_primary});
            border-left: 6px solid var(--danger_color);
            color: var(--text-light);
        }}
        .custom-metric-card-deleted .custom-metric-value {{
            color: var(--danger_color);
        }}

        .custom-metric-card-modified {{
            background: linear-gradient(135deg, {bg_secondary}, {bg_primary});
            border-left: 6px solid var(--warning_color);
            color: var(--text-light);
        }}
        .custom-metric-card-modified .custom-metric-value {{
            color: var(--warning_color);
        }}

        /* Delta colors */
        .custom-metric-delta.delta-positive {{
            color: var(--success_color);
        }}
        .custom-metric-delta.delta-negative {{
            color: var(--danger_color);
        }}
        .custom-metric-delta.delta-neutral {{
            color: var(--text-medium);
        }}


        /* Responsive Design */
        @media (max-width: 1024px) {{
            div[data-testid="stColumns"]:has(.custom-metric-card) {{
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
                gap: 1rem !important;
            }}
            .custom-metric-card {{
                min-height: 120px;
                padding: 1.2rem;
            }}
            .custom-metric-value {{
                font-size: 2.8em;
            }}
            .custom-metric-label {{
                font-size: 1em;
            }}
        }}

        @media (max-width: 768px) {{
            .main .block-container {{
                padding: 1.5rem;
                margin: 1.5rem auto;
                width: 95%;
            }}
            .stButton > button {{
                display: block;
                width: 100%;
                margin: 0.8rem 0;
            }}
            .stMarkdown h1 {{
                font-size: 2rem;
            }}
            .stMarkdown h2 {{
                font-size: 1.7rem;
            }}
            .stMarkdown h3 {{
                font-size: 1.4rem;
            }}
            .stMarkdown h4 {{
                font-size: 1.1rem;
            }}
            .stTabs [data-baseweb="tab-list"] button {{
                padding: 0.8rem 1rem;
                font-size: 1rem;
            }}
            .stMarkdown ul {{
                margin-left: 15px;
            }}
            div[data-testid="stColumns"]:has(.custom-metric-card) {{
                grid-template-columns: 1fr !important;
                gap: 0.8rem !important;
                padding: 0.8rem !important;
            }}
            .custom-metric-card {{
                min-height: 100px;
                padding: 1rem;
            }}
            .custom-metric-value {{
                font-size: 2.5em;
            }}
            .custom-metric-label {{
                font-size: 0.9em;
            }}
        }}

        /* --- Interactive Diff Viewer Styling --- */
        .diff-viewer-container {{
            background-color: var(--bg-primary); /* Dark background for the diff area */
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            padding: 1rem;
            margin-top: 1.5rem;
            overflow-x: auto; /* Allow horizontal scrolling for wide tables */
        }}

        .diff-table {{
            width: 100%;
            border-collapse: collapse; /* Ensure cells share borders */
            margin-bottom: 1rem;
            font-family: 'Fira Code', 'Cascadia Code', monospace; /* Monospace for diff content */
            font-size: 0.95em;
        }}

        .diff-table th, .diff-table td {{
            padding: 0.6rem 1rem;
            border: 1px solid var(--border-color); /* Cell borders */
            vertical-align: top; /* Align content to the top */
        }}

        .diff-table th {{
            background-color: var(--bg-secondary);
            color: var(--text-light);
            text-align: left;
            font-weight: 600;
        }}

        .diff-table tbody tr:nth-child(even) {{
            background-color: rgba(var(--bg-secondary-rgb), 0.5); /* Use a slight tint of secondary bg */
        }}
        .diff-table tbody tr:nth-child(odd) {{
            background-color: var(--bg-primary); /* Darker row background */
        }}
        /* Helper to get RGB for rgba backgrounds dynamically */
        .stApp {{
            --bg-secondary-rgb: {int(bg_secondary[1:3], 16)}, {int(bg_secondary[3:5], 16)}, {int(bg_secondary[5:7], 16)};
        }}


        /* Diff Cell Coloring */
        .diff-cell {{
            color: var(--text-light); /* Default text color */
        }}

        /* Added elements (Green) */
        .diff-added {{
            background-color: rgba(var(--success-color-rgb), 0.2);
            color: var(--success-color);
            font-weight: 500;
        }}
        .diff-added-label {{
            color: var(--success-color);
            font-weight: 600;
        }}

        /* Deleted elements (Red) */
        .diff-deleted {{
            background-color: rgba(var(--danger-color-rgb), 0.2);
            color: var(--danger-color);
            text-decoration: line-through;
            font-weight: 500;
        }}
        .diff-deleted-label {{
            color: var(--danger-color);
            font-weight: 600;
        }}

        /* Modified elements (Yellow/Orange) */
        .diff-modified {{
            background-color: rgba(var(--warning-color-rgb), 0.15);
            color: var(--warning-color);
            font-weight: 500;
        }}
        .diff-modified-label {{
            color: var(--warning-color);
            font-weight: 600;
        }}

        /* Renamed elements (Purple/Blue-Violet) - Using a distinct color */
        .diff-renamed {{
            background-color: rgba(138, 43, 226, 0.15);
            color: #8A2BE2;
            font-weight: 500;
        }}
        .diff-renamed-label {{
            color: #8A2BE2;
            font-weight: 600;
        }}

        .diff-viewer-container h4 {{
            color: var(--accent-blue-light);
            margin-top: 1rem;
            margin-bottom: 0.8rem;
        }}
        .diff-viewer-container h5 {{
            color: var(--text-light);
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            border-bottom: 1px dashed var(--border-color);
            padding-bottom: 0.3rem;
        }}

        /* Streamlit Toggle Specific Styling */
        .stToggle label span {{
            font-size: 1.1em;
            font-weight: 600;
            color: var(--text-light);
        }}
        .stToggle [data-testid="stCheckbox"] {{
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            padding: 0.8rem 1.2rem;
            box-shadow: 0 2px 5px var(--shadow-light);
        }}
        /* Customize the toggle switch itself */
        [data-testid="stCheckbox"] > label > div > div {{
            background-color: var(--border-color) !important;
            border-color: var(--text-medium) !important;
        }}
        [data-testid="stCheckbox"] > label > div > div[aria-checked="true"] {{
            background-color: var(--accent-blue-light) !important;
            border-color: var(--accent-blue-light) !important;
        }}

        /* New Footer Styling - Sticky */
        footer {{
            position: sticky;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: var(--bg-secondary); /* Match header/card background */
            padding: 1rem 2rem;
            text-align: center;
            color: var(--text-medium);
            font-size: 0.9em;
            border-top: 1px solid var(--border-color);
            box-shadow: 0 -4px 8px var(--shadow-medium);
            z-index: 1000;
            transition: all 0.3s ease;
        }}
        /* Ensure Streamlit's default footer doesn't interfere */
        #MainMenu, footer {{ visibility: visible; }}
        footer:has([data-testid="stDecoration"]) {{ visibility: hidden; }} /* Hide Streamlit's default footer */
        
        /* New style for transformation list items */
        .transformation-item {{
            display: inline-block; /* Make them behave like tags */
            background-color: var(--accent-blue-dark); /* Blue background */
            color: #ffffff; /* White text */
            padding: 0.4em 0.8em;
            margin: 0.3em;
            border-radius: var(--border-radius-md); /* Rounded corners */
            font-size: 0.95em;
            font-weight: 600;
            border: 1px solid var(--accent-blue-light);
            transition: all 0.2s ease-in-out;
            cursor: default; /* Not clickable, so default cursor */
            box-shadow: 0 2px 5px var(--shadow-light);
        }}
        .transformation-item:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 10px var(--shadow-medium);
            background-color: var(--accent-blue-light);
        }}
        .transformation-item i {{
            margin-right: 0.5em; /* Space for icon */
            color: #ffffff;
        }}
        /* Container for the tags */
        .transformation-list-container {{
            display: flex;
            flex-wrap: wrap; /* Allow items to wrap to next line */
            gap: 0.5em; /* Space between tags */
            margin-top: 1em;
            padding: 0.5em;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-md);
            background-color: var(--bg-primary);
            box-shadow: inset 0 0 8px var(--shadow-light);
        }}

    </style>
    """, unsafe_allow_html=True)