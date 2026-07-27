import { useState, useEffect } from "react";
import ProfileSelector from "./components/ProfileSelector";
import MatchList from "./components/MatchList";
import LoadingSpinner from "./components/LoadingSpinner";
import ErrorMessage from "./components/ErrorMessage";
import { getProfiles, getMatches } from "./services/api";
import "./App.css";

function App() {
    const [profiles, setProfiles] = useState([]);
    const [selectedProfile, setSelectedProfile] = useState("");
    const [matches, setMatches] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    // Load actual profiles dynamically from the backend on mount
    useEffect(() => {
        async function fetchProfiles() {
            try {
                const data = await getProfiles();
                setProfiles(data);
            } catch (err) {
                console.error("Error loading profiles:", err);
                setError("Unable to load founder profiles from the backend server. Please verify the backend is running.");
            }
        }
        fetchProfiles();
    }, []);

    function onProfileChangeAndReset(profileId) {
        setSelectedProfile(profileId);
        setMatches([]);
        setError("");
    }

    async function handleFindMatches() {
        if (!selectedProfile) return;
        try {
            setLoading(true);
            setError("");
            setMatches([]); // Clear previous matches during load

            const data = await getMatches(selectedProfile);
            setMatches(data);
        } catch (err) {
            console.error("Error fetching matches:", err);
            setError("Unable to fetch recommendations. Please check the backend connection.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="app">
            <header className="hero-section">
                <div className="hero-icon-container">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="36" height="36" className="hero-icon">
                        <circle cx="12" cy="5" r="3.5" />
                        <circle cx="5" cy="18" r="3.5" />
                        <circle cx="19" cy="18" r="3.5" />
                        <line x1="12" y1="8.5" x2="6.5" y2="15.5" strokeDasharray="2.5 2.5" />
                        <line x1="12" y1="8.5" x2="17.5" y2="15.5" strokeDasharray="2.5 2.5" />
                        <line x1="8.5" y1="18" x2="15.5" y2="18" strokeDasharray="2.5 2.5" />
                        <path d="M12 11.5l0.8 1.6 1.6 0.8-1.6 0.8-0.8 1.6-0.8-1.6-1.6-0.8 1.6-0.8z" fill="currentColor" stroke="none" />
                    </svg>
                </div>
                <h1>Co-founder Match <span className="gradient-text">Recommender</span></h1>
                <p className="hero-subtitle">AI-powered founder compatibility recommendations using semantic profile matching.</p>
            </header>

            <ProfileSelector
                profiles={profiles}
                selectedProfile={selectedProfile}
                onProfileChange={onProfileChangeAndReset}
                onFindMatches={handleFindMatches}
            />

            {loading && <LoadingSpinner />}

            {error && <ErrorMessage message={error} />}

            {!loading && !error && matches.length > 0 && (
                <>
                    <MatchList matches={matches} />
                    <div className="bottom-status-bar">
                        <div className="status-left">
                            <span className="status-sparkle">✨</span> Showing top 5 compatible founders for <strong className="active-founder-highlight">{profiles.find(p => p.id === parseInt(selectedProfile))?.name}</strong>
                        </div>
                        <div className="status-right">
                            <span className="status-badge">3 of 5 shown</span>
                            <span className="status-divider">•</span>
                            <span className="status-sort-text">Sorted by compatibility</span>
                        </div>
                    </div>
                </>
            )}

            {!loading && !error && matches.length === 0 && (
                <div className="empty-state">
                    <div className="empty-state-icon">👥</div>
                    <h3>Ready to Match</h3>
                    <p>Select a founder profile from the dropdown selector above and click "Find Matches" to discover compatible matches.</p>
                </div>
            )}
        </div>
    );
}

export default App;
