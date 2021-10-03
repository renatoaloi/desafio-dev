import { H2, Container } from "./css";
import TableLayout from "../common/Tables/TableLayout/TableLayout";
import useStores from "../../hooks/useStores";

export function Stores() {
  const { stores } = useStores();

  return (
    <Container>
      <H2>Lojas</H2>
      {stores && (
        <TableLayout
          columnNames={Object.keys(stores[0])}
          columnValues={stores.map((_, k) => Object.values(stores[k]))}
        />
      )}
    </Container>
  );
}
