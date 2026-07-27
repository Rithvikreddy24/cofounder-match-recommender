import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";
const API_BASE_URL = `${BASE_URL}/api`;

export async function getProfiles() {
    const response = await axios.get(`${API_BASE_URL}/profiles`);
    return response.data;
}

export async function getMatches(userId) {
    const response = await axios.get(`${API_BASE_URL}/matches/${userId}`);
    return response.data;
}