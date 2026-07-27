# Co-founder Match Recommender

Co-founder Match Recommender is an intelligent decision-support platform designed to solve the critical challenge of founding team assembly. Finding the right co-founder is one of the most significant determinants of early-stage startup success. This application automates candidate sourcing by analyzing biographical summaries, operational backgrounds, availability bounds, and technical skills to match complementary profiles.

The backend uses semantic text analysis combined with numeric scoring formulas. Individual biography summaries are mapped into high-dimensional vector spaces using a sentence-transformer embedding model to compute cosine similarity. These similarity values are then blended with categorical overlap metrics (matching roles, skills, availability, and experience levels) to generate a final weighted compatibility score.

The user interface is built as a dark dashboard inspired by Linear and Vercel. It supports dynamic profile selection, real-time query executions, detailed card partitions, outlined chips, and initials-based avatars.

---

## Features
* **AI-Powered Recommendation Engine**: Generates top matching profiles ranked by calculated compatibility metrics.
* **Semantic Biography Matching**: Computes cosine similarity scores on founder bios using natural language processing (NLP).
* **Category Overlap Scoring**: Integrates matching indicators across skills, interests, roles, availability, and experience levels.
* **Dynamic Custom Dropdown Selector**: A custom-designed React dropdown menu that expands downward reliably and avoids overlapping headers.
* **Polished SaaS UI/UX**: Includes soft ambient radial canvas glows, card top bevel details, hovered micro-lifts, and 2-line clamped biographies.
* **Comprehensive Error States**: Intercepts backend offline scenarios and handles state feedback gracefully with error banners.
* **Environment Configuration Fallback**: Fully customizable backend URL reading using Vite environment variables.

---

## Tech Stack

| Layer | Technology | Key Function / Purpose |
|---|---|---|
| **API Backend** | FastAPI (Python) | High-performance asynchronous endpoint server. |
| **Machine Learning** | Sentence-Transformers | Computes high-quality biographical semantic text embeddings. |
| **Vector Math** | NumPy | Calculates cosine similarity values and array dot products. |
| **UI Library** | React (JavaScript) | Component-driven frontend architecture. |
| **Build System** | Vite | Ultra-fast local hot module replacement (HMR) bundler. |
| **HTTP Client** | Axios | Frontend network request wrapper for API queries. |
| **Styling** | Vanilla CSS | Fully custom design system with custom properties. |

---

## Project Structure

```text
cofounder-match-recommender/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   │   ├── embeddings.py       # Model initialization and lazy loading
│   │   │   └── matching.py         # Cosine math and profile scoring logic
│   │   └── main.py                 # FastAPI application routes and startup context
│   └── tests/                      # Pytest API validation files
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── MatchCard.jsx       # Custom avatars, compatibility scores, and chip tags
│   │   │   └── ProfileSelector.jsx # Custom React dropdown select wrapper
│   │   ├── services/
│   │   │   └── api.js              # Environment variable fetching and Axios calls
│   │   ├── App.jsx                 # Dynamic page shell and query dispatchers
│   │   └── App.css                 # Dark blue ambient canvas styling rules
│   └── .env.example                # Vite environment configuration template
├── README.md                       # Main documentation
├── TEST_CASES.md                   # QA Manual verification scripts
└── ETHICS.md                       # Responsible AI guidelines and audits
```

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd cofounder-match-recommender
```

### 2. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Initialize and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Frontend Setup
1. Open a new terminal and navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install npm packages:
   ```bash
   npm install
   ```

---

## Environment Variables
The React frontend reads the backend URL dynamically following Vite standards.

* **Variable Name**: `VITE_API_BASE_URL`
* **Default Fallback**: `http://localhost:8000` (automatically applied if no env file is present).

A template is located at `frontend/.env.example`:
```ini
VITE_API_BASE_URL=http://localhost:8000
```
*Note: Do not check in your production `.env` files to source control.*

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| **GET** | `/` | Root index. Returns a greeting confirmation. |
| **GET** | `/api/profiles` | Fetches the full list of 40 founder profile objects (id and name) to populate selectors. |
| **GET** | `/api/matches/{user_id}` | Retrieves the top 5 compatible profiles for the target user, ordered by matching score. |

---

## How the Recommendation Engine Works
The system evaluates profile matching across multiple categories:
1. **Semantic Text Embeddings**: Uses the `all-MiniLM-L6-v2` transformer model to convert biographies into 384-dimensional vector representations, measuring background similarity via cosine similarity.
2. **Category Overlap**: Compares categorical overlaps across Skills, Interests, and Roles.
3. **Continuous Scoring Weight**: Combines the semantic rating and categorical overlap ratings into a unified weighted score. Results are returned sorted from most compatible to least compatible.

---

## Running the Project

### Start the Backend
From the `backend` directory with the virtual environment active:
```bash
uvicorn app.main:app --reload
```
*The API server will listen on `http://127.0.0.1:8000`.*

### Start the Frontend
From the `frontend` directory:
```bash
npm run dev
```
*The Vite development server will listen on `http://localhost:5173`.*

---

## Testing
Manual QA test cases are documented in [TEST_CASES.md](TEST_CASES.md). It covers 25 comprehensive scenarios, including:
* API schema validity
* Frontend loading, empty, and network error states
* Responsive breakpoint layout grids (Desktop, Tablet, Mobile)
* UI hover transitions and click feedbacks

---

## Responsible AI
Ethical boundaries, safety policies, and system limits are detailed in [ETHICS.md](ETHICS.md), including:
* **Transparency**: Open explanations of weighted matching factors.
* **Fairness**: Neutral scoring math applied identically across profiles.
* **Bias Awareness**: Notes on biases inherited from pre-trained language models.
* **Human Oversight**: Encouragement of manual profile reviews prior to partnership contracts.

---

## Future Improvements
* **Explainable AI Recommendations**: Provide clear UI cues explaining match reasoning (e.g. *Matched due to AI focus*).
* **Statistical Fairness Audits**: Regular demographic testing of recommendations.
* **User Feedback Loops**: Allow founders to tag match relevance to refine weighted formulas.
* **Secure Database Integration**: Move from local JSON profiles to PostgreSQL/MongoDB.
* **Production Auth**: Implement JWT/OAuth authentication systems.

---

## Screenshots

### Dashboard
*(Add dashboard screenshot here)*

### Recommendation Results
*(Add recommendation results screenshot here)*

---

## License
Educational / AI Engineering Assessment Internship Project.
