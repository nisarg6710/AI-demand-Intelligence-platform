// single place of frontend-backend communication
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const getAnalytics = async (question) => {
  const response = await api.post("/analytics", {
    question,
  });

  return response.data;
};

export const getForecast = async (question) => {
  const response = await api.post("/forecast", {
    question,
  });

  return response.data;
};

export const getChat = async (question) => {
  const response = await api.post("/chat", {
    question,
  });

  return response.data;
};

export const getReport = async (question) => {
  const response = await api.post("/report", {
    question,
  });

  return response.data;
};

export const getHealth = async () => {
  const response = await api.get("/health");

  return response.data;
};

export const getMonthlySales = async () => {
  const response = await api.get("/analytics/monthly-sales");

  return response.data;
};

export const getSalesSummary = async () => {
  const response = await api.get("/analytics/summary");
  return response.data;
};

export const getTopStores = async () => {
  const response = await api.get("/analytics/top-stores");
  return response.data;
};

export const getCategoryPerformance = async () => {
  const response = await api.get("/analytics/category-performance");
  return response.data;
};

export default api;