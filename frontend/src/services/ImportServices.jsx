import { backendServices } from "./AxiosFacade";

export const getImports = () =>
  backendServices
    .get("/api/v1/imports")
    .then(({ data }) => data.data)
    .catch((error) => {
      throw error.message;
    });

export const postImports = (data) => {
  const options = {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  };
  return backendServices
    .post("/api/v1/file/1/import", data, options)
    .then(({ data }) => data.data)
    .catch((error) => {
      throw error.message;
    });
};
