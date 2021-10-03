import { useCallback } from "react";
import { useQuery } from "react-query";

import { getStores } from "../services/StoreServices";

export default function useStores() {
  const {
    data: stores,
    isLoading: isStoresLoading,
    isError: isStoresError,
  } = useQuery("stores", getStores, {
    refetchOnWindowFocus: false,
  });

  const getStore = useCallback(() => {
    return stores;
  }, [stores]);

  return {
    stores,
    isStoresLoading,
    isStoresError,
    getStore,
  };
}
