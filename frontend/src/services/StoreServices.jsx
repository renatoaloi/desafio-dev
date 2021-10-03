import { backendServices } from "./AxiosFacade";

export const getStores = () =>
  backendServices
    .get("/api/v1/stores")
    .then(({ data }) => data.data)
    .catch((error) => {
      throw error.message;
    });
