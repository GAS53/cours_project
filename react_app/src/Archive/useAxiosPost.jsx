import { useState, useEffect } from "react";
import axios from "axios";

export const useAxiosPost = (url, payload) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const [loaded, setLoaded] = useState(false);

  axios.defaults.baseURL='http://127.0.0.1:8000/api/'
  const headers = {"Content-Type": "application/json", }
  useEffect(() => {
    axios
      .post(url, payload, {"Content-Type": "application/json", })
      .then((response) => setData(response.data))
      .catch((error) => setError(error.message))
      .finally(() => setLoaded(true));
  }, []);

  return { data, error, loaded };
};

