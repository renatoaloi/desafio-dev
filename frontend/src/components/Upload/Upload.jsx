import { Container, H2, StyledForm } from "./css";
import TableLayout from "../common/Tables/TableLayout/TableLayout";
import Button from "../common/Forms/Button/Button";
import useImports from "../../hooks/useImports";
import { useForm } from "react-hook-form";
import { postImports } from "../../services/ImportServices";
import { useEffect } from "react";

export function Upload({ onInvalidateQuery, onNotify }) {
  const { imports } = useImports();
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm();

  const onSubmit = (data) => {
    var bodyFormData = new FormData();
    bodyFormData.append("file", data.file[0]);
    var tzoffset = new Date().getTimezoneOffset() * 60000;
    var nowDate = new Date(Date.now() - tzoffset);
    nowDate.setSeconds(nowDate.getSeconds() + 10);
    bodyFormData.append(
      "execution_datetime",
      nowDate.toISOString().slice(0, -1)
    );
    postImports(bodyFormData).then(() => {
      onInvalidateQuery("imports");
      reset();
      onNotify("Arquivo registrado na fila com sucesso!");
    });
  };

  useEffect(() => {
    if (errors.file) {
      onNotify("O campo file é obrigatório!");
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [errors]);

  return (
    <Container>
      <H2>Upload de Arquivo CNAB</H2>
      <StyledForm>
        <form onSubmit={handleSubmit(onSubmit)}>
          <input type="file" {...register("file", { required: true })} />
          <Button />
        </form>
      </StyledForm>
      {imports && (
        <TableLayout
          columnNames={Object.keys(imports[0])}
          columnValues={imports.map((_, k) => Object.values(imports[k]))}
        />
      )}
    </Container>
  );
}
