import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api"
});

export const fetchSuggestions = async (query, debug = false) => {
    const res = await api.get("/autocomplete", {
        params: { query, debug }
    });
    return res.data;
};


export const logSelection = async (term, userId = "guest") => {
  await api.post("/select", null, {
    params: { term, user_id: userId },
  });
};
