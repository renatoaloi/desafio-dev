import { backendServices } from "./AxiosFacade";

export const getImports = () =>
  backendServices
    .get("/api/v1/imports")
    .then(({ data }) => data.data)
    .catch((error) => {
      throw error.message;
    });
