import axios from "axios";

import { BASE_API_URL } from "../utils/constants";

export const backendServices = axios.create({
  baseURL: BASE_API_URL,
});
