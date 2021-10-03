import { StyledColumn } from "./css";

export default function TableBody({ columnNames, columnValues }) {
  return (
    <>
      {columnValues.map((columnValue, ck) => (
        <tr key={ck}>
          {columnNames.map((_, k) => (
            <StyledColumn key={k}>{columnValue[k]}</StyledColumn>
          ))}
        </tr>
      ))}
    </>
  );
}
