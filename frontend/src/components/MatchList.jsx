import MatchCard from "./MatchCard";

function MatchList({ matches }) {
    return (
        <div className="match-list">
            {matches.map((match) => (
                <MatchCard
                    key={match.id}
                    match={match}
                />
            ))}
        </div>
    );
}

export default MatchList;