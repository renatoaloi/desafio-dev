import { Container, H2 } from "./css";
import TableLayout from "../common/Tables/TableLayout/TableLayout";
import FileInput from "../common/Forms/FileInput/FileInput";
import Button from "../common/Forms/Button/Button";
import useImports from "../../hooks/useImports";

export function Upload() {
  const { imports } = useImports();

  return (
    <Container>
      <H2>Upload de Arquivo CNAB</H2>
      <FileInput />
      <Button />
      {imports && (
        <TableLayout
          columnNames={Object.keys(imports[0])}
          columnValues={imports.map((_, k) => Object.values(imports[k]))}
        />
      )}
    </Container>
  );
}
