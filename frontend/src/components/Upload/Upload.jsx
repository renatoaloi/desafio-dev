import { Container, H2 } from "./css";
import FileInput from "../common/Forms/FileInput/FileInput";
import Button from "../common/Forms/Button/Button";

export function Upload() {
  return (
    <Container>
      <H2>Upload de Arquivo CNAB</H2>
      <FileInput />
      <Button />
    </Container>
  );
}
