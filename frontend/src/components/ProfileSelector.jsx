import { useState, useRef, useEffect } from "react";

function ProfileSelector({
    profiles,
    selectedProfile,
    onProfileChange,
    onFindMatches
}) {
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef(null);

    // Close the dropdown on outside click
    useEffect(() => {
        function handleClickOutside(event) {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
                setIsOpen(false);
            }
        }
        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, []);

    const selectedFounder = profiles.find((p) => String(p.id) === String(selectedProfile));

    return (
        <div className="profile-selector">
            <label htmlFor="profile-select-trigger">
                <span className="label-icon-wrapper">
                    <svg
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2.5"
                        width="14"
                        height="14"
                        style={{ marginRight: "6px", verticalAlign: "middle" }}
                    >
                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                        <circle cx="12" cy="7" r="4" />
                    </svg>
                </span>
                Select Founder Profile
            </label>

            <div className="custom-dropdown" ref={dropdownRef}>
                <button
                    id="profile-select-trigger"
                    type="button"
                    className={`dropdown-trigger ${isOpen ? "active" : ""}`}
                    onClick={() => setIsOpen(!isOpen)}
                    aria-haspopup="listbox"
                    aria-expanded={isOpen}
                >
                    <span className="selected-value">
                        {selectedFounder ? selectedFounder.name : "-- Select a Founder --"}
                    </span>
                    <span className="dropdown-arrow">
                        <svg
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="2.5"
                            width="12"
                            height="12"
                        >
                            <path d="m6 9 6 6 6-6" />
                        </svg>
                    </span>
                </button>

                {isOpen && (
                    <ul className="dropdown-options" role="listbox">
                        <li
                            className={`dropdown-option ${!selectedProfile ? "selected" : ""}`}
                            role="option"
                            aria-selected={!selectedProfile}
                            onClick={() => {
                                onProfileChange("");
                                setIsOpen(false);
                            }}
                        >
                            -- Select a Founder --
                        </li>
                        {profiles.map((profile) => (
                            <li
                                key={profile.id}
                                className={`dropdown-option ${
                                    String(selectedProfile) === String(profile.id) ? "selected" : ""
                                }`}
                                role="option"
                                aria-selected={String(selectedProfile) === String(profile.id)}
                                onClick={() => {
                                    onProfileChange(String(profile.id));
                                    setIsOpen(false);
                                }}
                            >
                                {profile.name}
                            </li>
                        ))}
                    </ul>
                )}
            </div>

            <button
                type="button"
                className="find-matches-btn"
                onClick={onFindMatches}
                disabled={!selectedProfile}
            >
                Find Matches
            </button>
        </div>
    );
}

export default ProfileSelector;