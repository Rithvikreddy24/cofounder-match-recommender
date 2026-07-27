function MatchCard({ match }) {
    const getInitials = (name) => {
        if (!name) return "";
        return name
            .split(" ")
            .map((part) => part[0])
            .join("")
            .toUpperCase()
            .slice(0, 2);
    };

    return (
        <div className="match-card">
            <div className="match-card-top">
                <div className="founder-avatar">
                    {getInitials(match.name)}
                </div>
                <div className="founder-info">
                    <h3 className="founder-name">{match.name}</h3>
                    <p className="founder-role">{match.role}</p>
                </div>
                <div className="match-score-badge">
                    <span className="match-score-number">
                        {(match.match_score * 100).toFixed(0)}%
                    </span>
                    <span className="match-score-label">Compatibility</span>
                </div>
            </div>

            <hr className="card-divider" />

            <div className="tags-section">
                <strong className="section-label">
                    <span className="title-icon-wrapper">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" width="12" height="12">
                            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" />
                        </svg>
                    </span>
                    Skills
                </strong>
                <div className="chips-container">
                    {match.skills.map((skill, idx) => (
                        <span key={idx} className="chip chip-skill">
                            {skill}
                        </span>
                    ))}
                </div>
            </div>

            <div className="tags-section">
                <strong className="section-label">
                    <span className="title-icon-wrapper">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" width="12" height="12">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                        </svg>
                    </span>
                    Interests
                </strong>
                <div className="chips-container">
                    {match.interests.map((interest, idx) => (
                        <span key={idx} className="chip chip-interest">
                            {interest}
                        </span>
                    ))}
                </div>
            </div>

            <hr className="card-divider" />

            <div className="match-detail">
                <p>
                    <strong className="detail-label">Experience:</strong> {match.experience} years
                </p>
                <p>
                    <strong className="detail-label">Availability:</strong> {match.availability}
                </p>
            </div>

            <hr className="card-divider" />

            <p className="match-bio">{match.bio}</p>
        </div>
    );
}

export default MatchCard;
