import { useCallback } from "react";
import { useQuery } from "react-query";

import { getImports } from "../services/ImportServices";

export default function useImports() {
  const {
    data: imports,
    isLoading: isImportsLoading,
    isError: isImportsError,
  } = useQuery("imports", getImports, {
    refetchOnWindowFocus: false,
  });

  const getStore = useCallback(() => {
    return imports;
  }, [imports]);

  return {
    imports,
    isImportsLoading,
    isImportsError,
    getStore,
  };
}
